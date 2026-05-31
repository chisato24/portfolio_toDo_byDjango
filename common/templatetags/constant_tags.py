import importlib
from pathlib import Path
from django import template
from django.conf import settings

register = template.Library()


class ConstantProxy:
   """定数クラスへのアクセスを提供するプロキシクラス"""
   
   _constants_cache = None
   
   @classmethod
   def load_all_constants(cls):
      """constantsフォルダ配下のすべての定数クラスを読み込む"""
      if cls._constants_cache is not None:
         return cls._constants_cache
      
      constants = {}
      
      # constantsフォルダのパスを取得
      base_dir = Path(settings.BASE_DIR)
      constants_dir = base_dir / 'constants'
        
      if not constants_dir.exists():
         return constants
      
      # constantsフォルダ内のすべてのPythonファイルを走査
      for file_path in constants_dir.glob('*.py'):
         if file_path.name.startswith('_'):
            continue
      
         # モジュール名を取得 (例: user_status.py -> user_status)
         module_name = file_path.stem

         try:
            # モジュールを動的にインポート
            module = importlib.import_module(f'constants.{module_name}')
         
            # モジュール内のクラスを取得
            for attr_name in dir(module):
               if attr_name.startswith('_'):
                  continue
            
               attr_value = getattr(module, attr_name)
            
               # クラスの場合のみ登録
               if isinstance(attr_value, type):
                  constants[attr_name] = attr_value
         except ImportError as e:
            print(f"Warning: Could not import constants.{module_name}: {e}")
            continue

      cls._constants_cache = constants
      return constants


   def __getattr__(self, name):
      """{{ UserStatus.ACTIVE }} のようにアクセスできるようにする"""
      constants = self.load_all_constants()
      if name in constants:
         return constants[name]
      raise AttributeError(f"Constant class '{name}' not found")


    def __getitem__(self, name):
      """辞書形式でもアクセスできるようにする"""
      return self.__getattr__(name)


# グローバルなConstantProxyインスタンスを作成
_constant_proxy = ConstantProxy()


@register.simple_tag
def UserStatus():
   """{{ UserStatus.ACTIVE }} で使用"""
   return _constant_proxy.load_all_constants().get('UserStatus')

@register.simple_tag
def OrderStatus():
   """{{ OrderStatus.PENDING }} で使用"""
   return _constant_proxy.load_all_constants().get('OrderStatus')

@register.simple_tag
def PaymentMethod():
   """{{ PaymentMethod.CREDIT_CARD }} で使用"""
   return _constant_proxy.load_all_constants().get('PaymentMethod')


# より汎用的なアプローチ: すべての定数クラスを自動登録
def _auto_register_constants():
   """定数クラスを自動的にテンプレートタグとして登録"""
   constants = ConstantProxy.load_all_constants()
    
   for class_name, class_obj in constants.items():
      # 動的にテンプレートタグを作成
      def make_tag(cls_obj):
         def tag_func():
            return cls_obj
         return tag_func
      
      # テンプレートタグとして登録
      register.simple_tag(name=class_name)(make_tag(class_obj))

# テンプレートタグを自動登録
_auto_register_constants()


# テンプレートフィルタ: {{ 1|constant_label:'UserStatus' }}
@register.filter
def constant_label(value, class_name):
   """定数のCHOICESから値に対応するラベルを取得"""
   constants = ConstantProxy.load_all_constants()
    
   if class_name not in constants:
      return value
   
   constant_class = constants[class_name]
   choices = getattr(constant_class, 'CHOICES', None)
   
   if not choices:
      return value
   
   for choice_value, choice_label in choices:
      if choice_value == value:
         return choice_label
   
   return value


# コンテキストプロセッサとして使用する場合（オプション）
# settings.pyのTEMPLATESに追加:
# 'context_processors': [
#     'core.context_processors.constants_processor',
# ]
def constants_processor(request):
   """すべてのテンプレートで定数クラスを直接使用可能にする"""
   return ConstantProxy.load_all_constants()
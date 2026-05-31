from common.templatetags.constant_tags import ConstantProxy

def constants_processor(request):
    """すべてのテンプレートで定数クラスを直接使用可能にする"""
    return ConstantProxy.load_all_constants()
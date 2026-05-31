# ログインユーザーに関する権限の定数クラス

class Permission():
   # サービス管理者（全権）
   ADMIN_SERVICE = 1
   
   # システム管理者
   ADMIN_SYSTEM = 2
   
   # 一般ユーザー
   GENERAL = 3
   
   # ゲスト
   GUEST = 4
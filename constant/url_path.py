# ブラウザ上に表示されるURLの実パスの定数定義
class UrlPath():
   # 認証
   AUTH = ""
   # ログイン
   AUTH_LOGIN = AUTH
   # ログアウト
   AUTH_LOGOUT = AUTH + "/logout/"
   
   # 共通
   COMMON = ""
   # ダッシュボード（トップページ）
   COMMON_DASHBOARD = "dashboard/"
   # ダッシュボード中の今日のタスク
   COMMON_TODAY_TODO = "today_todo/"
   
   # タスク管理ページ
   TASK = "task/"
   # タスク作成
   TASK_CREATE = TASK + "create/"
   # タスク編集
   TASK_EDIT = TASK + "edit/"
   # タスク一覧
   TASK_LIST = TASK + "list/"

   # 設定画面
   SETTING = "setting/"
   # ユーザー設定
   SETTING_USER = SETTING + "user/"
   # ログ一覧
   SETTING_LOG_LIST = SETTING + "log_list/"
   # ログ詳細
   SETTING_LOG_DETAIL = SETTING + "log_detail/"
   
   # 管理画面
   ADMIN = "admin/"
# テンプレートまたは静的ファイルのパスの定数定義
class FilesPath():
   # 認証
   AUTH = "auth/"
   # ログイン
   AUTH_LOGIN = AUTH + "login.html"
   # ログアウト
   AUTH_LOGOUT = AUTH + "logout.html"
   
   # 共通
   COMMON = "common/"
   # headタグ
   COMMON_HEAD = COMMON + "head.html"
   # 共通部分
   COMMON_MAIN = COMMON + "main.html"
   # ダッシュボード（トップページ）
   COMMON_DASHBOARD = COMMON + "dashboard.html"
   # ダッシュボード中の今日のタスク
   COMMON_TODAY_TODO = COMMON + "today_todo.html"
   
   # タスク管理ページ
   TASK = "task/"
   # タスク作成・編集・詳細フォーム
   TASK_FORM = TASK + "task_form.html"
   # タスク一覧
   TASK_LIST = TASK + "list.html"

   # 設定画面
   SETTING = "setting/"
   # ユーザー設定
   SETTING_USER = SETTING + "user.html"
   # ログ一覧
   SETTING_LOG_LIST = SETTING + "log_list.html"
   # ログ詳細
   SETTING_LOG_DETAIL = SETTING + "log_detail.html"
   
   # 管理画面
   ADMIN = "admin/"
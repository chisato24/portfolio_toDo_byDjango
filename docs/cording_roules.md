# 本アプリケーションにおけるコーディングルール

## すべての言語に共通すること
- インデント：半角空白4文字
- ハードコーディング：基本的に行わない
  - Python定数ファイルを作成・使用することで回避する
- マジックナンバー：基本的に使用しない
  - Python定数ファイルを作成・使用することで回避する
- 文字コード：BOM無しUTF-8
- コーディングの方針：「誰でも理解できる」を目指し、基本の書き方を重視する
- 品質担保：VS Codeの拡張機能（Formatter、Linter）を使用して担保する


## Python
### 全体として
- 変数：スネークケース（var_name）
- 定数：大文字スネークケース（CONST_NAME）
  - ルート/constに定数種別ごとに定数ファイルを作成する。ファイル名は「const_name.py」とする
- 関数名：スネークケース（def def_name(引数):）
- クラス名：パスカルケース（class ClassName(self, 引数):）
- 文字列：ダブルクォーテーション（""）
  - ただし、フォーマット文字列はバッククォートになる（f`string{var_name}string`）
- 例外処理：以下のルールに従い、UI上でのメッセージ表示とアクティビティログ作成を行う
  - 正常：ステータスsuccessで詳細ログを保存＋簡便な成功メッセージを表示（例：保存に成功しました）
  - 失敗：ステータスerrorで詳細ログを保存＋簡便な失敗メッセージを表示（例：保存に失敗しました）

### Django特有のもの
- フロントへの出力：render()・redirect()・HttpResponse()を適宜使い分ける
  - render()：画面の一部分を更新する内容を出力するとき
  - redirect()：別のviewsの処理を続けて行うとき
  - HttpResponse()：正常または異常のメッセージのみをフロントに返すとき
- 共通処理関数：root/service配下に関数ファイルを作成し、関数を記述→使用するファイルでimport


## HTML/CSS
### 共通
 - Googleのガイドラインに従う：https://google.github.io/styleguide/htmlcssguide.html

### HTML
 - class：適宜使用。表記はケバブケース（class-name）とする
 - id：必要な場合のみ定義する。表記はケバブケース（役割（container等）-name）とする
 - idおよびclassはタグセレクタ指定で対応できる場合、セレクタ使用を優先する
 - 入れ子構造：構造の複雑化・レスポンス悪化を避けるため、最低限にとどめる
 - コメント：基本的にDjangoテンプレートタグ（{% comment %}～{% endcomment %}）とし、F12での表示を回避する

### CSS
- 外部cssファイル間でのオーバーライドに注意
- 全画面で共通して使用する設定はcommon.cssにまとめる
- 画面固有の設定は各アプリにstatic/css/アプリ名.cssを作成し、適宜<head>タグ内のパスを変更する（全部読み込むと重くなるため）

## Javascript
 - 位置付け：画面表示完了後の動的処理の補完として使用する。Djangoテンプレートタグで代用できる処理ものはテンプレートタグを優先させる
 - MDN Docsのガイドライン（https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Introduction）に従う
 - ES2025準拠　　参考：https://qiita.com/rana_kualu/items/e82790fa50c05b167dcc
 - 複数画面で使用するメソッドについてはstatic/js/commonにjsファイルを作成し、使用箇所でimportを行う
 - 変数：なんでもかんでもletで宣言しない。キャメルケース（var varName / let varName）
 - 定数：大文字スネークケース（const CONST_NAME）
 - 関数名：キャメルケース（function myFunc(引数){} ）
 - 文字列：Pythonと同じ
 - イベント：イベントリスナ推奨
 - 非同期通信：fetch()を使用する
 - 例外処理：Pythonと同じ


以上

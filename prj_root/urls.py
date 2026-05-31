"""
各アプリのurls.pyへのルーティング

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from constant.url_path import UrlPath

urlpatterns = [
    path(UrlPath.ADMIN, admin.site.urls),
    path(UrlPath.AUTH, include('auth.urls'), namespace="auth"),   # 認証
    path(UrlPath.COMMON, include('common.urls'), namespace="common"),   # 共通部分
    path(UrlPath.TASK, include('task.urls'), namespace="task"),   # タスク管理
    path(UrlPath.SETTING, include('setting.urls', namespace="setting")),   # 設定
]

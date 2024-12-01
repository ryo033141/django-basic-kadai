"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# Django の管理サイトを利用するために必要なモジュールをインポートする文
from django.contrib import admin
from django.urls import path
from crud import views
# settings.pyをインポートする
from django.conf import settings
# DjangoのURL設定で 静的ファイルやメディアファイルを開発環境で提供するため に使用される関数をインポート
from django.conf.urls.static import static

urlpatterns = [
    # Django の管理サイト（Admin Interface）にアクセスするための URL パターンを定義
    path("admin/", admin.site.urls),
    path('',views.TopView.as_view(),name="top"),
    path("crud/",views.ProductListView.as_view(),name="list"),
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]

# 開発環境のみで動作するように動作を切り替える
# 画像を静的ファイルとして扱う
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
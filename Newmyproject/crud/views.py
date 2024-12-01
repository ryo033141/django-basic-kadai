# Django フレームワークでビュー関数を作成する際によく使用されるインポート文
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
"""
商品を新規作成するためのViewを追加
新規作成に特化したCreateViewクラス
既存のモデルオブジェクトを編集するフォームを表示し、更新内容を保存するUpdateViewクラス
既存のモデルオブジェクトを削除するためのDeleteViewクラスをインポート
"""
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# models.pyからProductクラスをインポート
from .models import Product
# 削除成功時に遷移するURLを指定するためのインポート文
from django.urls import reverse_lazy
# Djangoアプリケーションにログイン・ログアウト機能を組み込むためのインポート文
from django.contrib.auth.views import LoginView, LogoutView
# ログインしていなければアクセスできないようにするためのインポート文
from django.contrib.auth.mixins import LoginRequiredMixin
# Djangoで提供されているログイン用の組み込みフォームを使用するためのインポート文
from django.contrib.auth.forms import AuthenticationForm

# TopView クラスは TemplateView を継承し、指定したテンプレート (top.html) を表示する
class TopView(TemplateView):
  template_name = "top.html"

# データの一覧表示に特化したListViewクラスを利用する
# LoginRequiredMixinクラスとListViewクラスを継承したクラスを定義
# ログインしていなければアクセスできない
class ProductListView(LoginRequiredMixin, ListView):
  # 対象のModelクラスを指定する
  model = Product
  # 1ページに表示する数を指定
  # 1ページに3件表示するように指定
  paginate_by = 3

# 新規作成に特化したCreateViewを使用する
# LoginRequiredMixinクラスとCreateViewを継承したクラスを定義
# ログインしていなければアクセスできない
class ProductCreateView(LoginRequiredMixin, CreateView):
  # 対象のModelクラスを指定する
  model = Product
  # 新規作成時にユーザが入力するフィールドを指定する
  # 全フィールドを指定する
  fields = '__all__'

# 編集に特化したUpdateViewクラスを利用する
# LoginRequiredMixinクラスとUpdateViewを継承したクラスを定義
# ログインしていなければアクセスできない
class ProductUpdateView(LoginRequiredMixin, UpdateView):
  # 対象のModelクラスを指定する
  model = Product
  # 新規作成時にユーザが入力するフィールドを指定する
  # 全フィールドを指定する
  fields = '__all__'
  # 編集用のTemplateファイル名を指定する
  template_name_suffix = '_update_form'

# 削除に特化したDeleteViewクラスを利用する
# LoginRequiredMixinクラスとDeleteViewを継承したクラスを定義
# ログインしていなければアクセスできない
class ProductDeleteView(LoginRequiredMixin, DeleteView):
  # 対象のModelクラスを指定する
  model = Product
  # 削除成功時に遷移するURLを指定
  # ここでは一覧画面を指定する
  success_url = reverse_lazy('list')

# データの詳細表示に特化したDetailViewクラスを利用する
# LoginRequiredMixinクラスとDetailViewを継承したクラスを定義
# ログインしていなければアクセスできない
class ProductDetailView(LoginRequiredMixin, DetailView):
  # 対象のModelクラスを指定する
  model = Product

# ログインに特化したLoginViewクラスを利用する
# LoginViewクラスを継承したクラスを定義
class LoginView(LoginView):
  # デフォルトで用意されているAuthenticationFormを指定
  form_class = AuthenticationForm
  # Templateファイル名を指定
  template_name = 'login.html'

# ログアウトに特化したLogoutViewクラスを利用する
# LoginRequiredMixinクラスとLogoutViewクラスを継承したクラスを定義
# ログインしていなければアクセスできない
class LogoutView(LoginRequiredMixin, LogoutView):
  # Templateファイル名を指定する
  template_name = 'top.html'
# Djangoの管理画面機能を利用するためのインポート文
from django.contrib import admin
# models.pyからProductクラスをインポート
from .models import Product

# ProductAdmin クラスは、admin.ModelAdmin を継承している
# Djangoの管理画面の設定を管理するためのクラス
class ProductAdmin(admin.ModelAdmin):
  # 管理画面でのモデルの一覧表示時に表示するフィールドを指定する設定
  list_display = ('id', 'name', 'price')
  # 管理画面で検索ボックスを使って検索可能にしたいフィールドを指定
  search_fields = ('name',)

# Djangoの管理画面にProductモデルを登録するための命令
admin.site.register(Product,ProductAdmin)
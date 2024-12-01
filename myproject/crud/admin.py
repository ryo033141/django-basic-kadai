# Djangoの管理画面機能を利用するためのインポート文
from django.contrib import admin
# models.pyからProductクラス、Categoryクラスをインポート
from .models import Product, Category
# DjangoでHTMLを安全にレンダリングするために使用される関数をインポート
from django.utils.safestring import mark_safe

# admin.ModelAdminを継承しているProductAdminクラスを定義
# Djangoの管理画面の設定を管理するためのクラス
class ProductAdmin(admin.ModelAdmin):
  # 管理画面でのモデルの一覧表示時に表示するフィールドを指定する設定
  # カテゴリのID、商品名、値段、カテゴリ、画像を表示する
  list_display = ('id', 'name', 'price', 'category', 'image')
  # 管理画面で検索ボックスを使って検索可能にしたいフィールドを指定
  # 商品名で検索可能にする
  search_fields = ('name',)
  # 絞り込みフィルターにカテゴリを追加
  list_filter = ('category',)

  def image(self, obj):
    # HTMLで画像を表示するにはimgタグを使用する
    # 管理画面にimgタグを出力するためにmark_safe関数を使用する
    # mark_safe関数は指定した文字列が安全であるという印をつけて、HTMLを出力
    return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

# admin.ModelAdminを継承しているCategoryAdminクラスを定義
class CategoryAdmin(admin.ModelAdmin):
  # 管理画面でのモデルの一覧表示時に表示するフィールドを指定する設定
  # カテゴリのIDと名前を表示する
  list_display = ('id', 'name')
  # 管理画面で検索ボックスを使って検索可能にしたいフィールドを指定
  # カテゴリ名で検索可能とする
  search_fields = ('name',)

# Djangoの管理画面にProductモデルを登録するための命令
admin.site.register(Product,ProductAdmin)
# Djangoの管理画面にCategoryモデルを登録するための命令
admin.site.register(Category,CategoryAdmin)
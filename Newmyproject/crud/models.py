# Djangoのモデル機能を使うために必要なインポート文
# Djangoのモデルはデータベースと連携してデータを管理するためのクラスを定義するのに使用される
from django.db import models
# DjangoでURLを生成するための関数reverseをインポートする文
from django.urls import reverse

# models.Modelを継承するCategoryクラスを定義
class Category(models.Model):
   # カテゴリ名を文字列で定義する 最大文字列長は200
  name = models.CharField(max_length=200)

  # カテゴリ名を返す
  def __str__(self):
    return self.name

# models.Modelを継承している
class Product(models.Model):
  # 商品名を文字列型で定義する　最大文字列長は200
  name = models.CharField(max_length=200)
  # 金額を正の整数型で定義する
  price = models.PositiveBigIntegerField()
  # 「1：多」のリレーションを追加する
  # on_deleteは紐づいているデータが削除された場合の振る舞いを指定する
  # Categoryが削除されたらCategoryに紐づいているProductも削除する「models.CASCADE」を指定
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  # Productクラスに画像フィールドを追加
  # 画像フィールドを追加する画像は省略可能で、省略時はデフォルト画像として、noImage.pngが使用される
  img = models.ImageField(blank=True, default='noImage.png')
  # Productクラスに商品詳細の説明を追加するためのフィールドを追加
  detail = models.TextField(blank=True, null=True)

  # str(self)を定義すると、一覧画面で表示される名称を変更できる
  # 商品名を返す
  def __str__(self):
    return self.name
  # 新規作成・編集完了時のリダイレクト先
  # 新規作成後に一覧画面へ遷移する
  def get_absolute_url(self):
    # reverse関数：名前からURLを取得する
    return reverse('list')

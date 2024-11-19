# Djangoのモデル機能を使うために必要なインポート文
# Djangoのモデルはデータベースと連携してデータを管理するためのクラスを定義するのに使用される
from django.db import models
# DjangoでURLを生成するための関数reverseをインポートする文
from django.urls import reverse

# models.Modelを継承している
class Product(models.Model):
  # 商品名を文字列型で定義する　最大文字列長は200
  name = models.CharField(max_length=200)
  # 金額を正の整数型で定義する
  price = models.PositiveBigIntegerField()

  # str(self)を定義すると、一覧画面で表示される名称を変更できる
  # 商品名を返す
  def __str__(self):
    return self.name
  # 新規作成・編集完了時のリダイレクト先
  # 新規作成後に一覧画面へ遷移する
  def get_absolute_url(self):
    # reverse関数：名前からURLを取得する
    return reverse('list')

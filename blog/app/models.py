from django.db import models

# カテゴリー
class Category(models.Model):
    # 名前
    name = models.CharField(max_length=20)

    # 作成日
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# サブカテゴリー
class SubCategory(models.Model):
    # 名前
    name = models.CharField(max_length=20)

    # 作成日
    created_datetime = models.DateTimeField(auto_now_add=True)

    # 親カテゴリー
    target_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# タグ
class Tag(models.Model):
    # 名前
    name = models.CharField(max_length=50)

    #作成日
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 記事
class Post(models.Model):
    # タイトル
    title = models.CharField(max_length=100)

    # テキスト
    main_sentence = models.TextField(blank=True)

    # 作成日と更新日
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    # サブカテゴリー
    target_subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)

    # タグ
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


# コメント
class Comment(models.Model):
    # 投稿者の名前
    name = models.CharField("名前" ,max_length=50)

    # 年齢
    age = models.PositiveSmallIntegerField("年齢", default=25)

    # 性別の選択肢
    SEX_CHOICES = (
        ("男性", "男性"),
        ("女性", "女性"),
    )

    # 性別
    sex = models.CharField("性別", max_length=5, choices=SEX_CHOICES, default="男性")

    # 内容
    text = models.TextField("内容")

    # 作成日
    created_datetime = models.DateTimeField("作成日",auto_now_add=True)

    # どの記事についてか
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="対象記事", null=True)

    def __str__(self):
        return self.text[:20]

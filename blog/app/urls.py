from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "app"

urlpatterns = [
    # 最新記事一覧　検索による絞り込みの結果一覧
    path("", views.TopView.as_view(), name="top"),

    # 記事の詳細
    path("post_detail/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),

    # ブログの紹介
    path("about_blog/", TemplateView.as_view(template_name="app/about_blog.html"), name="about_blog"),

    # 自己紹介
    path("about_writer/", TemplateView.as_view(template_name="app/about_writer.html"), name="about_writer"),

    # サブカテゴリーによる絞り込みの結果一覧
    path("subcategory/<str:subcategory>/", views.SubCategoryView.as_view(), name="subcategory"),

    # タグによる絞り込みの結果一覧
    path("tag/<str:t>/", views.TagView.as_view(), name="tag"),
]

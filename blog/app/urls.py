from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "app"

urlpatterns = [
    # TOP
    path("", views.TopView.as_view(), name="top"),

    # 記事の詳細
    path("post_detail/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),

    # ブログの紹介
    path("about_blog/", TemplateView.as_view(template_name="app/about_blog.html"), name="about_blog"),

    # 自己紹介
    path("about_writer/", TemplateView.as_view(template_name="app/about_writer.html"), name="about_writer"),

    # サブカテゴリー
    path("subcategory/<str:subcategory>/", views.SubCategoryView.as_view(), name="subcategory"),

    # タグ
    path("tag/<str:t>/", views.TagView.as_view(), name="tag"),
]

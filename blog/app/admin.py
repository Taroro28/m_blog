from django.contrib import admin
from .models import Post, Comment, Category, SubCategory, Tag

# 記事
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', "target_subcategory", "tags", 'title', 'created_datetime', 'updated_datetime', "main_sentence")
    list_display_links = ('id', 'title', "target_subcategory")

    def tags(self, row):
        return " ".join([x.name for x in row.tag.all()])

# コメント
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "text", "created_datetime")
    list_display_links = ("name", "text")

# カテゴリー
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_datetime")

# サブカテゴリー
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("target_category", "name", "created_datetime")
    list_display_links = ("target_category",)

# タグ
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_datetime")
    list_display_links = ("name",)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag, TagAdmin)

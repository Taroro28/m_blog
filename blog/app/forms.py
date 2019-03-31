from django import forms
from .models import Comment

# コメント投稿
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","text", )
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "お名前を入力して下さい。"}),
            "text": forms.Textarea(attrs={"placeholder": "コメントを入力して下さい。"}),
        }

# 記事検索
class PostSearchForm(forms.Form):
    keyword = forms.CharField(
        required = False,
        widget = forms.TextInput(
            attrs={"class": "search_input", "placeholder": "キーワード検索"}
        ),
    )

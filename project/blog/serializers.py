from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('title', 'content', 'created_at', 'updated_at', 'category_id', 'author')
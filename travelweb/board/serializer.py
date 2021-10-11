from rest_framework import serializers
from board.models import Category, Board, Comment


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    category_id = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'username', 'category_id', 'title', 'imgUrl',
                  'schedule_id', 'date', 'board_content', 'hit', 'like']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'board_id', 'user_id', 'comment_content', 'comment_date']

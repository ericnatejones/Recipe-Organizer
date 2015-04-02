from rest_framework import serializers
from models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)


    class Meta:
        model = Recipe


    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            try:
                ingredient = Ingredient.objects.get(name=ingredient["name"])
            except Ingredient.DoesNotExist():
                ingredient = Ingredient.objects.create(**ingredient)
            recipe.ingredients.add(ingredient)
        return recipe


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

    def get_comments(self, obj):
        comments = Comment.objects.filter(recipe=obj.id)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data




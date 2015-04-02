from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, help_text="This is a quick description of your recipe")
    directions = models.TextField(help_text="How to make the recipe")
    ingredients = models.ManyToManyField(Ingredient)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    # meal = models.ManyToManyField(Meal)

    def __str__(self):
        return self.name

class Comment(models.Model):
    # user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text
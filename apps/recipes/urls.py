from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings

urlpatterns = patterns(
    '',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^ingredients/$', IngredientList.as_view(), name='ingredient-list'),
    url(r'^add-recipe$', RecipeList.as_view(), name='add-recipe'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^commentList/$', CommentList.as_view(), name='comment-list'),
    # Handling media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
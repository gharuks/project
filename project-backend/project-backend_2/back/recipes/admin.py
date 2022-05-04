from django.contrib import admin

from recipes.models import Recipes, Category, Ingredients


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tag', )
    search_fields = ('name', 'like',)
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(Ingredients)
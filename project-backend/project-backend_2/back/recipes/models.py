from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, default='')
    # firstName = models.CharField(max_length=255, default= '')
    # lastName = models.CharField(max_length=255, default = '')
    # def create(nm):
    #     person = UserProfile.objects.create(name = nm)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Recipes(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(default = '')
    tag = models.CharField(max_length = 255)
    image = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name='Recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='Recipes')


    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name} | {self.tag}'

    def to_json(self):
        return {
            # 'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description,
            'tag': self.tag,
            'image': self.image,
            'like': self.like,
            'dislike': self.dislike,
            'category': self.category
        }


class Ingredients(models.Model):
    ing1 = models.CharField(max_length=300, default="")
    amount1 = models.CharField(max_length=300, default="")
    ing2 = models.CharField(max_length=300, default="")
    amount2 = models.CharField(max_length=300, default="")
    ing3 = models.CharField(max_length=300, default="")
    amount3 = models.CharField(max_length=300, default="")
    ing4 = models.CharField(max_length=300, default="")
    amount4 = models.CharField(max_length=300, default="")
    ing5 = models.CharField(max_length=300, default="")
    amount5 = models.CharField(max_length=300, default="")
    ing6 = models.CharField(max_length=300, default="")
    amount6 = models.CharField(max_length=300, default="")
    ing7 = models.CharField(max_length=300, default="")
    amount7 = models.CharField(max_length=300, default="")
    ing8 = models.CharField(max_length=300, default="")
    amount8 = models.CharField(max_length=300, default="")
    step1 = models.TextField(max_length=1000, default="")
    step2 = models.TextField(max_length=1000, default="")
    step3 = models.TextField(max_length=1000, default="")
    step4 = models.TextField(max_length=1000, default="")
    step5 = models.TextField(max_length=1000, default="")
    step6 = models.TextField(max_length=1000, default="")
    step7 = models.TextField(max_length=1000, default="")
    step8 = models.TextField(max_length=1000, default="")
    step9 = models.TextField(max_length=1000, default="")

    ingredient_id = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True, related_name='Ingredients')

    def to_json(self):
        return {
            'id': self.id,
            'ing1': self.ing1,
            'amount1': self.amount1,
            'ing2': self.ing2,
            'amount2': self.amount2,
            'ing3': self.ing3,
            'amount3': self.amount3,
            'ing4': self.ing4,
            'amount4': self.amount4,
            'ing5': self.ing5,
            'amount5': self.amount5,
            'ing6': self.ing6,
            'amount6': self.amount6,
            'ing7': self.ing7,
            'amount7': self.amount7,
            'ing8': self.ing8,
            'amount8': self.amount8,
            'step1': self.step1,
            'step2': self.step2,
            'step3': self.step3,
            'step4': self.step4,
            'step5': self.step5,
            'step6': self.step6,
            'step7': self.step7,
            'step8': self.step8,
            'step9': self.step9,
            'ingredient_id': self.ingredient_id
        }

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}'
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from rest_framework import serializers
from recipes.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher
import bcrypt

# Model Serializers

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'username', 'password', )

# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer
#     class Meta:
#         model = UserProfile
#         fields = ('user', 'name', 'recipes')
# {
#     'user': {
#         'id': '1'
#         'username': 'asd',
#         'password': 'asdf'
#     },
#     'name' : 'profile name'
# }
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length = 5)

    encoder = BCryptSHA256PasswordHasher()

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        

    def create(self, validated_data):
        try:
            password = validated_data.pop('password')
            hashed_password = self.encoder.encode(password, salt=self.encoder.salt())
            user = User.objects.create(password=hashed_password, username=validated_data['username'])
            user.save()
            return user
        except:
            return

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data['name'])
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance

class CategorySerializer2(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'name',)



class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    tag = serializers.CharField()
    image = serializers.CharField()
    like = serializers.IntegerField()
    dislike = serializers.IntegerField()
    # author_id = serializers.IntegerField(write_only=True)
    author = UserSerializer(required=False)
    
    def create(self, validated_data):
        recipe = Recipes.objects.create(name=validated_data.get('name'), 
        author= validated_data.get('author'),
        description = validated_data.get('description'), 
        tag= validated_data.get('tag'), 
        image=validated_data.get('image'), 
        like= validated_data.get('like'),
        dislike=validated_data.get('dislike'))
        recipe.save()
        return recipe

    def update(self, instance, validated_data):
        instance.like = validated_data['like']
        instance.dislike = validated_data['dislike']
        instance.name = validated_data['name']
        instance.save()
        return instance

    def put(self, instance, validated_data):
        instance.like = validated_data['like']
        instance.dislike = validated_data['dislike']
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

class RecipeSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    tag = serializers.CharField()
    image = serializers.CharField()
    like = serializers.IntegerField()
    dislike = serializers.IntegerField()
    author = UserSerializer(required=False)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Recipes
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class IngredientSerializer(serializers.Serializer):
    ing1 = serializers.CharField(max_length=300, default="")
    amount1 = serializers.CharField(max_length=300, default="")
    ing2 = serializers.CharField(max_length=300, default="")
    amount2 = serializers.CharField(max_length=300, default="")
    ing3 = serializers.CharField(max_length=300, default="")
    amount3 = serializers.CharField(max_length=300, default="")
    ing4 = serializers.CharField(max_length=300, default="")
    amount4 = serializers.CharField(max_length=300, default="")
    ing5 = serializers.CharField(max_length=300, default="")
    amount5 = serializers.CharField(max_length=300, default="")
    ing6 = serializers.CharField(max_length=300, default="")
    amount6 = serializers.CharField(max_length=300, default="")
    ing7 = serializers.CharField(max_length=300, default="")
    amount7 = serializers.CharField(max_length=300, default="")
    ing8 = serializers.CharField(max_length=300, default="")
    amount8 = serializers.CharField(max_length=300, default="")
    step1 = serializers.CharField(max_length=1000, default="")
    step2 = serializers.CharField(max_length=1000, default="")
    step3 = serializers.CharField(max_length=1000, default="")
    step4 = serializers.CharField(max_length=1000, default="")
    step5 = serializers.CharField(max_length=1000, default="")
    step6 = serializers.CharField(max_length=1000, default="")
    step7 = serializers.CharField(max_length=1000, default="")
    step8 = serializers.CharField(max_length=1000, default="")
    step9 = serializers.CharField(max_length=1000, default="")

    ingredient_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        ingredients = Ingredients.objects.create(name=validated_data.get('ing1', 'amount1', 'ing2', 'amount2', 'ing3', 'amount3', 'ing4', 'amount4', 'ing5', 'amount5', 'ing6', 'amount6', 'ing7', 'amount7', 'ing8', 'amount8', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'step8', 'step9', 'ingredient_id'))
        return ingredients
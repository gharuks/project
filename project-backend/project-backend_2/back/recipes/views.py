from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from recipes.models import Recipes, Category, Ingredients
from rest_framework.response import Response
from recipes.serializers import *
from rest_framework import status
from django.shortcuts import Http404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(request):
    print(request.user)
    return HttpResponse("ok")



@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = RegisterSerializer(users, many=True)
    return Response(serializer.data)


# FBV
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories_list = Category.objects.all()
        serializer = CategorySerializer2(categories_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CategorySerializer2(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'deleted'}, status=204)


@api_view(['GET', 'POST'])
def recipe_list(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        # print(request.user)
        post_list = Recipes.objects.all()
        serializer = RecipeSerializer(post_list, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            print('success')
            serializer.save(author_id=request.user.id)
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    permission_classes = [IsAuthenticated]
    try:
        post = Recipes.objects.get(id=pk)
    except Recipes.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'PUT':
        serializer = RecipeSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            if str(post.author_id) != str(request.user.id):
                print('someone else attempts to change')
                return JsonResponse({'error': 'not yours'})
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    elif request.method == 'GET':
        # print(request.user)
        serializer = RecipeSerializer(post)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if str(post.author_id) != str(request.user.id):
            print('someone else attempts to change your post')
            return JsonResponse({'error': 'error'})
        post.delete()



@api_view(['GET'])
def ingredient_list(request, pk):
    permission_classes = [IsAuthenticated]
    try:
        post = Ingredients.objects.get(ingredient_id=pk)
    except Ingredients.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)
    if request.method == 'GET':
        serializer = IngredientSerializer(post)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def signup(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        post_list = User.objects.all()
        serializer = RegisterSerializer(post_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print('success')
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors)

# CBV
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def get(self, request):
        post_list = User.objects.all()
        serializer = RegisterSerializer(post_list, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print('success')
            serializer.save()
            return Response(serializer.data)
        else:
            print('oops')
            print(serializer.errors)
        return Response(serializer.errors)

class SignUpView(APIView):
    def get(self, request):
        post_list = User.objects.all()
        serializer = RegisterSerializer(post_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print('success')
            serializer.save()
            return Response(serializer.data)
        else:
            print('oops')
            print(serializer.errors)
        return Response(serializer.errors)

class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all().order_by('id')
        serializer = CategorySerializer2(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        category = self.get_object(pk)
        serializer = CategorySerializer2(category)
        return Response(serializer.data)

    def put(self, request, pk=None):
        category = self.get_object(pk)
        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        category = self.get_object(pk)
        category.delete()
        return Response({'message': 'deleted'}, status=204)
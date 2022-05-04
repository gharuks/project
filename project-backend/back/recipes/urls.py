from recipes.views import recipe_detail, recipe_list, SignUpView, category_list, category_detail, ingredient_list, user_list, signup
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from recipes.views import CategoryDetailAPIView, CategoryListAPIView, Register

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('sign-up/', Register.as_view()),
    # path('sign-up/', signup),
    # path('token-refresh/', refresh_jwt_token),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view()),
    path('recipes/', recipe_list),
    path('recipes/<int:pk>/', recipe_detail),
    # path('ingredients/<int:pk>', ingredient_list),
    path('recipes/<int:pk>/ingredients/', ingredient_list),
    path('users/', user_list),
]
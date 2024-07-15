# """
# test for the recipe apis.
# """
# from decimal import Decimal

# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from  django.urls import reverse

# from rest_framework import status
# from rest_framework.test import APIClient

# from core.models import Recipe

# from recipe.serializers import RecipeSerializer

# RECIPES_URL = reverse('recipe:recipe-list')

# def create_recipe(user, **params):
#     """Create and return a sample recipe."""
#     defaults = {
#         'title': 'sample recipe title',
#         'time_minutes': 10,
#         'price': Decimal('5.99'),
#         'description': 'sample recipe description',
#         'linked': 'https://example.com/sample-recipe',
#     }
#     defaults.update(params)

#     recipe = Recipe.objects.create(user=user, **defaults)
#     return recipe

# class PublicRecipeApiTests(TestCase):
#     """test unauthenticated API requests."""

#     def setUp(self):
#         self.client = APIClient()

#     def test_auth_required(self):
#         """test auth required to call API."""
#         res = self.client.get(RECIPES_URL)

#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

# class PrivateRecipeApiTests(TestCase):
#     """Tests authenticated API requests."""

#     def setUp(self):
#         self.client = APIClient()
#         self.user = get_user_model().objects.create_user(
#             'testuser', 'testpass123',
#         )
#         self.client.force_authenticate(self.user)

#     def test_retrieve_recipes(self):
#         """test retrieving a list of recipes."""
#         create_recipe(user=self.user)
#         create_recipe(user=self.user)

#         res = self.client.get(RECIPES_URL)

#         recipes = Recipe.objects.all().order_by('-id')
#         serializer = RecipeSerializer(recipes, many=True)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertEqual(res.data, serializer.data)

#     def test_recipe_list_limited_to_user(self):
#         """Test list of recipes is limited to authenticated user."""
#         other_user = get_user_model().objects.create_user(
#             'otheruser', 
#             'otherpass123',
#         )
#         create_recipe(user=other_user)
#         create_recipe(user=self.user)

#         res = self.client.get(RECIPES_URL)

#         recipes = Recipe.objects.filter(user=self.user)
#         serializer = RecipeSerializer(recipes, many=True)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertEqual(res.data, serializer.data)

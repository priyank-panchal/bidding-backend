from django.urls import path
from .views import *

urlpatterns = [
      path('registration/',Registration.as_view(),name='regs'),
      path('product/',Product.as_view(),name="product"),
      path('product/<int:pk>',ProductwithParamter.as_view(),name="productwithparamter"),
      path('category/',Category.as_view(),name="category"),
      path('category/<int:pk>',CategoryWithParameters.as_view(),name="categorysingle"),
      path('subcategory/',SubCategory.as_view(),name='subcategory'),
      path('subcategory/<int:pk>',SubCategorywithParamter.as_view(),name='subcategorysingle'),
]
from django.urls import path
from .views import *

urlpatterns = [
      path('registration/',Registration.as_view(),name='regs'),
      path('products/',Product.as_view(),name="product"),
      path('products/<int:pk>',ProductwithParamter.as_view(),name="productwithparamter"),
      path('category/',Category.as_view(),name="category"),
      path('category/<int:pk>',CategoryWithParameters.as_view(),name="categorysingle"),
      path('subcategory/',SubCategory.as_view(),name='subcategory'),
      path('subcategory/<int:pk>',SubCategorywithParamter.as_view(),name='subcategorysingle'),
      path('actioninfo/',Auctioninfo.as_view(),name='actionDetails'),
      path('actioninfo/<int:pk>',AuctionwithParamter.as_view(),name='auctionwithparamters'),
]
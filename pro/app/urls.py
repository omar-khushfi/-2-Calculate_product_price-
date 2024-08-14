from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.view_products,name="product"),
    path('Materials/',views.view_Materials,name="Materials"),
    path('edit-proudct/<int:pk>',views.edit_proudct.as_view(),name="edit-proudct"),
    path('edit-mateiral/<int:pk>',views.edit_mateiral.as_view(),name="edit-material"),
    path('edit_mateiral_product/<int:pk>',views.edit_mateiral_product.as_view(),name="edit-material-product"),
    path('delete-product/<int:pk>',views.delete_product,name="delete-product"),
    path('delete-material/<int:pk>',views.delete_material,name="delete-material"),
    path('delete-material-product/<int:pk>',views.delete_material_product,name="delete-material-product"),
     path('add-product/',views.add_product.as_view(),name="add-product"),
     path('add-material/',views.add_material.as_view(),name="add-material"),


   
]

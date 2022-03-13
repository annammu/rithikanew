from django.urls import path
from . import views
urlpatterns=[
    path('cartdetails',views.cartdetails,name='cartdetails'),
    path('add/<int:product_id>/',views.addcart,name="addcart"),
    path('dec/<int:product_id>/', views.mincart, name="dec"),
    path('remove/<int:product_id>/', views.cartdelete, name="remove"),

]


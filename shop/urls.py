from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    # path('details',views.prodetails,name='details'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetails, name='details'),
    path('search',views.searching,name='search')
]

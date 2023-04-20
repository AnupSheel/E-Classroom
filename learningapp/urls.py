from django.urls import path,include
from learningapp import views

urlpatterns = [
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('addproduct',views.addproduct),
    path('dash',views.dashboard),
    path('statfilter/<sv>',views.statfilter),
    path('cat1filter/<cv1>',views.cat1filter),
    path('cat2filter/<cv2>',views.cat2filter),
    path('timefilter/<tf>',views.timefilter),
    path('pricefilter/<pf>',views.pricefilter),
    path('sort/<s>',views.sortfilter),
    path('multifilter',views.multifilter),
   
]
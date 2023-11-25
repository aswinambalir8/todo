from . import views
from django.urls import path

urlpatterns = [

    path('',views.main,name='main'),
    path('details',views.details,name='details'),
    path('delete/<int:todoid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('genlist/',views.todolist.as_view(),name='genlist'),
    path('gendetail/<int:pk>/',views.tododetail.as_view(),name='gendetail'),
    path('genupdate/<int:pk>/',views.todoupdate.as_view(),name='genupdate'),
    path('gendelete/<int:pk>/',views.tododelete.as_view(),name='gendelete'),
]

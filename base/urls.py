from django.urls import path



from . import views

urlpatterns=[
    path('', views.index),
    path('add_task/', views.add_task),
    path('delete_task/<int:todo_item_id>/', views.delete_task),
    path('clear/', views.clear)
]
from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_fruit/', views.FruitFormView.as_view(), name='create-fruit'),
    path('<int:fruit_pk>/', include(
        [
            path('details/', views.details_fruit, name='details-fruit'),
            path('edit/', views.edit_fruit, name='edit-fruit'),
            path('delete/', views.delete_fruit, name='delete-fruit'),
        ]
    )),
    path('create_category/', views.create_category, name='create-category')
]

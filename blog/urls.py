
from django.urls import path
from . import views

urlpatterns =[

	path('blog/', views.index, name="index" ),
        path('blog/<int:pk>/', views.post_detail, name="post_detail"),
        path('blog/new/', views.post_new, name= "post_new"),
        path('blog/<int:pk>/edit/', views.edit_post, name="edit_post"),
]
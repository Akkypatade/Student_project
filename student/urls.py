from django.urls import path
from . import views

urlpatterns = [
    path('',views.show),
    path('stud',views.stud),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.update),
    path('update/<int:id>',views.destroy),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('submit_score/', views.submit_score, name='submit_score'),
    path('score_board/', views.score_board, name='score_board'),
    # path('base/', views.base, name='base'),
    
]

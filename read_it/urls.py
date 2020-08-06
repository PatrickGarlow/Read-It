from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'read-it-home'),
    path('upload/', views.upload, name = 'read-it-upload'),
    path('quiz/', views.quiz, name = 'read-it-quiz'),
    path('quiz_response/<new_genre_profile>', views.quiz_response, name='read-it-quiz-response'),
    path('liked/<book_title>', views.book_liked, name='read-it-book-liked'),
    path('book/<book_title>', views.book_detail, name='read-it-detail'),
    path('recommend_book/', views.recommend_book, name='read-it-recommend')
]
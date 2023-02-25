from django.urls import path

from movie_app import views
from movie_app.views import *
urlpatterns = [
    path("api/v1/directors", views.director_list),
    path("api/v1/directors/<int:id>/", views.get_director),
    path("api/v1/movies/", views.movie_list),
    path("api/v1/movies/<int:id>/", views.get_movie),
    path("api/v1/reviews/", views.review_list),
    path("api/v1/reviews/<int:id>/", views.get_review),
    path("api/v1/movies/reviews/", views.movie_list),

]
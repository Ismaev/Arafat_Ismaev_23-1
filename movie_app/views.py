from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serialiezers import *
from movie_app.models import *
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def director_list(request):
    if request.method == "GET":
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True)
        return Response(data.data)

@api_view(["GET"])
def get_director(request, id):
    director = get_object_or_404(Director, id=id)
    serializer = DirectorSerializer(director)
    return Response(serializer.data)

@api_view(["GET"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True)
        return Response(data.data)

@api_view(["GET"])
def get_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(["GET"])
def review_list(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True)
        return Response(data.data)

@api_view(["GET"])
def get_review(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

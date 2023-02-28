
from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=10, verbose_name='Имя директора')

    @property
    def movie_count(self):
        return self.movie_set.all().count()
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название фильма')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    duration = models.IntegerField(default=0, verbose_name='Длительность')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    @property
    def rating(self):
        total_amount = self.review_set.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.review_set.all():
            sum_ += i.stars
        return sum_ / total_amount


    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=1000, verbose_name='Комментарий')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(max_length=5, default='Звезды')
    def __str__(self):
        return self.text


from django.db import models
from datetime import date
from django.db.models.signals import pre_save
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=155,unique = True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to = "actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug":self.name})

    class Meta:
        verbose_name = "Актер и режиссер"
        verbose_name_plural = "Актеры и режиссеры"



class Genre(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.SlugField(unique = True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Наименование")
    tagline = models.CharField(max_length = 155, default = "")
    description = models.TextField()
    poster = models.ImageField(upload_to = "movies/")
    year= models.PositiveSmallIntegerField(verbose_name = "Год")
    country = models.CharField(max_length = 100)
    directors = models.ManyToManyField(Actor, verbose_name = "Режиссер", related_name= "film_director")
    actors = models.ManyToManyField(Actor, verbose_name = "Актеры",related_name= "film_actor")
    genres = models.ManyToManyField(Genre, verbose_name = "Жанры")
    world_premieres = models.DateField(default = date.today)
    budjet = models.PositiveIntegerField(default = 0, help_text = "Указывать в долларах")
    fees_in_usa = models.PositiveIntegerField(default = 0, help_text = "Указывать в долларах")
    fees_in_world = models.PositiveIntegerField(default = 0, help_text = "Указывать в долларах")
    category = models.ForeignKey(Category, verbose_name = "Категория", on_delete=models.SET_NULL, null = True)
    slug = models.SlugField(max_length = 155, unique = True, blank = True)
    draft = models.BooleanField(default = False, verbose_name = "Черновик")





    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comment_set.filter(parent__isnull = True)

    def get_absolute_url(self):
        return reverse("detail_movie", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"



class MovieShot(models.Model):
    headers = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = "MovieShots/")
    movie = models.ForeignKey(Movie, verbose_name = "Фильм", on_delete= models.CASCADE)


    def __str__(self):
        return self.headers

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"



class MovieStar(models.Model):
    value = models.SmallIntegerField(default = 0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Звезда фильма"
        verbose_name_plural = "Звезды фильма"


class MovieRating(models.Model):
    ip = models.CharField("Ip adress", max_length = 15)
    star = models.ForeignKey(MovieStar, verbose_name = "Звезды фильма", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"


    class Meta:
        verbose_name = "Рейтинг фильма"
        verbose_name_plural = "Рейтинги фильма"


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 100)
    text = models.TextField(max_length = 6000)
    parent = models.ForeignKey("self", verbose_name = "Родитель", on_delete = models.SET_NULL, blank = True, null=True)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"







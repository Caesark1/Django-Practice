from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, View
from .models import *
from .forms import *


class MovieGenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).distinct().values("year")


class MovieListView(MovieGenreYear, ListView):
    model = Movie
    template_name = "movie/movie_list.html"
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'movies'
    paginate_by = 3


class MovieDetailView(MovieGenreYear, DetailView):
    template_name = "movie/movie_detail.html"
    queryset = Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentAddForm()
        return context


class CommentAdd(View):
    def post(self, request, pk):
        form = CommentAddForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorDetailView(MovieGenreYear, DetailView):
    model = Actor
    template_name = "movie/actor.html"
    slug_field = "name"


class MovieFilter(MovieGenreYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genres"))
        )
        return queryset


class MovieSearch(MovieGenreYear,ListView):
    # paginate_by = 1

    def get_queryset(self):
        return Movie.objects.filter(title__icontains = self.request.GET.get("search"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search"] = self.request.GET.get("search")
        return context
from django.urls import path
from .views import MovieDetailView, MovieListView, CommentAdd, ActorDetailView, MovieFilter, MovieSearch


urlpatterns = [
    path("", MovieListView.as_view(), name="list_view"),
    path("filter/", MovieFilter.as_view(), name = "filter"),
    path("search/", MovieSearch.as_view(), name = "search"),
    path("<str:slug>/", MovieDetailView.as_view(), name="detail_movie"),
    path("review/<int:pk>/", CommentAdd.as_view(), name = "comment_link"),
    path("actor/<str:slug>/", ActorDetailView.as_view(), name = "actor_detail"),
]

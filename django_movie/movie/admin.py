from django.contrib import admin
from .models import Actor, Category, Comment, Genre, MovieRating,Movie,MovieShot,MovieStar
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label = "Описание" ,widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'






@admin.register(Category)
class MovieCategory(admin.ModelAdmin):
    list_display = ("id", "title", "url",)
    list_display_links = ("title",)


class CommentsInMovie(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ("name", "email", "movie", "parent")

@admin.register(Movie)
class MovieList(admin.ModelAdmin):
    list_display = ("title","category", "year", "draft")
    list_filter = ("title", "year")
    search_fields = ("title",)
    inlines = [CommentsInMovie]
    list_editable = ("draft", )
    save_on_top = True
    form = MovieAdminForm
    actions = ["publish", "unpublish"]


    def unpublish(self,request, queryset):
        row_update = queryset.update(draft = True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
    
    def publish(self,request, queryset):
        row_update = queryset.update(draft = False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ("change", )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ("change", )

@admin.register(Comment)
class MovieComment(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email", "movie", "parent")

@admin.register(Actor)
class ActorMovie(admin.ModelAdmin):
    list_display = ("name", "age", "get_image",)


    def get_image(self,obj):
        return mark_safe(f'<img src = {obj.image.url} width = "50" height = "60"')

    get_image.short_description = "Изображение"

@admin.register(Genre)
class MovieGenre(admin.ModelAdmin):
    list_display = ("title", "url")


@admin.register(MovieRating)
class MovieRationg(admin.ModelAdmin):
    list_display = ("movie", "ip")


@admin.register(MovieShot)
class MovieShots(admin.ModelAdmin):
    list_display = ("headers", "movie", "get_image")

    def get_image(self,obj):
        return mark_safe(f'<img src = {obj.image.url} width = "50" heigth = "60"')

    get_image.short_description = "Изображение"

admin.site.register(MovieStar)

admin.site.site_title = "Caesar"
admin.site.site_header = "Django Movie"
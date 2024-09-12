from ckeditor.fields import RichTextField
from django.contrib import admin

from .models import ScientificTeam, Scientists, Expressions, News, Provensiya, Dictionary, Sentences, Contact, Slider, \
    Text
from ckeditor.widgets import CKEditorWidget

from .utils import search_texts

admin.site.register(ScientificTeam)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'description')


@admin.register(Expressions)
class ExpressionsAdmin(admin.ModelAdmin):
    list_display = ('express',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class SentencesInline(admin.TabularInline):
    model = Sentences
    extra = 1


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya', 'text', 'lemmatized_text')  # Fields to display in the list view
    search_fields = ['text', 'lemmatized_text']  # Fields to be searchable in the admin interface
    list_filter = ('provensiya',)

    def get_search_results(self, request, queryset, search_term):
        # Qidiruv termiga lemmatizatsiya qo'shish
        search_results = search_texts(search_term)
        return search_results, False


class ProvensiyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya')


class DictionaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }
    list_display = ('id', 'lexical', 'provensiya')
    search_fields = ('lexical', 'provensiya__provensiya')
    inlines = [SentencesInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'instagram', 'telegram', 'facebook', 'latitude', 'longitude')
    search_fields = ('phone', 'email', 'instagram', 'telegram', 'facebook')
    list_filter = ('latitude', 'longitude')
    ordering = ('phone',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Adjust fields as needed
    search_fields = ('title',)  # Allows searching by title
    list_filter = ('title',)  # Allows filtering by title

  # Add filters on the sidebar for the list view

admin.site.register(Text, TextAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Provensiya, ProvensiyaAdmin)
admin.site.register(Dictionary, DictionaryAdmin)

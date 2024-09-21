from django.urls import path


from .views import scientific_team_list, scientific_team_detail, scientists_list, expressions_list, news_list, \
    dictionary_list, provensiya_list, \
    news_detail, contact_list_create, contact_detail, slider_list, TextListView, LemmatizeWordAPIView, WordRootAPIView

urlpatterns = [
    path('scientific-team/', scientific_team_list),
    path('scientific-team/<int:pk>', scientific_team_detail),
    path('scientists/', scientists_list),
    path('expressions/', expressions_list),
    path('news/', news_list),
    path('news/<int:pk>/', news_detail),
    path('provensiya/', provensiya_list),
    path('dictionary/', dictionary_list,),
    path('contacts/', contact_list_create),
    path('contacts/<int:pk>/', contact_detail),
    path('sliders/', slider_list),
    path('text/', TextListView.as_view()),
    path('api/word-root/', WordRootAPIView.as_view(), name='word-root-api'),

]


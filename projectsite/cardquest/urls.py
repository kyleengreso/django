from django.urls import path
from cardquest.views import HomePageView, TrainerList, TrainerCreateView, TrainerUpdateView, TrainerDeleteView
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('pokemon_card', views.PokemonCardList.as_view(), name='pokemon-card'),
    path('collection', views.CollectionList.as_view(), name='collection'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', TrainerDeleteView.as_view(), name='trainer-delete'),
]
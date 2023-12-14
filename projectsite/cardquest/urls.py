from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('pokemon_card', views.PokemonCardListView.as_view(), name='pokemon-card'),
    path('collection', views.CollectionList.as_view(), name='collection'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete')
]
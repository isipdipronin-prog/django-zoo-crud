from django.urls import path
from .views import (
    index_view,
    AnimalListView, AnimalDetailView, AnimalCreateView, AnimalUpdateView, AnimalDeleteView,
    EnclosureListView, EnclosureDetailView, EnclosureCreateView, EnclosureUpdateView, EnclosureDeleteView,
    KeeperListView, KeeperDetailView, KeeperCreateView, KeeperUpdateView, KeeperDeleteView,
    VetCardListView, VetCardDetailView, VetCardCreateView, VetCardUpdateView, VetCardDeleteView,
    FeedingScheduleListView, FeedingScheduleDetailView, FeedingScheduleCreateView, FeedingScheduleUpdateView, FeedingScheduleDeleteView,
)

urlpatterns = [
    path('', index_view, name='index'),

    # Животные
    path('animals/', AnimalListView.as_view(), name='animal_list'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('animals/create/', AnimalCreateView.as_view(), name='animal_create'),
    path('animals/<int:pk>/update/', AnimalUpdateView.as_view(), name='animal_update'),
    path('animals/<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal_delete'),

    # Вольеры
    path('enclosures/', EnclosureListView.as_view(), name='enclosure_list'),
    path('enclosures/<int:pk>/', EnclosureDetailView.as_view(), name='enclosure_detail'),
    path('enclosures/create/', EnclosureCreateView.as_view(), name='enclosure_create'),
    path('enclosures/<int:pk>/update/', EnclosureUpdateView.as_view(), name='enclosure_update'),
    path('enclosures/<int:pk>/delete/', EnclosureDeleteView.as_view(), name='enclosure_delete'),

    # Сотрудники
    path('keepers/', KeeperListView.as_view(), name='keeper_list'),
    path('keepers/<int:pk>/', KeeperDetailView.as_view(), name='keeper_detail'),
    path('keepers/create/', KeeperCreateView.as_view(), name='keeper_create'),
    path('keepers/<int:pk>/update/', KeeperUpdateView.as_view(), name='keeper_update'),
    path('keepers/<int:pk>/delete/', KeeperDeleteView.as_view(), name='keeper_delete'),

    # Ветеринарные карты
    path('vetcards/', VetCardListView.as_view(), name='vetcard_list'),
    path('vetcards/<int:pk>/', VetCardDetailView.as_view(), name='vetcard_detail'),
    path('vetcards/create/', VetCardCreateView.as_view(), name='vetcard_create'),
    path('vetcards/<int:pk>/update/', VetCardUpdateView.as_view(), name='vetcard_update'),
    path('vetcards/<int:pk>/delete/', VetCardDeleteView.as_view(), name='vetcard_delete'),

    # Расписание кормлений
    path('feedings/', FeedingScheduleListView.as_view(), name='feeding_list'),
    path('feedings/<int:pk>/', FeedingScheduleDetailView.as_view(), name='feeding_detail'),
    path('feedings/create/', FeedingScheduleCreateView.as_view(), name='feeding_create'),
    path('feedings/<int:pk>/update/', FeedingScheduleUpdateView.as_view(), name='feeding_update'),
    path('feedings/<int:pk>/delete/', FeedingScheduleDeleteView.as_view(), name='feeding_delete'),
]
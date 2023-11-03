from django.urls import path

from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import HabitsCreateView, HabitsListView, HabitsRetrieveView, HabitsUpdateView, \
    HabitsDestroyView

app_name = AtomicHabitsConfig.name

urlpatterns = [
    path('create/', HabitsCreateView.as_view(), name='create'),
    path('list/', HabitsListView.as_view(), name='list'),
    path('<int:pk>', HabitsRetrieveView.as_view(), name='retrieve'),
    path('update/<int:pk>', HabitsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', HabitsDestroyView.as_view(), name='delete'),
]

from django.urls import path
from .views import (
    RandomCharacterView,
    RandomQuoteView,
    RandomSettingView,
    RandomPlotView,
)

urlpatterns = [
    path('api/characters/random/', RandomCharacterView.as_view(), name='random-character'),
    path('api/characters/<int:pk>/', RandomCharacterView.as_view(), name='update-character'),  # For PUT
    path('api/quotes/random/', RandomQuoteView.as_view(), name='random-quote'),
    path('api/quotes/<int:pk>/', RandomQuoteView.as_view(), name='update-quote'),  # For PUT
    path('api/settings/random/', RandomSettingView.as_view(), name='random-setting'),
    path('api/settings/<int:pk>/', RandomSettingView.as_view(), name='update-setting'),  # For PUT
    path('api/plots/random/', RandomPlotView.as_view(), name='random-plot'),
    path('api/plots/', RandomPlotView.as_view(), name='create-plot'),  # For POST (optional use case)
]


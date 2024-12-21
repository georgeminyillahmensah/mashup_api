from django.urls import path
from .views import (
    CharacterView, 
    QuoteView, 
    SettingView, 
    RandomPlotView
)


urlpatterns = [
    # Character Endpoints
    path('characters/', CharacterView.as_view()),  # List and Create Characters
    path('characters/<int:pk>/', CharacterView.as_view()),  # Retrieve and Update a specific Character

    # Quote Endpoints
    path('quotes/', QuoteView.as_view()),  # List and Create Quotes
    path('quotes/<int:pk>/', QuoteView.as_view()),  # Retrieve and Update a specific Quote

    # Setting Endpoints
    path('settings/', SettingView.as_view()),  # List and Create Settings
    path('settings/<int:pk>/', SettingView.as_view()),  # Retrieve and Update a specific Setting

    # Plot Generator Endpoint
    path('plots/', RandomPlotView.as_view()),  # Generate a Random Plot
]

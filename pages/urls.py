from django.urls import path
from . import views
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
], 'pages'); # This is a tuple with the URL patterns and the app name
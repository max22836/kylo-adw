from django.urls import path
from apps.catalog import views
from apps.main.views import PageView, ContactsView

urlpatterns = [
    path('<str:slug>/', PageView.as_view(), name='page'),
    path('<str:slug>/', ContactsView.as_view, name='contacts'),
]

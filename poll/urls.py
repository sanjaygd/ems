from django.urls import path
from .views import *

urlpatterns = [
    path('add/',PollView.as_view(), name='poll_add'),
    path('<int:id>/edit', PollView.as_view(), name='poll_edit'),
    path('<int:id>/delete', PollView.as_view(), name='poll_delete'),
    path('list/', index, name='poll_list'),
    path('<int:id>/details/', details, name='poll_details'),
    path('<int:id>/', poll, name='poll_vote'),
    
    
]

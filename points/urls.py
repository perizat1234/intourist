from django.urls import path
from .views import points,create,point,edit_place,delete_place,FeedBackView,FeedBackDetailView

urlpatterns = [
    path('', points, name= 'points-list'),
    path('create/', create, name='create-point'),
    path ('<int:id>/', point, name = 'point'),
    path ('<int:id>/edit/',edit_place, name = 'edit-place'),
    path ('<int:id>/delete/',delete_place, name = 'delete-place'),
    path ('feedback/', FeedBackView.as_view(), name= 'feedback' ),
    path ('feedback/<int:pk>', FeedBackDetailView.as_view(), name='feedback-detail')

]
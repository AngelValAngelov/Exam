from django.urls import path


from karuchka.main.views.generic import HomeView
from karuchka.main.views.vehicles import CreateVehicleView, EditVehicleView, DeleteVehicleView, ListVehiclesView, \
    VehicleDetailsView, LikeVehicleView, DislikeVehicleView, CommentVehicleView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', ListVehiclesView.as_view(), name='dashboard'),

    path('details/<int:pk>', VehicleDetailsView.as_view(), name='vehicle details'),
    path('vehicle/add/', CreateVehicleView.as_view(), name='create vehicle'),
    path('vehicle/edit/<int:pk>/', EditVehicleView.as_view(), name='edit vehicle'),
    path('vehicle/delete/<int:pk>/', DeleteVehicleView.as_view(), name='delete vehicle'),

    path('like/<int:pk>/', LikeVehicleView.as_view(), name='like vehicle'),
    path('dislike/<int:pk>/', DislikeVehicleView.as_view(), name='dislike vehicle'),

    path('comment/<int:pk>', CommentVehicleView.as_view(), name='comment vehicle'),



]

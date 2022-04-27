from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from karuchka.accounts.views import UserLoginView, UserRegisterView, ChangeUserPasswordView, \
    EditProfileView, DeleteProfileView, logout_user, ProfileDetailsView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout_user, name='log out user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/', DeleteProfileView.as_view(), name='delete profile'),

]
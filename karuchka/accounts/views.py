from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView

from karuchka.accounts.forms import CreateProfileForm, EditProfileForm, LoginForm, ProfileForm
from karuchka.accounts.models import Profile
from karuchka.common.view_mixins import RedirectToDashboard
from karuchka.main.models import Vehicle, Like


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')
    form_class = LoginForm

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user



def logout_user(request):
    logout(request)
    return redirect('index')


class DeleteProfileView(DeleteView):
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'accounts/profile_details.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.picture = form.cleaned_data['picture']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes_count = Like.objects.filter(vehicle__user_id=self.request.user.id).count()

        vehicles = list(Vehicle.objects.filter(user_id=self.object.user_id))
        total_vehicle_count = len(vehicles)
        context['vehicles'] = Vehicle.objects.filter(user_id=self.request.user.id)
        context['profile'] = self.object

        context.update({
            'total_likes_count': total_likes_count,
            'total_vehicle_images_count': total_vehicle_count,
            'is_owner': self.object.user_id == self.request.user.id,

        })

        return context



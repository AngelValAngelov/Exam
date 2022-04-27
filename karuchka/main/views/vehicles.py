import profile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import CreateView

from karuchka.accounts.forms import CommentForm
from karuchka.common.helpers import BootstrapFormMixin, PostOnlyView
from karuchka.main.forms import CreateVehicleForm, EditVehicleForm, DeleteVehicleForm
from karuchka.main.models import Vehicle, Like, Dislike, Comment


class CreateVehicleView(views.CreateView):
    model = Vehicle
    template_name = 'vehicle_create.html'
    form_class = CreateVehicleForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


# class CreateVehicleView(LoginRequiredMixin, BootstrapFormMixin, views.CreateView):
#     form_class = CreateVehicleForm
#     success_url = reverse_lazy('create vehicle')
#     template_name = 'vehicle_create.html'
#
#     # def form_valid(self, form):
#     #     vehicle = form.save(commit=False)
#     #     vehicle.user = self.request.user
#     #     vehicle.save()
#     #     return super().form_valid(form)


class EditVehicleView(views.UpdateView):
    model = Vehicle
    template_name = 'vehicle_edit.html'
    form_class = EditVehicleForm
    success_url = reverse_lazy('dashboard')


class DeleteVehicleView(views.DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    form_class = DeleteVehicleForm
    success_url = reverse_lazy('dashboard')

    #
    # def get_success_url(self):
    #     return reverse_lazy('delete vehicle', kwargs={'pk': self.object.id})
    #
    # fields = ('photo', 'tagged_vehicle', 'description')
    #
    # def get_object(self, queryset=None):
    #     return self.request.user


class VehicleDetailsView(views.DetailView):
    model = Vehicle
    template_name = 'vehicle_details.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = context['vehicle']

        vehicle.likes_count = vehicle.like_set.count()
        vehicle.dislikes_count = vehicle.dislike_set.count()
        is_owner = vehicle.user == self.request.user

        is_liked_by_user = vehicle.like_set.filter(user_id=self.request.user.id) \
            .exists()

        is_disliked_by_user = vehicle.dislike_set.filter(user_id=self.request.user.id) \
            .exists()



        context['comment_form'] = CommentForm(
            initial={
                'pet_pk': self.object.id,
            }
        )
        context['comments'] = vehicle.comment_set.all()

        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user
        context['is_disliked'] = is_disliked_by_user


        return context


class ListVehiclesView(views.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'vehicles'
    model = Vehicle


class LikeVehicleView(LoginRequiredMixin, views.View):

    def get(self, request, *args, **kwargs):
        print(self.kwargs['pk'])
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = vehicle.like_set.filter(user_id=self.request.user.id) \
            .first()

        if like_object_by_user:

            like_object_by_user.delete()

        else:
            like = Like(
                vehicle=vehicle,
                user=self.request.user,
            )

            like.save()
        return redirect('vehicle details', vehicle.id)


class DislikeVehicleView(LoginRequiredMixin, views.View):
    def get(self, request, *args, **kwargs):
        print(self.kwargs['pk'])
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        dislike_object_by_user = vehicle.dislike_set.filter(user_id=self.request.user.id) \
            .first()

        if dislike_object_by_user:

            dislike_object_by_user.delete()

        else:
            dislike = Dislike(
                vehicle=vehicle,
                user=self.request.user,
            )

            dislike.save()
        return redirect('vehicle details', vehicle.id)


class CommentVehicleView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            vehicle=vehicle,
            user=self.request.user,
        )
        comment.save()

        return redirect('vehicle details', vehicle.id)

    def form_invalid(self, form):
        pass
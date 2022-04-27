from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin, get_user_model

from karuchka.accounts.models import Profile
# from karuchka.main.forms import CreateVehiclePhotoForm
from karuchka.main.models import  Vehicle, Like
from django.views import generic as views, View


# class VehiclePhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
#     model = VehiclePhoto
#     template_name = 'vehicle_details.html'
#     context_object_name = 'vehicle_photo'
#
#     # def dispatch(self, request, *args, **kwargs):
#     #     response = super().dispatch(request, *args, **kwargs)
#     #
#     #     viewed_vehicle_photos = request.session.get('last_viewed_vehicle_photo_ids', [])
#     #
#     #     viewed_vehicle_photos.insert(0, self.kwargs['pk'])
#     #     request.session['last_viewed_vehicle_photo_ids'] = viewed_vehicle_photos[:4]
#     #
#     #     return response
#
#     def get_queryset(self):
#         return super().get_queryset().prefetch_related('tagged_vehicle')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['is_owner'] = self.object.user == self.request.user
#
#         return context
# class VehiclePhotoDetailsView(views.DetailView):
#     model = Vehicle
#     template_name = 'vehicle_details.html'
#     context_object_name = 'vehicle'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         vehicle = context['vehicle']
#
#         vehicle.likes_count = vehicle.like_set.count()
#         is_owner = vehicle.user == self.request.user
#
#         is_liked_by_user = vehicle.like_set.filter(user_id=self.request.user.id) \
#             .exists()
#         # context['comment_form'] = CommentForm(
#         #     initial={
#         #         'pet_pk': self.object.id,
#         #     }
#         # )
#         # context['comments'] = pet.comment_set.all()
#         context['is_owner'] = is_owner
#         context['is_liked'] = is_liked_by_user
#
#         return context


# class LikePetView(LoginRequiredMixin, View):
#     def post(self, request, *args, **kwargs):
#         vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
#         like_object_by_user = vehicle.like_set.filter(user_id=self.request.user.id) \
#             .first()
#         if like_object_by_user:
#             like_object_by_user.delete()
#         else:
#             like = Like(
#                 vehicle=vehicle,
#                 user=self.request.user,
#             )
#             like.save()
#         return redirect('vehicle photo details', vehicle.id)

    # def like_vehicle_photo(request, pk):
    #
    #     user = request.user
    #     if request.method == 'GET':
    #         vehicle_photo = VehiclePhoto.objects.get(pk=pk)
    #         print(vehicle_photo)
    #         if vehicle_photo.user == request.user:
    #             vehicle_photo.likes -= 1
    #         else:
    #             vehicle_photo.likes += 1
    #         # if not created:
    #         #     if like.value == 'Like':
    #         #         like.value == 'Unlike'
    #         #     else:
    #         #         like.value = 'Like'
    #
    #         # like.save()

    # like_object_by_user = vehicle_photo.objects.all(user=request.user, vehicle_photo=vehicle_photo)
    # if like_object_by_user:
    #     like_object_by_user.delete()
    # else:
    #     vehicle_photo.likes += 1


# vehicle_photo.save()
#
# return redirect('vehicle photo details', pk)


# def dislike_vehicle_photo(request, pk):
#     vehicle_photo = VehiclePhoto.objects.get(pk=pk)
#     vehicle_photo.dislikes += 1
#     vehicle_photo.save()
#
#     return redirect('vehicle photo details', pk)


# def rate_vehicle_photo(request, pk):
#     vehicle_photo = VehiclePhoto.objects.get(pk=pk)
#     vehicle_photo.rate += 1
#
#     vehicle_photo.save()
#
#     return redirect('vehicle photo details', pk)


# class CreateVehiclePhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
#     model = VehiclePhoto
#     template_name = 'photo_create.html'
#     form_class = CreateVehiclePhotoForm
#
#     # fields = ('photo', 'tagged_vehicle', 'description')
#
#     success_url = reverse_lazy('dashboard')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

    # def get_queryset(self):
    #     return super().get_queryset().order_by('likes')


# class EditVehiclePhotoView(views.UpdateView):
#     model = VehiclePhoto
#     template_name = 'photo_edit.html'
#     fields = ('description',)
#
#     # success_url = reverse_lazy('edit vehicle photo')
#
#     def get_success_url(self):
#         return reverse_lazy('vehicle photo details', kwargs={'pk': self.object.id})

# class DeleteVehiclePhotoView(views.DeleteView):
#     template_name = 'vehicle_delete.html'
#     success_url = reverse_lazy('dashboard')
#     fields = ('photo', 'tagged_vehicle', 'description')
#
#     # def get_object(self, queryset=None):
#     #     return self.request.user

import random
from os.path import join

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from karuchka.accounts.models import Profile
from karuchka.main.models import Vehicle
from karuchka.tests.base.tests import KaruchkaTestCase


class ProfileDetailsTest(KaruchkaTestCase):
    def test_getDetails_whenLoggedInUserWithNoPets_shouldGetDetailsWithNoPets(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['vehicles']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithPets_shouldGetDetailsWithPets(self):
        vehicle = Vehicle.objects.create(
            manufacturer='Tesla',
            description='Test vehicle description',
            age=1,
            image='path/to/image.png',
            type=Vehicle.VEHICLE_TYPE,
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([vehicle], list(response.context['vehicles']))

    # def test_postDetails_whenUserLoggedInWithoutImage_shouldChangeImage(self):
    #     path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.webp')
    #
    #     file_name = f'{random.randint(1, 10000)}-test_image.webp'
    #     file = SimpleUploadedFile(
    #         name=file_name,
    #         content=open(path_to_image, 'rb').read(),
    #         content_type='image/jpeg')
    #
    #     self.client.force_login(self.user)
    #
    #     response = self.client.post(reverse('profile details'), data={
    #         'profile_image': file,
    #     })
    #
    #     self.assertEqual(302, response.status_code)
    #
    #     profile = Profile.objects.get(pk=self.user.id)
    #     self.assertTrue(str(profile.profile_image).endswith(file_name))
    #
    # def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
    #     path_to_image = 'path/to/image.png'
    #     profile = Profile.objects.get(pk=self.user.id)
    #     profile.profile_image = path_to_image + 'old'
    #     profile.save()
    #
    #     self.client.force_login(self.user)
    #
    #     response = self.client.post(reverse('profile details'), data={
    #         'profile_image': path_to_image,
    #     })
    #
    #     self.assertEqual(302, response.status_code)
    #
    #     profile = Profile.objects.get(pk=self.user.id)
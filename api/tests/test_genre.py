from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from api.models import Genre
from django.urls import reverse
from rest_framework import status

User = get_user_model()

class GenreTest(APITestCase):
    fixtures = ['genres']

    def setUp(self):
        self.staffuser = User.objects.create_superuser(is_staff=True,phone_number='+998901234567', password='testpass')
        self.client.force_authenticate(user=self.staffuser)
        self.category1 = Genre.objects.first()
    def test_genre_list(self):
        url = reverse("genre-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_genre_detail(self):
        url = reverse("genre-detail",args=[self.category1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_genre_update(self):
        url = reverse("genre-detail",args=[self.category1.id])
        data = {"name":"historical"}
        response = self.client.put(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_genre_create(self):
        url = reverse("genre-list")
        data={"name":"test_genre"}
        response = self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    def test_delete(self):
        url = reverse('genre-detail', args=[self.category1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
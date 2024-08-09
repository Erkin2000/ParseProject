from rest_framework.test import APITestCase
from rest_framework import status
from .models import Data
from .serializers import DataSerializer, CreateSerializer
from django.urls import reverse


class GetFromUrlTests(APITestCase):

    def test_get_from_url(self):
        url = reverse('https://newsapi.org/v2/everything?q=tesla&from=2024-07-08&sortBy=publishedAt&apiKey=cefee91e87f34a25bdf48c668c38194e')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        if response.data:
            self.assertIn('author', response.data[0])
            self.assertIn('title', response.data[0])


class GetAllTests(APITestCase):

    def setUp(self):
        self.data_instance = Data.objects.create(
            author="Author",
            title="Title",
            description="Description",
            url="http://example.com",
            publishedAt="2024-08-08T00:00:00Z",
            content="Content"
        )

    def test_get_all(self):
        url = reverse('get-all')  # Adjust the URL name if needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)


class GetByIdTests(APITestCase):

    def setUp(self):
        self.data_instance = Data.objects.create(
            author="Author",
            title="Title",
            description="Description",
            url="http://example.com",
            publishedAt="2024-08-08T00:00:00Z",
            content="Content"
        )

    def test_get_by_id(self):
        url = reverse('get-by-id', kwargs={'pk': self.data_instance.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.data_instance.pk)

    def test_get_by_id_not_found(self):
        url = reverse('get-by-id', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateDataTests(APITestCase):

    def test_create_data(self):
        url = reverse('create-data')
        data = {
            'author': "New Author",
            'title': "New Title",
            'description': "New Description",
            'url': "http://example.com/new",
            'publishedAt': "2024-08-08T00:00:00Z",
            'content': "New Content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Title")

    def test_create_data_invalid(self):
        url = reverse('create-data')
        data = {
            'author': "",  # Assuming title is required and others are not provided
            'title': "New Title",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateIdTests(APITestCase):

    def setUp(self):
        self.data_instance = Data.objects.create(
            author="Author",
            title="Title",
            description="Description",
            url="http://example.com",
            publishedAt="2024-08-08T00:00:00Z",
            content="Content"
        )

    def test_update_id(self):
        url = reverse('update-id', kwargs={'pk': self.data_instance.pk})
        data = {
            'author': "Updated Author",
            'title': "Updated Title",
            'description': "Updated Description",
            'url': "http://example.com/updated",
            'publishedAt': "2024-08-08T00:00:00Z",
            'content': "Updated Content"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_update_id_not_found(self):
        url = reverse('update-id', kwargs={'pk': 9999})
        data = {
            'author': "Updated Author"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteIdTests(APITestCase):

    def setUp(self):
        self.data_instance = Data.objects.create(
            author="Author",
            title="Title",
            description="Description",
            url="http://example.com",
            publishedAt="2024-08-08T00:00:00Z",
            content="Content"
        )

    def test_delete_id(self):
        url = reverse('delete-id', kwargs={'pk': self.data_instance.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Data.objects.filter(pk=self.data_instance.pk).exists())

    def test_delete_id_not_found(self):
        url = reverse('delete-id', kwargs={'pk': 9999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
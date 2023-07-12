from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Weather
from .helper import api


class ApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_response(self):
        lat = 33.441792
        lon = -94.037689
        typ = "minute"

        mock_api_response = {
            'temperature': 25,
            'humidity': 80,
        }

        weather = Weather.objects.create(
            latitude=lat, longitude=lon, detailing=typ, response=mock_api_response)

        response = self.client.post(reverse('api_response'), {
            'latitude': lat,
            'longitude': lon,
            'type': typ
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_api_response)

        weather.refresh_from_db()
        self.assertLessEqual(
            timezone.now() - weather.date, timedelta(minutes=10))

    def test_api_response_no_data(self):
        lat = 33.441792
        lon = -94.037689
        typ = "current"

        response = self.client.post(reverse('api_response'), {
            'latitude': lat,
            'longitude': lon,
            'type': typ
        })

        self.assertEqual(response.status_code, 200)

        weather = Weather.objects.filter(
            latitude=lat, longitude=lon, detailing=typ).first()
        self.assertIsNotNone(weather)

        self.assertEqual(response.json(), weather.response)

        api_response = api(lat, lon, typ)
        self.assertEqual(response.json(), api_response.json())

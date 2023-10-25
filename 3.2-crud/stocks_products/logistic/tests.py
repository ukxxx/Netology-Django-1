from unittest import TestCase
from rest_framework.test import APIClient


class Test(TestCase):
    def test_main(self):
        client = APIClient()
        url = "/api/v1/test/"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

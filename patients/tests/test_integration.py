from rest_framework.test import APITestCase
from rest_framework import status

class PatientAPITest(APITestCase):
    def test_get_patients(self):
        response = self.client.get('/fhir/Patient/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
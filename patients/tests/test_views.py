from rest_framework.test import APITestCase
from rest_framework import status
from patients.models import Patient

class PatientViewTests(APITestCase):

    def setUp(self):
        # Create a test patient for use in tests
        self.test_patient = Patient.objects.create(
            name="John Doe",
            gender="male",
            birth_date="1990-01-01",
            address="123 Main St",
            email="johndoe@example.com"
        )
        self.patient_url = f"/fhir/Patient/{self.test_patient.id}/"

    def test_get_patient_list(self):
        # Test GET request to retrieve patient list
        response = self.client.get("/fhir/Patient/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "John Doe")

    def test_get_patient_detail(self):
        # Test GET request to retrieve specific patient details
        response = self.client.get(self.patient_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Doe")
        self.assertEqual(response.data["email"], "johndoe@example.com")

    def test_create_patient(self):
        # Test POST request to create a new patient
        data = {
            "name": "Jane Doe",
            "gender": "female",
            "birth_date": "1985-05-05",
            "address": "456 Elm St",
            "email": "janedoe@example.com"
        }
        response = self.client.post("/fhir/Patient/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Jane Doe")
        self.assertEqual(response.data["email"], "janedoe@example.com")

    def test_update_patient(self):
        # Test PUT request to update an existing patient
        data = {
            "name": "Updated John Doe",
            "gender": "male",
            "birth_date": "1990-01-01",
            "address": "456 Elm St",
            "email": "updatedjohndoe@example.com"
        }
        response = self.client.put(self.patient_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated John Doe")
        self.assertEqual(response.data["email"], "updatedjohndoe@example.com")

    def test_delete_patient(self):
        # Test DELETE request to delete an existing patient
        response = self.client.delete(self.patient_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Patient.objects.filter(id=self.test_patient.id).exists())
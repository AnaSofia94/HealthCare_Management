from rest_framework.test import APITestCase
from rest_framework import status
from patients.models import Patient


class PatientIntegrationTests(APITestCase):

    def setUp(self):
        # Set up initial data for integration tests
        self.test_patient_1 = Patient.objects.create(
            name="John Doe",
            gender="male",
            birth_date="1990-01-01",
            address="123 Main St",
            email="johndoe@example.com"
        )
        self.test_patient_2 = Patient.objects.create(
            name="Jane Smith",
            gender="female",
            birth_date="1985-05-05",
            address="456 Elm St",
            email="janesmith@example.com"
        )

    def test_create_and_get_patient(self):
        # Test the creation of a new patient and retrieval of patient list
        new_patient_data = {
            "name": "Alice Johnson",
            "gender": "female",
            "birth_date": "1995-07-15",
            "address": "789 Maple St",
            "email": "alicejohnson@example.com"
        }
        post_response = self.client.post("/fhir/Patient/", new_patient_data, format="json")
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

        # Verify the patient list includes the new patient
        get_response = self.client.get("/fhir/Patient/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get_response.data), 3)  # There should now be 3 patients
        self.assertTrue(any(patient["email"] == "alicejohnson@example.com" for patient in get_response.data))

    def test_update_and_retrieve_patient(self):
        # Test updating a patient and verifying the updated details
        updated_data = {
            "name": "Updated Jane Smith",
            "gender": "female",
            "birth_date": "1985-05-05",
            "address": "999 Birch St",
            "email": "updatedjanesmith@example.com"
        }
        update_response = self.client.put(f"/fhir/Patient/{self.test_patient_2.id}/", updated_data, format="json")
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        # Verify the updated patient details
        get_response = self.client.get(f"/fhir/Patient/{self.test_patient_2.id}/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["name"], "Updated Jane Smith")
        self.assertEqual(get_response.data["email"], "updatedjanesmith@example.com")

    def test_delete_and_verify_patient(self):
        # Test deleting a patient and verifying they are removed
        delete_response = self.client.delete(f"/fhir/Patient/{self.test_patient_1.id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the patient is no longer in the list
        get_response = self.client.get("/fhir/Patient/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get_response.data), 1)  # Only one patient should remain
        self.assertFalse(any(patient["email"] == "johndoe@example.com" for patient in get_response.data))

    def test_get_non_existent_patient(self):
        # Attempt to retrieve a patient that doesn't exist
        response = self.client.get("/fhir/Patient/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
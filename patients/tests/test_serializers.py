from django.test import TestCase
from patients.serializers import PatientSerializer

class PatientSerializerTest(TestCase):
    def test_valid_patient_data(self):
        data = {
            "name": "John Doe",
            "gender": "male",
            "birth_date": "1990-01-01",
            "address": "123 Main St",
            "email": "johndoe@example.com"
        }
        serializer = PatientSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], "John Doe")

    def test_invalid_patient_data(self):
        data = {
            "name": "",
            "gender": "invalid",  # Invalid gender
            "birth_date": "not-a-date",  # Invalid date format
            "address": "123 Main St",
            "email": "invalid-email"  # Invalid email
        }
        serializer = PatientSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("gender", serializer.errors)
        self.assertIn("birth_date", serializer.errors)
        self.assertIn("email", serializer.errors)
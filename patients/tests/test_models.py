from django.test import TestCase
from patients.models import Patient

class PatientModelTest(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(
            name="Jane Doe",
            gender="female",
            birth_date="1991-01-01",
            address="456 Elm St",
            email="janedoe@example.com"
        )
        self.assertEqual(str(patient), "Jane Doe")
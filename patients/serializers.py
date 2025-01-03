from rest_framework import serializers
from fhir.resources.patient import Patient as FHIRPatient
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate(self, data):
        # Transform Django model data into FHIR-compatible format
        fhir_data = {
            "resourceType": "Patient",
            "id": data.get("id"),
            "name": [{"text": data.get("name")}],
            "gender": data.get("gender"),
            "birthDate": str(data.get("birth_date")),
            "address": [{"text": data.get("address")}],
            "telecom": [{"system": "email", "value": data.get("email")}],
        }

        # Validate using FHIR
        try:
            fhir_patient = FHIRPatient.parse_obj(fhir_data)
            if not fhir_patient:
                raise serializers.ValidationError("FHIR validation failed.")
        except Exception as e:
            raise serializers.ValidationError(f"FHIR validation error: {str(e)}")

        return data
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer


logger = logging.getLogger(__name__)


class PatientList(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetail(APIView):
    def get(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
            return Response({
                "id": patient.id,
                "name": patient.name,
                "gender": patient.gender,
                "birth_date": patient.birth_date,
                "address": patient.address,
                "email": patient.email
            }, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            patient = Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            patient = Patient.objects.get(pk=id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
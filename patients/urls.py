from django.urls import path
from .views import PatientList, PatientDetail

urlpatterns = [
    path('Patient/', PatientList.as_view(), name='patient-list'),
    path('Patient/<int:id>/', PatientDetail.as_view(), name='patient-detail'),  # Note the trailing slash
]
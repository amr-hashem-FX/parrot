from django.urls import path
from http_response.views import HttpResponseMimickerView

urlpatterns = [
    path('view/<int:response_id>/', HttpResponseMimickerView.as_view()),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from http_response.models import HttpResponseMimicker

class HttpResponseMimickerView(APIView):
    
    def get(self, request, response_id=None):
        try:
            http_response = HttpResponseMimicker.objects.get(pk=response_id)
            return Response(data=http_response.json_response, status=http_response.status_code)
        except:
            return Response(data={'details': f"reponse with id {response_id} couldn't be found"}, status=status.HTTP_404_NOT_FOUND)

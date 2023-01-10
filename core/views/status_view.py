from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class StatusView(APIView):
  
   def get(self, request):
       return Response({'result':'server is running and OK'}, status=status.HTTP_200_OK)

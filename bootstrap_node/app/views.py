# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Node

# Create your views here.

class NodeAuthView(APIView):
    def post(self,request):
        rv_node_ip = request.META.get('REMOTE_ADDR',None)
        rv_password = request.data.get('password',None)
        
        try:
            node = Node.objects.get(node_ip=rv_node_ip)
        except Node.DoesNotExist:
            return Response({"detail": "Node IP not registered"}, status=status.HTTP_404_NOT_FOUND)

        if node.node_password != rv_password:
            return Response({"detail": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)

            
        
        
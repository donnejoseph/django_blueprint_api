# from django.shortcuts import render

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """
    API health check endpoint.
    Used by Docker health check and monitoring systems.
    """
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)

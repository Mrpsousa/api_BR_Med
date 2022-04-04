from rest_framework.views import APIView
from app_main.services.services import (return_qoutes_values, 
                                        return_quotes_by_date)
import asyncio
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class BuildGraph(APIView):
    def get(self, request):
        return asyncio.run(return_qoutes_values())

        
class OldQuotes(APIView):
    def get(self, request):
        return return_quotes_by_date(request.data['days'])


class MyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = ['algo', "assim"]
        return Response({'profiles': queryset})
from rest_framework.views import APIView
from app_main.services.services import return_qoutes_values
import asyncio


class BuildGraph(APIView):
    
    def get(self, request):
        return asyncio.run(return_qoutes_values())

        

from rest_framework.views import APIView
from app_main.services.services import (return_qoutes_values, 
                                        return_quotes_by_date)
import asyncio


class BuildGraph(APIView):
    def get(self, request):
        return asyncio.run(return_qoutes_values())

        
class OldQuotes(APIView):
    def get(self, request, **kwargs):
        return return_quotes_by_date(request.data)
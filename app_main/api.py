from rest_framework.views import APIView
from app_main.services.services import return_versus_values
import asyncio
from decouple import config


class BuildGraph(APIView):
    """
             Name            : BaseModel
            :class           : Base class with default fields for other classes
            :create          : junho-2021
            description      : Date information 
    ____________________________________________________________________________________________________
    """
    
    def get(self, request):
        url = config('API_URL')
        return asyncio.run(return_versus_values(url))

        

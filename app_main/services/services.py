from rest_framework import status
from rest_framework.response import Response
import aiohttp
from ..quotes import Quotes


def para_teste(data):
    '''
       Comentario
    '''
    try:
        return Response(data, status=status.HTTP_200_OK)
    except Exception:
        return Response('Error: data format',
                        status=status.HTTP_400_BAD_REQUEST)


# async def api_return():
#     url = 'https://api.vatcomply.com/rates'
#     async with aiohttp.ClientSession() as session:
#         try:
#             async with session.get(url) as resp:
#                 data = await resp.json()
#             return Response(data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def return_versus_values(url: str):
    """
        Name             : NONE
        :class           : Base class with default fields for other classes
        :create          : junho-2021
        description      : Date information 
    ____________________________________________________________________________________________________
    """

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                data = await resp.json()
                values = await Quotes(data).run()
                return Response(values, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.
                            HTTP_500_INTERNAL_SERVER_ERROR)

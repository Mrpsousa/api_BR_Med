from rest_framework import status
from rest_framework.response import Response
import aiohttp
from common.utilities import func_name_with_err
from ..models import Values
from asgiref.sync import sync_to_async

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
             Name            : NONE
            :class           : Base class with default fields for other classes
            :create          : junho-2021
            description      : Date information 
    ____________________________________________________________________________________________________
    """

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                data = await resp.json()
                values = await make_calc(data['rates'])
                return Response(values, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def make_calc(data: dict) -> dict:
    """
             Name            : NONE
            :class           : Base class with default fields for other classes
            :create          : March-2022
            description      : Date information 
    ____________________________________________________________________________________________________
    """

    try:
        values = {'euro_dol': data['EUR'] / data['USD'],
                  'brl_dol': data['BRL'] * (data['EUR'] / data['USD']),
                  'jpy_dol': data['JPY'] * (data['EUR'] / data['USD'])}
        await save_values(values)
        return values
    except Exception as e:
        raise Exception(func_name_with_err(e))


async def save_values(data: dict) -> dict:
    """save_values
             Name            : NONE
            :class           : Base class with default fields for other classes
            :create          : March-2022
            description      : Date information 
    ____________________________________________________________________________________________________
    """

    try:
        
        await sync_to_async(Values.objects.create)(euro_dol=data['euro_dol'],
                              brl_dol=data['brl_dol'], jpy_dol=data['jpy_dol'])
    except Exception as e:
        raise Exception(func_name_with_err(e))

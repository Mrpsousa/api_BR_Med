from rest_framework import status
from rest_framework.response import Response
from ..classes import Quotes, Main
from decouple import config

url = config('API_URL')
quote: Quotes = Quotes()
main: Main = Main(url)


async def return_qoutes_values():
    try:
        await main.run(quote.return_valid_dates())
        return Response(main.quotes_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.
                        HTTP_500_INTERNAL_SERVER_ERROR)


def para_teste(data):
    '''
       Comentario
    '''
    try:
        return Response(data, status=status.HTTP_200_OK)
    except Exception:
        return Response('Error: data format',
                        status=status.HTTP_400_BAD_REQUEST)

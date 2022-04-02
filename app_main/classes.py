from common.utilities import error_handler
from .models import Values
from asgiref.sync import sync_to_async
import calendar
import datetime
from datetime import date
import aiohttp
import numpy as np
from .serializers import QuotesSerializer


class DateValidator():

    def return_valid_dates(self) -> list:
        count = 0
        i = 0
        list_valid_dates: list = []
        try:
            while count < 5:
                day = date.today() - datetime.timedelta(days=i)
                i += 1
                if self.verify_valid_date(day):
                    # day = day.date
                    day = str(day)
                    list_valid_dates.append(day)
                    count += 1
            return np.array(list_valid_dates)
        except Exception as e:
            raise Exception(error_handler(e))

    def verify_valid_date(self, date_: date):
        black_list = ['Sunday', 'Saturday']
        try:
            week_day = calendar.day_name[date_.weekday()]
            if (week_day not in black_list):
                return week_day
            else:
                return False
        except Exception as e:
            raise Exception(error_handler(e))


class Quotes():

    def __init__(self):
        pass

    async def save_values(self, quotes: dict):
        try:
            if QuotesSerializer(quotes):
                await sync_to_async(Values.objects.
                                    update_or_create)(
                                        euro_dol=quotes['euro_dol'],
                                        brl_dol=quotes['brl_dol'],
                                        jpy_dol=quotes['jpy_dol'],
                                        of_date=quotes['of_date'])
        except Exception as e:
            raise Exception(error_handler(e))

    @classmethod
    def get_quotes_by_date(self, date_: str):
        try:
            # if bool(re.match("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
#             date_)):
            quotes = Values.objects.filter(of_date=date_['date'])
            return self.quotes_serializer(quotes)
        except Exception as e:
            raise Exception(error_handler(e))

    def quotes_serializer(self, quotes) -> list:
        quotes_list: list = []
        try:
            for quote in quotes:
                quotes_list.append(QuotesSerializer(quote).data)
            return quotes_list
        except Exception as e:
            raise Exception(error_handler(e))


class Main(DateValidator, Quotes):

    def __init__(self, url):
        self.all_quotes: list = []
        self.quotes_list: list = []
        self.url: str = url

    async def call_api(self, dates: list):
        async with aiohttp.ClientSession() as session:
            try:
                for date_ in dates:
                    url = f'{self.url}{date_}'
                    async with session.get(url) as resp:
                        data = await resp.json()
                        self.all_quotes.append(data)
            except Exception as e:
                raise Exception(error_handler(e))

    async def assemble_values(self) -> list:
        try:
            for quotes in self.all_quotes:
                date_ = quotes['date']
                quotes = quotes['rates']
                dol_base = quotes['EUR'] / quotes['USD']
                values = {'euro_dol': dol_base,
                          'brl_dol': dol_base * quotes['BRL'],
                          'jpy_dol': dol_base * quotes['JPY'],
                          'of_date': date_}

                await self.save_values(values)
                self.quotes_list.append(values)
            return values
        except Exception as e:
            raise Exception(error_handler(e))

    async def return_quotes(self) -> list:
        try:
            return self.quotes_list
        except Exception as e:
            raise Exception(error_handler(e))
    
    async def run(self, dates: list) -> dict:
        await self.call_api(dates)
        await self.assemble_values()
        # await self.return_quotes()


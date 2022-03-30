from common.utilities import error_handler
from .models import Values
from asgiref.sync import sync_to_async


class Quotes():
    """
        Name             : NONE
        :class           : Base class with default fields for other classes
        :create          : March-2022
        description      : Date information 
    ____________________________________________________________________________________________________
    """

    def __init__(self, data):
        try:
            self.euro_dol = data['rates']['EUR'] / data['rates']['USD']
            self.brl_dol = data['rates']['BRL'] * self.euro_dol
            self.jpy_dol = data['rates']['JPY'] * self.euro_dol
        
        except Exception as e:
            raise Exception(error_handler(e))

    async def assemble_values(self) -> dict:
        """
            Name             : NONE
            :class           : Base class with default fields for other classes
            :create          : March-2022
            description      : Date information 
        ____________________________________________________________________________________________________
        """

        try:
            values = {'euro_dol': self.euro_dol,
                      'brl_dol': self.brl_dol,
                      'jpy_dol': self.jpy_dol}

            await self.save_values()
            return values
        except Exception as e:
            raise Exception(error_handler(e))

    async def save_values(self) -> dict:
        """
            Name             : NONE
            :class           : Base class with default fields for other classes
            :create          : March-2022
            description      : Date information 
        ____________________________________________________________________________________________________
        """

        try:
            await sync_to_async(Values.objects.create)(euro_dol=self.euro_dol,
                                                       brl_dol=self.brl_dol,
                                                       jpy_dol=self.jpy_dol)
        except Exception as e:
            raise Exception(error_handler(e))

    async def run(self) -> dict:
        """
            Name             : NONE
            :class           : Base class with default fields for other classes
            :create          : March-2022
            description      : Date information 
        ____________________________________________________________________________________________________
        """
        return await self.assemble_values()

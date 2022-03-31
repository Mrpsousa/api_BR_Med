from django.db import models
from common.base_model import BaseModel


class Values(BaseModel):
   
    """"
             Name            : Values
            :class           : Class Values
            :create          : March-2022
            description      : All values related to the dollar
    ___________________________________________________________________________________________________
    """

    euro_dol = models.FloatField('euro-dolar', default=0.0)
    brl_dol = models.FloatField('real-dolar', default=0.0)
    jpy_dol = models.FloatField('iene-dolar', default=0.0)
    of_date = models.CharField(max_length=16)
    
    class Meta:
        verbose_name_plural = 'Valores'
        verbose_name = 'Valor'



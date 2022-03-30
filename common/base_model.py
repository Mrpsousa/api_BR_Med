from django.db import models


class BaseModel(models.Model):
    """
             Name            : BaseModel
            :class           : Base class with default fields for other classes
            :create          : junho-2021
            description      : Date information 
    ____________________________________________________________________________________________________
    """

    created_at = models.DateTimeField('criado', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado', auto_now=True)

    class Meta:
        abstract = True


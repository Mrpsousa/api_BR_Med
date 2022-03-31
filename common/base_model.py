from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField('criado', auto_now_add=True)

    class Meta:
        abstract = True


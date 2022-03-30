from .api import (BuildGraph)
from django.urls import re_path


# list_actions = {
#     'get': 'list',
#     'post': 'create'
# }


# single_actions = {
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# }


urlpatterns = [
    re_path('values', BuildGraph.as_view(),
            name='valores'),
]

from .api import BuildGraph, OldQuotes, MyView
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
    re_path('old/quotes', OldQuotes.as_view(),
            name='oldquotes'),
    re_path('quotes', BuildGraph.as_view(),
            name='quotes'),
    re_path('view', MyView.as_view(),
            name='view'),
]

# class GetHistoryByDate(APIView):
#     def get(self, request, **kwargs):
#         return history_list_by_date(kwargs.get("date"))

# def history_list_by_date(date_value):
#     if bool(re.match("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",
#             date_value)):

#         general_list = RoundPointHistory.objects.filter(date=date_value)

#         if general_list.exists():
#             old_id = None
#             history_list_dto = []
#             for history in general_list:
#                 if old_id != history.round_id:
#                     history_list = []
#                     round = Round.objects.filter(
#                         id=history.round_id).first()
#                     histories = RoundPointHistory.objects.filter(
#                         round_id=round.id).filter(date=date_value)

#                     for history in histories:
#                         history_list.append(
#                             RoundPointHistorySerializer(history).data)

#                     dto = {'id_round': round.id,
#                            'name_round': round.name,
#                            'points': history_list}
#                     history_list_dto.append(dto)
#                     old_id = history.round_id
#             return Response(history_list_dto, status=status.HTTP_200_OK)
#         else:
#             return Response([], status=status.HTTP_200_OK)

#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
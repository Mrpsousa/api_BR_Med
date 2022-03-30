from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from ..models import Values
from ..serializers import ValuesSerializer
from json import dumps
# from ..services.services import 


class ValuesTest(TestCase):

    client = Client()

    def setUp(self):
        pass


    def test_sucess_get_values(self):
        response = self.client.get(reverse('values'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_fail_get_values(self):
    #     response = self.client.get(reverse('values'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

class ValuesTest(TestCase):

    client = Client()

    def setUp(self):
        pass

    def test_get_values(self):
        response = self.client.get(reverse('values'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_list_one_point(self):
#         response = self.client.get(
#             reverse('point', kwargs={'pk': self.point_novo.pk}))
#         point = Point.objects.get(pk=self.point_novo.pk)
#         serializer = PointSerializer(point)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_invalid_single_point(self):
#         response = self.client.get(
#             reverse('point', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_valid_update_point(self):
#         response = self.client.put(
#             reverse('point', kwargs={'pk': self.point_novo.pk}),
#             data=dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_invalid_update_point(self):
#         response = self.client.put(
#             reverse('point', kwargs={'pk': self.point_novo.pk}),
#             data=dumps(self.invalid_payload),
#             content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_valid_delete_point(self):
#         response = self.client.delete(
#             reverse('point', kwargs={'pk': self.point_novo.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_delete_point(self):
#         response = self.client.delete(
#             reverse('point', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# # ------------------------------------------------------------------------------
#     def test_create_valid_setpoint(self):
#         response = self.client.post(reverse('setpoints'), data=dumps
#                                     (self.valid_array),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_bad_value_setpoint(self):
#         response = self.client.post(reverse('setpoints'), data=dumps
#                                     (self.invalid_array),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code,
#                          status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def test_bad_array_setpoint(self):
#         response = self.client.post(reverse('setpoints'), data=dumps
#                                     (self.invalid_array_format),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code,
#                          status.HTTP_400_BAD_REQUEST)

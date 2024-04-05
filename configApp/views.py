from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from configApp.models import *
from configApp.serializers import DateToDateCountMock
from django.db.models import *


class EmployeeApi(APIView):
    def get(self, request, pk, month, year):
        name = Employee.objects.get(pk=pk)
        customer = Order.objects.filter(employee__id=pk, created__year=year, created__month=month).aggregate(
            costomer=Count('customer', distinct=True))
        product = OrderDetails.objects.filter(order_id__employee__id=pk, order_id__created__year=year,
                                              order_id__created__month=month).aggregate(
            product=Sum('quantity', distinct=True))
        a = [{"full_name": name.full_name}, customer, product]

        data = {
            "data": a,
        }
        return Response(data=data)


class EmployeesApi(APIView):
    def get(self, request, month, year):
        employees = Employee.objects.filter(order__created__year=year, order__created__month=month).annotate(
            customer=Count('order__customer', distinct=True)).values('id', 'full_name', 'customer').annotate(
            product=Sum('order__orderdetails__quantity')
        )

        data = {
            "data": employees
        }
        return Response(data=data)


class CustomerApi(APIView):
    def get(self, request, pk, month, year):
        customer = Customer.objects.get(pk=pk)
        product = Customer.objects.filter(pk=pk, order__created__year=year, order__created__month=month).aggregate(
            quantity=Sum('order__orderdetails__quantity'))
        discount = Customer.objects.filter(pk=pk, order__created__year=year, order__created__month=month).aggregate(
            discount=Sum('order__orderdetails__discount'))
        a = [{"full_name": customer.full_name,"id":customer.pk}, product, discount]
        data = {
            "data": a
        }
        return Response(data=data)

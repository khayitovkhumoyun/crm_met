from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=256)
    birthday = models.DateField()

    def __str__(self):
        return self.full_name


class Employee(models.Model):
    full_name = models.CharField(max_length=256)
    birthday = models.DateField()

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField(max_length=256)
    price = models.CharField(max_length=10)
    price_min = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.full_name


class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.order_id.customer.full_name

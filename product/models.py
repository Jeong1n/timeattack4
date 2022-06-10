from django.db import models
from user.models import user
# Create your models here.

class product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(max_length=256, default='')
    image = models.CharField(max_length=256, default='')
    ex = models.CharField(max_length=256, default='')
    price = models.CharField(max_length=256, default='')
    stock = models.IntegerField(verbose_name="재고")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    class Meta:
        db_table = "Category"

    name = models.CharField(max_length=100)


class OrderStatus(models.Model):
    class Meta:
        db_table = "OrderStatus"

    author = models.ForeignKey('user.user', on_delete=models.CASCADE)
    order = models.CharField(max_length=256, default='')
    payment = models.CharField(max_length=256, default='')
    cancel = models.CharField(max_length=256, default='')
    Delivery = models.CharField(max_length=256, default='')
    completed = models.CharField(max_length=256, default='')

class ProductOrder (models.Model):
    class Meta:
        db_table = "Quantity"

    userorder = models.ForeignKey('UserOrder', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='수량')

class UserOrder(models.Model):
    class Meta:
        db_table = "UserOrder"

    author = models.ForeignKey('user.user', on_delete=models.CASCADE)
    address = models.CharField(max_length=256, default='')
    ordertime = models.CharField(max_length=256, default='')
    totalpay = models.CharField(max_length=256, default='')
    Sale = models.CharField(max_length=256, default='')
    pay = models.CharField(max_length=256, default='')
    boolean = models.CharField(max_length=256, default='')
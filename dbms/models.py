from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length = 50, null = True, blank = True)
    date_of_mnf = models.CharField(max_length = 50, null = True, blank = True)
    date_of_exp = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.product_name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length = 50, null = True, blank = True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.customer_name
    
class Orders(models.Model):
    order_name = models.CharField(max_length = 50, null = True, blank = True)
    order_date = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.order_name
    
class Payment(models.Model):
    Payment_mode = models.CharField(max_length = 50, null = True, blank = True)
    amount = models.IntegerField()

    def __str__(self):
        return self.Payment_mode
    
class Order_details(models.Model):
    order_quantity = models.IntegerField()
    # order_price = models.IntegerField()

    def __str__(self):
        return str(self.order_quantity)





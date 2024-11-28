from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
  """
  Model representing a customer with basic information.
  """
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField(unique=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}   ({self.email})"

class Order(models.Model):
  """
  Model representing an order placed by a customer.
  """
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # One-to-Many relationship
  order_date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"Order #{self.id} placed by {self.customer}"
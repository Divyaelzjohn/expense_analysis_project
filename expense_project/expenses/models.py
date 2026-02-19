from django.db import models

# Create your models here.
class Expense(models.Model):
  date = models.DateField()
  category = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return f"{self.category} - {self.amount}"
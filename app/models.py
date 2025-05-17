from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Status(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
    
class Type(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
                return f"{self.type.title} - {self.title}"

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ['title', 'category']

    def __str__(self):
        return f"{self.category.title} - {self.title}"
    
class CashFlow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cashflows')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, related_name='cashflows')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.created_at} - {self.amount} руб."
    

    def get_absolute_url(self):
        return reverse('cashflow_detail', kwargs={'pk': self.pk})
from django.db import models
from django.contrib.auth.models import User
from categories.models import Category  
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_date']

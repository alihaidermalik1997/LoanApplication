from django.db import models
from user.models import User

class Application(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    due_date = models.DateField()
    amount = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[2][0])
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Application #{self.pk} for {self.user.username}"

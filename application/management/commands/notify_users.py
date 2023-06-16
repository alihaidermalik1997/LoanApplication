from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from application.models import Application

class Command(BaseCommand):
    help = 'Notify users before two days of due date'

    def handle(self, *args, **options):
        today = timezone.now().date()
        two_days_from_today = today + timedelta(days=2)

        applications = Application.objects.filter(due_date=two_days_from_today)

        for application in applications:
            # Implement your notification logic here
            # Send notifications to users or perform any required actions
            self.stdout.write(f'Notifying user {application.user.username} about application #{application.pk}')

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from application.models import Application
from application.serializers import LoanApplicationSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView


class LoanApplicationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        today = timezone.now().date()

        # Check if user has already created a loan application today
        existing_application = Application.objects.filter(user=user, created_date=today)
        if existing_application.exists():
            return Response({'error': 'You have already created a loan application today.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if there is any previous loan application in progress or open
        previous_application = Application.objects.filter(user=user, status__in=['in_progress', 'open'])
        if previous_application.exists():
            return Response({'error': 'You have a previous loan application in progress or open.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanApplicationDetailView(RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = LoanApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return Application.objects.filter(user=user).latest('created_date')

from rest_framework import serializers
from application.models import Application



def validate_loan_amount(value):
    if value % 500 != 0:
        raise serializers.ValidationError('Loan amount should be a multiple of 500.')
    return value


class LoanApplicationSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    comment = serializers.CharField(read_only=True)
    created_date = serializers.DateField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    amount = serializers.IntegerField(validators=[validate_loan_amount])

    class Meta:
        model = Application
        fields = '__all__'


class ManageLoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['comment', 'status']


from rest_framework.serializers import ModelSerializer
from main.models import Shop, Report

class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ShopSerializer(ModelSerializer):
    reports = ReportSerializer(many=True, read_only=True)
    class Meta:
        model = Shop
        fields = ['name', 'reports']
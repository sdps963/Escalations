from rest_framework import serializers

from .models import AlertsDropdown_Table, Customers, Alerts, Dropdown_Table_Associations, Severity_Level, Estimated_Downtime_Cost

class AlertsDropdownTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlertsDropdown_Table
        fields = ('id', 'Dropdown_Type', 'Dropdown_Value')

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class DropdownAssociationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dropdown_Table_Associations
        fields = ('id', 'Site_ID', 'Function_ID', 'Function_Area1_ID', 'Function_Area2_ID')

class SeverityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Severity_Level
        fields =('id', 'Severity_Type')

class EstimatedDowntimeCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimated_Downtime_Cost
        fields =('id', 'Estimated_Dropdown')

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'


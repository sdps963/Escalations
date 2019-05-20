from django.db import models
from datetime import datetime

class AlertsDropdown_Table(models.Model):
    Dropdown_Type=models.CharField(max_length=200)
    Dropdown_Value=models.CharField(max_length=200)
    Created_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)
    Updated_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "List: {}".format(self.Dropdown_Type)


class Dropdown_Table_Associations(models.Model):
    Function_Area2_ID=models.PositiveIntegerField()
    Function_Area1_ID=models.PositiveIntegerField()
    Function_ID=models.PositiveIntegerField()
    Site_ID=models.PositiveIntegerField()
    Created_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)
    Updated_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "List: {}".format(self.Function_Area2_ID)


class Severity_Level(models.Model):
    Severity_Type = models.CharField(max_length=200)
    Created_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)
    Updated_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "List: {}".format(self.Function_Area2_ID)

class Estimated_Downtime_Cost(models.Model):
    Estimated_Dropdown = models.CharField(max_length=200)
    Created_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)
    Updated_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "List: {}".format(self.Function_Area2_ID)

class Customers(models.Model):
    Customer_Name=models.CharField(max_length=200)
    Customer_Email=models.EmailField()
    Customer_PhoneNo=models.CharField(max_length=200)
    Customer_Role=models.CharField(max_length=200)
    Site_ID=models.PositiveIntegerField()
    Function_ID=models.PositiveIntegerField()
    Function_Area1_ID=models.PositiveIntegerField(default=0)
    Function_Area2_ID=models.PositiveIntegerField(default=0)
    Informative_ID=models.IntegerField(default=0)
    Minor_ID = models.IntegerField(default=0)
    Moderate_ID = models.IntegerField(default=0)
    Severe_ID = models.IntegerField(default=0)
    Critical_ID = models.IntegerField(default=0)
    Created_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)
    Updated_Timestamp=models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "List: {}".format(self.Customer_Name)


class Alerts(models.Model):
    Site_ID=models.PositiveIntegerField()
    Function_ID = models.PositiveIntegerField()
    Function_Area1_ID=models.PositiveIntegerField()
    Function_Area2_ID=models.PositiveIntegerField()
    Severity_Level_ID=models.PositiveIntegerField()
    Days_To_Resolve	=models.CharField(max_length=200)
    Alert_Title =models.CharField(max_length=200)
    Estimated_Downtime =models.CharField(max_length=200)
    Estimated_DowntimeCost_ID =models.CharField(max_length=200)
    Imp_Ton =models.CharField(max_length=200)
    Imp_Grade =models.CharField(max_length=200)
    Imp_Recovery =models.CharField(max_length=200)
    Imp_CashFlow =models.CharField(max_length=200)
    Imp_SlowdownHrs =models.CharField(max_length=200)
    Imp_Description =models.CharField(max_length=200)
    Date_of_Occurance =models.CharField(max_length=200)
    Escalation_Description = models.CharField(max_length=500,default='', blank=True)
    Resolution_Description = models.CharField(max_length=500,default='', blank=True)
    Owner_ID = models.PositiveIntegerField(default=0)
    Escalated_On = models.CharField(max_length=200,default='', blank=True)
    Resolved_On = models.CharField(max_length=200,default='', blank=True)
    Location_Coordinates =models.CharField(max_length=200, blank=True)
    Created_Timestamp=models.DateTimeField(default=datetime.now, blank=True)
    Updated_Timestamp=models.DateTimeField(default=datetime.now, blank=True)
    Status= models.CharField(max_length=200)
    Time=models.CharField(max_length=200,default='', blank=True)

    def __str__(self):
        return "List: {}".format(self.Location_Coordinates)

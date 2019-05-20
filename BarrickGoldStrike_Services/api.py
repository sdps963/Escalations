from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
#from django.core.mail import send_mail
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import AlertsDropdownTableSerializer, CustomersSerializer, AlertSerializer, DropdownAssociationsSerializer, SeverityLevelSerializer, EstimatedDowntimeCostSerializer
from .models import AlertsDropdown_Table, Customers, Alerts, Dropdown_Table_Associations, Severity_Level, Estimated_Downtime_Cost


class AlertsDropdownViewSetApi(ModelViewSet):
    queryset = AlertsDropdown_Table.objects.all()
    serializer_class = AlertsDropdownTableSerializer


class DropdownAssociationsViewSetApi(ModelViewSet):
    serializer_class = DropdownAssociationsSerializer

    def get_queryset(self):
        queryset = Dropdown_Table_Associations.objects.all()
        site = self.request.query_params.get('site', None)
        function = self.request.query_params.get('function', None)
        functionArea1 = self.request.query_params.get('functionArea1', None)
        functionArea2 = self.request.query_params.get('functionArea2', None)
        if site is not None:
            queryset = queryset.filter(Site_ID=site)
        if function is not None:
            queryset = queryset.filter(Function_ID=function)
        if functionArea1 is not None:
            queryset = queryset.filter(Function_Area1_ID=functionArea1)
        if functionArea2 is not None:
            queryset = queryset.filter(Function_Area2_ID=functionArea2)
        return queryset

class CustomersViewSetApi(ModelViewSet):
    #queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

    def get_queryset(self):
        queryset = Customers.objects.all()
        function = self.request.query_params.get('function', None)
        site = self.request.query_params.get('site', None)
        functionArea1 = self.request.query_params.get('functionArea1', None)
        functionArea2 = self.request.query_params.get('functionArea2', None)
        minor = self.request.query_params.get('minor', None)
        moderate = self.request.query_params.get('moderate', None)
        severe = self.request.query_params.get('severe', None)
        critical = self.request.query_params.get('critical', None)
        informative = self.request.query_params.get('informative', None)

        if (site == '5'  and function == '9') or (site == '3' and function == '8'):
            if site is not None:
                queryset = queryset.filter(Site_ID=site)
            if function is not None:
                queryset = queryset.filter(Function_ID=function)
            if minor is not None:
                queryset = queryset.filter(Minor_ID=minor)
            elif moderate is not None:
                queryset = queryset.filter(Moderate_ID=moderate)
            elif severe is not None:
                queryset = queryset.filter(Severe_ID=severe)
            elif critical is not None:
                queryset = queryset.filter(Critical_ID=critical)
            elif informative is not None:
                queryset = queryset.filter(Informative_ID=informative)
        elif site != '32' and function != '33' and functionArea1 != '34' and functionArea2 != '35':
            if site is not None:
                queryset = queryset.filter(Q(Site_ID=site) | Q(Site_ID=28))
            #queryset = queryset.filter(Site_ID=28)
            if function is not None:
                queryset = queryset.filter(Q(Function_ID=function) | Q(Function_ID=29))
            #queryset = queryset.filter(Function_ID=29)
            if functionArea1 is not None:
                queryset = queryset.filter(Q(Function_Area1_ID=functionArea1) | Q(Function_Area1_ID=30))
            #queryset = queryset.filter(Function_Area1_ID=30)
            if functionArea2 is not None:
                queryset = queryset.filter(Q(Function_Area2_ID=functionArea2) | Q(Function_Area2_ID=25))
            #queryset = queryset.filter(Function_Area2_ID=25)
            if minor is not None:
                queryset = queryset.filter(Minor_ID=minor)
            elif moderate is not None:
                queryset = queryset.filter(Moderate_ID=moderate)
            elif severe is not None:
                queryset = queryset.filter(Severe_ID=severe)
            elif critical is not None:
                queryset = queryset.filter(Critical_ID=critical)
            elif informative is not None:
                queryset = queryset.filter(Informative_ID=informative)

        return queryset

class SeverityLevelViewSetApi(ModelViewSet):
    queryset = Severity_Level.objects.all()
    serializer_class = SeverityLevelSerializer

class estimatedDowntimeCostViewSetApi(ModelViewSet):
    queryset = Estimated_Downtime_Cost.objects.all()
    serializer_class = EstimatedDowntimeCostSerializer

class AlertViewSetApi(ModelViewSet):
    serializer_class = AlertSerializer

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy', None)
        if orderBy == 'desc':
            queryset = Alerts.objects.order_by('-Updated_Timestamp')
        else:
            queryset = Alerts.objects.order_by('Updated_Timestamp')
        status = self.request.query_params.get('status', None)
        severityID = self.request.query_params.get('severityId', None)
        if status is not None:
            queryset = queryset.filter(Status=status)
        if severityID is not None:
            queryset = queryset.filter(Severity_Level_ID=severityID)
        return queryset

class AlertViewSetCountApi(ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # Where the magic happens!
        response.data=[{'activeAlertCount':self.queryset.filter(Status='Active').count(),
                            'escalatedAlertCount':self.queryset.filter(Status='Escalated').count(),
                            'resolvedAlertCount':self.queryset.filter(Status='Resolved').count(),}];
        return response

class resolveAlertViewSetApi(ModelViewSet):
    #send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER, ['divyachava7@gmail.com'], fail_silently =False)
    subject, from_email, to = 'hello', settings.EMAIL_HOST_USER, 'divyachava7@gmail.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer







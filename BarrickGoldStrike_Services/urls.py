from rest_framework.routers import DefaultRouter
from .api import AlertsDropdownViewSetApi, CustomersViewSetApi, AlertViewSetApi, resolveAlertViewSetApi,AlertViewSetCountApi,DropdownAssociationsViewSetApi, SeverityLevelViewSetApi, estimatedDowntimeCostViewSetApi

router = DefaultRouter()
router.register(r'dropdownList', AlertsDropdownViewSetApi),
router.register(r'customerList', CustomersViewSetApi, base_name='customer_List')
router.register(r'dropdownAssociations', DropdownAssociationsViewSetApi, base_name='dropdownAssociations_List')
router.register(r'severityLevelList', SeverityLevelViewSetApi)
router.register(r'alerts', AlertViewSetApi, base_name='alerts_List')
# router.register(r'sendMail', resolveAlertViewSetApi)
router.register(r'alertCount', AlertViewSetCountApi,base_name='alerts_count')
router.register(r'estimatedDowntimeCostList', estimatedDowntimeCostViewSetApi)
urlpatterns = router.urls

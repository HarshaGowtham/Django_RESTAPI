from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset ) 

#localhost:p/api/
#GET,POST,UPDATE,DELETE
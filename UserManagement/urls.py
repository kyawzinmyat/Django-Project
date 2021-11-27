from django.urls import path
from .views import Register,register

urlpatterns = [
	path("",Register.as_view())
	#path("",register)

]
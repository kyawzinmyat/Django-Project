from django.shortcuts import render,redirect
from django.views import View
from .form import UserForm

# Create your views here.

class Register(View):	
	form = UserForm()
	context={}
	template = 'User/SignUpC.html'
	
	def get(self,request,*args,**kwargs):
		self.context['form']=self.form
		return render(request,self.template,self.context)
	
	def post(self,request,*args,**kwargs):
		form_data = UserForm(request.POST)
		if form_data.is_valid():
			return redirect("/")
		else:
			return render(request,self.template,self.context)
		
	

		

	
		
	
def register(request):
		if request.method == "POST":
			name = request.POST['username']
			print(name)
			return redirect("/")
		return render(request,'User/SignUp.html')
		
		


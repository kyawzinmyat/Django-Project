from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def test_view(request):
  
    return render(request,'Home.html')

def google(request):
    return HttpResponseRedirect("https://www.google.com/webhp?client=ms-android-samsung-rev2&source=android-home&gws_rd=ssl")

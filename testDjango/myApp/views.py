from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'inserts_me': "I am printing from myApp Views"}
    return render(request,'myApp/index.html',context=my_dict)

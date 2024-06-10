from django.shortcuts import render
from django.http import HttpResponse


def curd_rice(request): #argument
    peoples=[
	{'name' : 'kiran' , 'age' : 26},
	{'name' : 'rinil' , 'age' : 23},
	{'name' : 'mahe' , 'age' : 14},
	{'name' : 'harish' , 'age' : 16},
	{'name' : 'vamsi' , 'age' : 25},
    ]
    
    vegetables = ['pumpkin','tomato','potato' ]

    
    return render(request, "hotel/good.html",context = { 'peoples' : peoples,'vegetables' : vegetables}  
                  )
    
    

def briyani(request):
    return HttpResponse("WOW!!!....too tasty")

def bad(request):
    	return render(request , "hotel/bad.html")

def mod(request):
	return render(request , "hotel/mod.html")

def good(request):
    return render(request , "hotel/good.html")





   




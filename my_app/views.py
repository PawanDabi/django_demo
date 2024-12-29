from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the my_app index.")

def template(request):
    # context={
    #     'name':'Pawan Dabi',
    #     'age': 23
    # }
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is the about page.")

def services(request):
    return HttpResponse("This is the services page.")

def contact(request):
    return HttpResponse("This is the contact page.")
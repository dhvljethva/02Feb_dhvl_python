from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    return render(request, 'service.html')
def error_404(request):
    return render(request, '404.html')
def blog(request):
    return render(request, 'blog.html')
def team(request):  
    return render(request, 'team.html')
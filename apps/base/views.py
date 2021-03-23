from django.shortcuts import render


# Dashboard template
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')

from django.shortcuts import render

def home(request):  # 민혁추가함. 
    return render(request, 'layout.html')
from django.shortcuts import render, redirect


def review(request):
    return render(request, 'review/review.html')


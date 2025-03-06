from django.shortcuts import render

def marketplace_listings(request):
    return render(request, 'listings.html')

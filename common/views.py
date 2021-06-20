from django.shortcuts import render

def landing_page(req):
    return render (req, 'templates/landing_page.html')

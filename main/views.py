from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207972',
        'name': 'Nadia Rahmadina Aristawati',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)

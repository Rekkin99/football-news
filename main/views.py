from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406420596',
        'name': 'Farrell Bagoes Rahmantyo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
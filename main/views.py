from django.shortcuts import render
# Create your views here.
def show_main(request):
    context = {
        'name': 'Maulana Afzaal Wibowo',
        'class': 'PBP E',
        'description' : 'Mahasiswa PBP'
    }

    return render(request, "main.html", context)

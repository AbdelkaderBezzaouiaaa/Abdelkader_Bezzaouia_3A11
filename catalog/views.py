from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Bonjour, ceci est le catalogue !")
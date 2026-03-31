from django.http import JsonResponse
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    return redirect("accounts:login")


def health(request):
    return JsonResponse({"health": "ok"})

# Create your views here.

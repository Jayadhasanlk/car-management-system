# Create your views here.

from django.shortcuts import render, redirect
from .models import Car


def funtionname(request):
    data = Car.objects.all()
    return render(request, "show.html", {"keys_forloop": data})


def home(request):
    return render(request, "home.html")


def update_name(request, pk):
    obj = Car.objects.get(pk=pk)

    if request.method == "POST":

        brand = request.POST.get("brand")
        model = request.POST.get("model")
        price = request.POST.get("price")
        year = request.POST.get("year")
        fuel_type = request.POST.get("fuel_type")

        obj.brand = brand
        obj.model = model
        obj.price = price
        obj.year = year
        obj.fuel_type = fuel_type

        if request.FILES.get("image"):
            obj.image = request.FILES.get("image")

        obj.save()

        return redirect("show")

    return render(request, "update.html", {"key": obj})


def add_product(request):

    if request.method == "POST":

        brand = request.POST.get("brand")
        model = request.POST.get("model")
        price = request.POST.get("price")
        year = request.POST.get("year")
        fuel_type = request.POST.get("fuel_type")
        image = request.FILES.get("image")

        Car.objects.create(
            brand=brand,
            model=model,
            price=price,
            year=year,
            fuel_type=fuel_type,
            image=image
        )

        return redirect("show")

    return render(request, "add.html")





def single_car(request, pk):

    car = Car.objects.get(pk=pk)

    return render(request, 'single_car.html', {'car': car})


def delete_name(request, pk):

    obj = Car.objects.get(pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect("show")

    context = {"key": obj}

    return render(request, "delete.html", context)
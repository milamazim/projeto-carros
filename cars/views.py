from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all() # select * from cars
    return render(request, 'cars.html', {'cars':cars})

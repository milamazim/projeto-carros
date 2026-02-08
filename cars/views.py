from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View


class CarsView(View):
    
    def get(self, request):
        cars = Car.objects.all().order_by('model') # select * from cars order by model
        search = request.GET.get('search') # filtro da busca do usuario

        if search:
            cars = Car.objects.filter(model__icontains=search).order_by('model')

        return render(request, 'cars.html', {'cars':cars})


class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm() # form vazio
        return render(request, 'new_car.html', {'new_car_form': new_car_form})   
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES) # recebe os dados que o usuario preencheu

        if new_car_form.is_valid(): # valida o form antes de gravar
            new_car_form.save()
            return redirect('cars_list')
        
        return render(request, 'new_car.html', {'new_car_form': new_car_form})


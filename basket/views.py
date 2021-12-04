from django.http import JsonResponse

from .basket import Basket

from django.shortcuts import get_object_or_404, render

from store.models import Animal


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        animal_id = int(request.POST.get('animalid'))
        animal_qty = int(request.POST.get('animalqty'))
        animal = get_object_or_404(Animal, id=animal_id)
        basket.add(animal=animal, qty=animal_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        animal_id = int(request.POST.get('animalid'))
        basket.delete(animal=animal_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        animal_id = int(request.POST.get('animalid'))
        animal_qty = int(request.POST.get('animalqty'))
        basket.update(animal=animal_id, qty=animal_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


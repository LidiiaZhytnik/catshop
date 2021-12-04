from decimal import Decimal

from django.http import JsonResponse

from store.models import Animal


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket


    def add(self, animal, qty):
        animal_id = str(animal.id)

        if animal_id in self.basket:
            self.basket[animal_id]['qty'] = qty
        else:
            self.basket[animal_id] = {'price': str(animal.price), 'qty': qty}

        self.save()


    def __iter__(self):
        animal_ids = self.basket.keys()
        animals = Animal.animals.filter(id__in=animal_ids)
        basket = self.basket.copy()

        for animal in animals:
            basket[str(animal.id)]['animal'] = animal

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def update(self, animal, qty):
        animal_id = str(animal)
        if animal_id in self.basket:
            self.basket[animal_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, animal):
        animal_id = str(animal)

        if animal_id in self.basket:
            del self.basket[animal_id]
            print(animal_id)
            self.save()

    def save(self):
        self.session.modified = True
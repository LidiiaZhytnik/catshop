from decimal import Decimal

from store.models import Animal


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket


    def add(self, animal, qty):
        animal_id = animal.id
        if animal_id not in self.basket:
            self.basket[animal_id] = {'price': str(animal.price), 'qty':int(qty)}

        self.session.modified = True


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

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
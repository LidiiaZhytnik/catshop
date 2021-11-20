from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Animal


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='cat', slug='cat')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'cat')


class TestAnimalModel(TestCase):
    def setUp(self):
        Category.objects.create(name='cat', slug='cat')
        User.objects.create(username='admin')
        self.data1 = Animal.objects.create(category_id=1, animal_name='Boris', created_by_id=1, fur_pattern='b', fur_color='White',
                                           fur_length='s', slug='boris', price='10', age='9', sex='m', location='ha',
                                           description='bla bla bla', special_needs='no needs', image='cat', is_active=False, )
        self.data2 = Animal.objects.create(category_id=1, animal_name='Moris', created_by_id=1, fur_pattern='b',
                                           fur_color='Grey', fur_length='s', slug='boris',
                                           price='0', age='0.5', sex='m', location='si', description='blah',
                                           special_needs='special needs', image='cat', is_active=False, )

    def test_animals_model_entry(self):
        """
        Test animal model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Animal))
        self.assertEqual(str(data), 'Boris')


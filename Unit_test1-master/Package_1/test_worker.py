from unittest import TestCase
from Package_1.Worker import *
class TestWorker(TestCase):
    def setUp(self):
        self.bob = Worker('Bob', 'Marshal', 1990, 8, 30, '2 Dizengof,Tel Aviv', 'il')
        self.alice = Worker('Alice', 'Smith', 2020, 12, 1, '90 Yigal Alon Tel Aviv', 'il')
        self.philips= Worker('Philips','Shvili',2030,12,1,'27 Laskov Haim, Holon','il')

    def tearDown(self):
        print('TearDown')


    def test_full_name(self):
        self.assertTrue(self.bob.full_name()=='Bob Marshal')
        # self.assertTrue(self.alice.full_name() == 'Alice Smith')
    # def test_age(self):
    #     self.assertTrue(self.bob.age()=='Bob is 30 years old')
    #     self.assertTrue(self.alice.age() == 'Alice is 0 years old')
    #     self.assertTrue(self.philips.age() == 'Philips is -10 years old')

    def test_days_to_birthday(self):
        self.assertIn(self.bob.days_to_birthday()== '7')
        # self.assertTrue(self.bob.birth_day() == 30)




    def test_greet(self):
        pass

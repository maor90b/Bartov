from unittest import TestCase, mock
from Package_1.Worker import Worker
from unittest.mock import patch




class TestWorker33(TestCase):


    def setUp(self):
        print('setup')
        self.moshe= Worker('Moshe','Cohen',2000,2,17,'1 Yigal Alon ,Tel Aviv', 'il')
    def tearDown(self):
        print('teardown')

    @mock.patch(('Package_1.Worker.Worker.full_name'),return_value='maor philips')
    def test_full_name(self,mock_full_name):
        res = self.moshe.full_name()
        self.assertEqual(res,'maor philips')

    def test_age(self):
        pass

    def test_days_to_birthday(self):
        with patch('Package_1.Worker.Worker.days_to_birthday') as mocked_get:
            mocked_get.return_value=20
            self.assertEqual(self.moshe.days_to_birthday(),20)


    def test_greet(self):
        pass

    def test_location(self):
        with patch('Worker.requests.get') as mocked_get:
            mocked_get.return_value.ok = True             #משתנים שכביכול הפונקציה החזירה
            mocked_get.return_value.text = 'success'       #כתוצאה מהTrue מה שחזר זה הסטרינג הזה

            res = self.moshe.location()
            self.assertEqual(res,'success')

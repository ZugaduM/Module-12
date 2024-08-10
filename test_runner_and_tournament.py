import runner_and_tournament as rt  # импортируем python-файл как rt
import unittest  # импортируем модуль unittest для проведения юнит-тестов


class TournamentTest(unittest.TestCase):  # создаем класс TournamentTest наследуемый от класса unittest.TestCase
    @classmethod  # применяем декоратор @classmethod
    def setUpClass(cls):  # объявляем классовый метод setUpClass, выполняется один раз перед всеми тестами
        cls.all_results = {}  # объявляем пустой словарь

    def setUp(self):  # объявляем  метод setUp
        self.Usain = rt.Runner('Usain', 10)  # объявляем бегуна Усэйн
        self.Andrey = rt.Runner('Andrey', 9)  # объявляем бегуна Андрей
        self.Nik = rt.Runner('Nik', 3)  # объявляем бегуна Ник

    def test_start_1(self):  # объявляем тест первого забега
        test_tournament = rt.Tournament(90, self.Usain, self.Nik)
        '''
        объявляем забег с указанием дистанции и участников
        '''
        results = test_tournament.start()  # объявляем переменную results и вносим в нее результат забега
        self.assertTrue(results[len(results)] == 'Nik')  # проверяем является ли Ник последним бегуном
        self.__class__.all_results['Usain, Nik'] = {p: str(n) for p, n in results.items()}
        '''
        сохраняем в классовую переменную результат текущего забега
        '''
        del test_tournament  # удаляем объект test_tournament для исключения ошибок в следующих тестах

    def test_start_2(self):  # объявляем тест второго забега
        test_tournament = rt.Tournament(90, self.Andrey, self.Nik)
        '''
        объявляем забег с указанием дистанции и участников
        '''
        results = test_tournament.start()  # объявляем переменную results и вносим в нее результат забега
        self.assertTrue(results[len(results)] == 'Nik')  # проверяем является ли Ник последним бегуном
        self.__class__.all_results['Andrey, Nik'] = {p: str(n) for p, n in results.items()}
        '''
        сохраняем в классовую переменную результат текущего забега
        '''
        del test_tournament  # удаляем объект test_tournament для исключения ошибок в следующих тестах

    def test_start_3(self):  # объявляем тест второго забега
        test_tournament = rt.Tournament(90, self.Usain, self.Andrey, self.Nik)
        '''
        объявляем забег с указанием дистанции и участников
        '''
        results = test_tournament.start()  # объявляем переменную results и вносим в нее результат забега
        self.assertTrue(results[len(results)] == 'Nik')  # проверяем является ли Ник последним бегуном
        self.__class__.all_results['Usain, Andrey, Nik'] = {p: str(n) for p, n in results.items()}
        '''
        сохраняем в классовую переменную результат текущего забега
        '''
        del test_tournament  # удаляем объект test_tournament для исключения ошибок в следующих тестах

    @classmethod  # применяем декоратор @classmethod
    def tearDownClass(cls):  # объявляем классовый метод setUpClass, выполняется один раз после всех тестов
        for result in cls.all_results.values():  # для каждого результата из списка всех результатов
            print(f'{result}')  # выводим каждый результат по отдельности


if __name__ == '__main__':
    unittest.main()

import logging
import rt_with_exceptions as runner
import unittest


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='[%(levelname)s] - <%(funcName)s>: <%(lineno)s> - <%(message)s>')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_runner = runner.Runner('Jack', -5)
            for _ in range(10):
                test_runner.walk()
            unittest.TestCase.assertEqual(self, test_runner.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError as ve:
            logging.warning(f'Неверная скорость для Runner. {ve}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runners = {'Вася', 'Федя', 'Виктор'}
        try:
            test_runner = runner.Runner(runners)
            for _ in range(10):
                test_runner.run()
            unittest.TestCase.assertEqual(self, test_runner.distance, 100)
        except TypeError as tp:
            logging.warning(f'Неверный тип данных для объекта Runner. {tp}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner_1 = runner.Runner('Harold')
        test_runner_2 = runner.Runner('Henry')
        for _ in range(10):
            test_runner_1.run()
            test_runner_2.walk()
        unittest.TestCase.assertNotEqual(self, test_runner_1.distance, test_runner_2.distance)


if __name__ == '__main__':
    unittest.main()

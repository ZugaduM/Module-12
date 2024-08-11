import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_runner = runner.Runner('Jack')
        for _ in range(10):
            test_runner.walk()
        unittest.TestCase.assertEqual(self, test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_runner = runner.Runner('Fred')
        for _ in range(10):
            test_runner.run()
        unittest.TestCase.assertEqual(self, test_runner.distance, 100)

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


import unittest
import test_runner
import test_runner_and_tournament


suit_tests = unittest.TestSuite()
suit_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
suit_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_and_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit_tests)

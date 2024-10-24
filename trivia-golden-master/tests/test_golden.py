import filecmp
import sys
from random import seed

from trivia.main import run_game


class TestGolden:
    def test_golden(self):
        seed(1)
        with open('current.log', 'w') as sys.stdout:
            run_game()

        assert filecmp.cmp('current.log', 'golden.log', shallow=False)

import pytest
import random

class TestMyTest:
    params = [(3), (5), (12), (18)]

    @pytest.mark.parametrize('param', params)
    def test_go(self, param):
        count = random.randint(0, 20)

        assert count >= param, f"{count} МЕНЬШЕ! -  чем {param}"




import pytest


class TestOne():
    def test_3(self):
        print("test_a")
        return 1 * 0

    def test_4(self):
        print("test_b")
        return 1 / 0


if __name__ == '__main__':
    pytest.main(["-s"])

import pytest


def test_1():
    print("======")
    return 1 * 0


def test_2():
    print("+++++++")
    return 1 / 0


if __name__ == '__main__':
    pytest.main(["-s"])

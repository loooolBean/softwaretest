import pytest


def setup_module(args):
    print("setup_module", args)


def teardown_module(args):
    print("teardown_module", args)


def test_func_a():
    print("------", "test_func_a")


def test_func_b():
    print("-------", "test_func_b")


class TestOne(object):
    TAG = "a"

    def test_1(self):
        print("---------", self.TAG + "test_1")

    def test_2(self):
        print("---------", self.TAG + "test_2")


if __name__ == '__main__':
    pytest.main(["-s", "test_07_jiaju.py"])

import pytest


@pytest.fixture()
def before():
    print("before")


@pytest.fixture()
def login():
    print("login")
    return "user"


@pytest.mark.usefixtures("before")
def test_1():
    print("test_1()")


@pytest.fixture(params=[1, 2, 3])
def init_data(request):
    print("requests参数是", request.param)
    return request.param


def test_data(init_data):
    assert init_data > 2


def test_2(login):
    print("test_02()", login)


if __name__ == '__main__':
    pytest.main(["-s", "test_08_xiushijiaju.py"])

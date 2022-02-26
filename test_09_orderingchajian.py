import pytest


# 标记运行的顺序  正数 负数 0
# 标记了运行数据的，正整数数量越小，运行的优先级越高
# 标记了运行顺序正整数或0>没有标记的
# 0和正整数 > 没有标记 > 负整数
# 在各个阶段 数越小的运行的优先级越高

def test_1():
    print("1")


def test_2():
    print("2")


def test_3():
    print("3")


@pytest.mark.run(order=3)
def test_4():
    print("4")


@pytest.mark.run(order=2)
def test_5():
    print("5")


@pytest.mark.run(order=1)
def test_6():
    print("6")


if __name__ == '__main__':
    pytest.main(["-s", "test_09_orderingchajian.py"])

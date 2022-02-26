# 单元测试 1测试 函数 类 方法 能不能正常的运行完成 2. 测试执行的结果是否符合我们的预期结果 断言
import pytest


def test_a():
    print("test_a")
    return 1 * 0


@pytest.mark.skip(reason="我想跳过")
def test_b():
    print("test_b")
    return 1 / 0


@pytest.mark.xfail(reason=ZeroDivisionError)
def test_c():
    print("test_c")
    return 1 / 0


if __name__ == '__main__':
    pytest.main(["-s", "test_05_demo.py"])

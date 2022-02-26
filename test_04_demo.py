# 单元测试 1测试 函数 类 方法 能不能正常的运行完成 2. 测试执行的结果是否符合我们的预期结果 断言
import pytest


def test_a():
    print("test_a")
    assert 1==1


def test_b():
    print("test_b")
    assert "a" in "hello"


if __name__ == '__main__':
    pytest.main(["-s", "test_04_demo.py"])

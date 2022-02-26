# 单元测试 1测试 函数 类 方法 能不能正常的运行完成 2. 测试执行的结果是否符合我们的预期结果 断言
import pytest


@pytest.mark.parametrize(["a", "b"], [(1, 2), (10, 20), (30, 40), (50, 60), (70, 80), (90, 90)])
def test_a(a, b):
    print("test_a")
    assert a + b > 100


if __name__ == '__main__':
    pytest.main(["-s", "test_06_demo.py"])

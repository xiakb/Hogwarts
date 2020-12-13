import pytest


@pytest.fixture(autouse="true", scope="module")
def my_fixture():

    print("开始计算")
    yield
    print("结束计算")


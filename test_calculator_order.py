import pytest
import yaml
from pythoncode.Calculator import Calculator


def get_data(path):
    with open(path) as file:
        data = file.read()
        result = yaml.safe_load(data)
    return result


class TestCalculator:
    cal = Calculator()

    @pytest.mark.run(order=9)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["add_normal"],
        ids=get_data("./data.yaml")["add_normal_ids"])
    def test_add_normal(self, a, b, result):
        assert result == round(self.cal.add(a, b), 2)

    @pytest.mark.run(order=8)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["add_abnormal"],
        ids=get_data("./data.yaml")["add_abnormal_ids"])
    def test_add_abnormal(self, a, b, result):
        assert result != round(self.cal.add(a, b), 2)

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["sub_normal"],
        ids=get_data("./data.yaml")["sub_normal_ids"])
    def test_sub_normal(self, a, b, result):
        assert result == round(self.cal.sub(a, b), 2)

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["sub_abnormal"],
        ids=get_data("./data.yaml")["sub_abnormal_ids"])
    def test_sub_abnormal(self, a, b, result):
        assert result != round(self.cal.sub(a, b), 2)

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["mul_normal"],
        ids=get_data("./data.yaml")["mul_normal_ids"])
    def test_mul_normal(self, a, b, result):
        assert result == round(self.cal.mul(a, b), 4)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["mul_abnormal"],
        ids=get_data("./data.yaml")["mul_abnormal_ids"])
    def test_mul_abnormal(self, a, b, result):
        assert result != round(self.cal.mul(a, b), 4)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["div_normal"],
        ids=get_data("./data.yaml")["div_normal_ids"])
    def test_div_normal(self, a, b, result):
        assert result == round(self.cal.div(a, b), 4)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(
        "a, b, result",
        get_data("./data.yaml")["div_abnormal"],
        ids=get_data("./data.yaml")["div_abnormal_ids"])
    def test_div_abnormal(self, a, b, result):
        assert result != round(self.cal.div(a, b), 4)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(
        "a, b",
        get_data("./data.yaml")["div_abnormal_denominator"],
        ids=get_data("./data.yaml")["div_abnormal_denominator_ids"])
    def test_div_abnormal_denominator(self, a, b):
        assert self.cal.div(a, b) == 'error'


if __name__ == '__main__':
    pytest.main()

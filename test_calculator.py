import pytest
from pythoncode.Calculator import Calculator


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, result", [
        (1, 2, 3),
        (5.5, 6.6, 12.1),
        (-10, -22, -32),
        (-22.2, -33.3, -55.5),
        (15, -5, 10),
        (17.5, -23.6, -6.1),
        (-33, 22, -11),
        (-23.45, 34.56, 11.11)
    ], ids=[
        'case_add_normal_1',
        'case_add_normal_2',
        'case_add_normal_3',
        'case_add_normal_4',
        'case_add_normal_5',
        'case_add_normal_6',
        'case_add_normal_7',
        'case_add_normal_8'])
    def test_add_normal(self, a, b, result):
        assert result == round(self.cal.add(a, b), 2)

    @pytest.mark.parametrize("a, b, result", [
        (11, 5.5, 16.4),
        (6.6, 20, 26.7),
        (-23, -20.4, 43.4),
        (-7.8, -33, -40),
        (20, -14.4, 34.4),
        (15.5, -44, 28.9),
        (-67, 77.7, 10.71),
        (-34.5, 34, -1)
    ], ids=[
        'case_add_abnormal_1',
        'case_add_abnormal_2',
        'case_add_abnormal_3',
        'case_add_abnormal_4',
        'case_add_abnormal_5',
        'case_add_abnormal_6',
        'case_add_abnormal_7',
        'case_add_abnormal_8'])
    def test_add_abnormal(self, a, b, result):
        assert result != round(self.cal.add(a, b), 2)

    @pytest.mark.parametrize("a, b, result", [
        (1, 2, -1),
        (6.6, 5.5, 1.1),
        (-10, -22, 12),
        (-33.3, -22.2, -11.1),
        (15, -5, 20),
        (17.5, -23.6, 41.1),
        (-33, 22, -55),
        (-23.45, 34.56, -58.01)
    ], ids=[
        'case_sub_normal_1',
        'case_sub_normal_2',
        'case_sub_normal_3',
        'case_sub_normal_4',
        'case_sub_normal_5',
        'case_sub_normal_6',
        'case_sub_normal_7',
        'case_sub_normal_8'])
    def test_sub_normal(self, a, b, result):
        assert result == round(self.cal.sub(a, b), 2)

    @pytest.mark.parametrize("a, b, result", [
        (11, 5.5, 5.51),
        (6.6, 20, -13.39),
        (-23, -20.4, 2.6),
        (-7.8, -33, -25.2),
        (20, -14.4, 34.5),
        (15.5, -44, 59.4),
        (-67, 77.7, 144.71),
        (-34.5, 34, 69)
    ], ids=[
        'case_sub_abnormal_1',
        'case_sub_abnormal_2',
        'case_sub_abnormal_3',
        'case_sub_abnormal_4',
        'case_sub_abnormal_5',
        'case_sub_abnormal_6',
        'case_sub_abnormal_7',
        'case_sub_abnormal_8'])
    def test_sub_abnormal(self, a, b, result):
        assert result != round(self.cal.sub(a, b), 2)

    @pytest.mark.parametrize("a, b, result", [
        (1, 2, 2),
        (6.6, 5.5, 36.3),
        (-10, -22, 220),
        (-33.3, -22.2, 739.26),
        (15, -5, -75),
        (17.5, -23.6, -413),
        (-33, 22, -726),
        (-23.45, 34.56, -810.432)
    ], ids=[
        'case_mul_normal_1',
        'case_mul_normal_2',
        'case_mul_normal_3',
        'case_mul_normal_4',
        'case_mul_normal_5',
        'case_mul_normal_6',
        'case_mul_normal_7',
        'case_mul_normal_8'])
    def test_mul_normal(self, a, b, result):
        assert result == round(self.cal.mul(a, b), 4)

    @pytest.mark.parametrize("a, b, result", [
        (11, 5.5, 60.51),
        (6.6, 20, 131.9),
        (-23, -20.4, 469.1),
        (-7.8, -33, -257.4),
        (20, -14.4, 288),
        (15.5, -44, -682.1),
        (-67, 77.7, -5206),
        (-34.5, 34, -1174)
    ], ids=[
        'case_mul_abnormal_1',
        'case_mul_abnormal_2',
        'case_mul_abnormal_3',
        'case_mul_abnormal_4',
        'case_mul_abnormal_5',
        'case_mul_abnormal_6',
        'case_mul_abnormal_7',
        'case_mul_abnormal_8'])
    def test_mul_abnormal(self, a, b, result):
        assert result != round(self.cal.mul(a, b), 4)

    @pytest.mark.parametrize("a, b, result", [
        (1, 2, 0.5),
        (6.6, 5.5, 1.2),
        (-22, -10, 2.2),
        (-33.3, -22.2, 1.5),
        (15, -5, -3),
        (17.5, -2.5, -7),
        (-33, 22, -1.5),
        (-55.55, 11, -5.05),
    ], ids=[
        'case_div_normal_1',
        'case_div_normal_2',
        'case_div_normal_3',
        'case_div_normal_4',
        'case_div_normal_5',
        'case_div_normal_6',
        'case_div_normal_7',
        'case_div_normal_8'])
    def test_div_normal(self, a, b, result):
        assert result == round(self.cal.div(a, b), 4)

    @pytest.mark.parametrize("a, b, result", [
        (11, 5.5, 2.1),
        (6.6, 20, 0.3),
        (-22, -4.4, 5.1),
        (-7.8, -3, -2.6),
        (22, -5.5, 3.9),
        (15.5, -40, -0.3874),
        (-66, 2.2, -30.0001),
        (-34.34, 34, -1)
    ], ids=[
        'case_div_abnormal_1',
        'case_div_abnormal_2',
        'case_div_abnormal_3',
        'case_div_abnormal_4',
        'case_div_abnormal_5',
        'case_div_abnormal_6',
        'case_div_abnormal_7',
        'case_div_abnormal_8'])
    def test_div_abnormal(self, a, b, result):
        assert result != round(self.cal.div(a, b), 4)

    @pytest.mark.parametrize("a, b", [
        (10, 0),
        (11.11, 0),
        (-22, 0),
        (-78.9, 0)
    ], ids=[
        'case_div_abnormal_denominator_1',
        'case_div_abnormal_denominator_2',
        'case_div_abnormal_denominator_3',
        'case_div_abnormal_denominator_4'])
    def test_div_abnormal_denominator(self, a, b):
        assert self.cal.div(a, b) == 'error'

import pytest

from src.ch1._07.function import func


@pytest.mark.parametrize(
    "case",
    [
        {"x": 12, "y": "気温", "z": 22.4, "result": "12時の気温は22.4"},
        {"x": 23, "y": "湿度", "z": 50.0, "result": "23時の湿度は50.0"},
    ],
)
def test_func(case):
    assert func(case["x"], case["y"], case["z"]) == case["result"]

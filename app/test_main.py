from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, combination",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "1 cent should be combinated into 1 penny",
            "6 cents should be combinated into 1 penny + 1 nickel",
            "17 cents should be combibated into 2 pennies + 1 nickel + 1 dime",
            "50 cents should be combinated into 2 quarters"
        ]
    )
    def test_geting_coin_combination(
        self,
        cents: int,
        combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == combination

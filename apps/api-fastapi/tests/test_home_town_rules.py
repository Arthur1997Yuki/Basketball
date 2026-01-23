import pytest

from Application.HomeTowns.rules import check_granularity


def test_check_granularity_rejects_ward_outside_tokyo():
    # 東京都以外では「区」を含む指定はNG。
    with pytest.raises(ValueError):
        check_granularity("27", "大阪市北区")

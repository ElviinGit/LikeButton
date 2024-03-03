import pytest
from src.slapping.slap_that_like_button import LikeState, slap_many


def test_empty_slap():
    assert slap_many(LikeState.empty, '') is LikeState.empty


def test_single_slap():
    assert slap_many(LikeState.empty, "l") is LikeState.liked
    assert slap_many(LikeState.empty, "d") is LikeState.disliked


@pytest.mark.parametrize("test_input, expected", [
     ("ll", LikeState.empty),
     ("dd", LikeState.empty),
     ("ld", LikeState.disliked),
     ("dl", LikeState.liked),
     ("ldd", LikeState.empty),
     ("lldd", LikeState.empty),
     ("ddl", LikeState.liked),
])
def test_many_slaps(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regex not supported yet")
def test_regex_slap():
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_slap():
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, "x")

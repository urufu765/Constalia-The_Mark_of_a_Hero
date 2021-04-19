'''
For testing functions that require root level imports
'''
import pytest
from resources import mapper
from resources.global_dic import v_long, v_major, v_minor, v_hotfx, v_ltype


def test_check_version() -> None:
    """
    Isn't here for actual testing, is here for noting what version this
    test was made/updated for
    """
    assert v_long == 'Version alpha'  # Don't change
    assert v_major == '1'
    assert v_minor == '0'
    assert v_hotfx == '0'
    assert v_ltype in ['raw', 'unstable', 'stable']


def test_mapper_init_mithavil() -> None:
    """
    Tests initializing the mithavil map
    """
    test_map = mapper.Mithavil()
    assert test_map.map_id == 0


def test_mapper_init_home() -> None:
    """
    Tests initializing the home map
    """
    test_map = mapper.Home()
    assert test_map.map_id == 1


def test_mapper_init_ravia_house() -> None:
    """
    Tests initializing Ravia's house map
    """
    test_map = mapper.Ravia_House()
    assert test_map.map_id == 2


if __name__ == '__main__':
    pytest.main(['alpha_tester.py'])

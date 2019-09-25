import pytest
from datetime import datetime
from plotdarn.utils import antipode, sun_position
from plotdarn.locations import north_pole, Location


def test_antipode():
    assert antipode(-72) == 108


def test_antipode_pos():
    assert antipode(72) == -108


def test_antipode_lat():
    assert antipode(20, axis='latitude') == -20


def test_antipode_lat_neg():
    assert antipode(-20, axis='latitude') == 20


def test_antipode_zero():
    assert antipode(0) == 180


def test_antipode_unknown_type():
    with pytest.raises(ValueError):
        antipode(20, axis='anything')


def test_sun_position():
    time = datetime(year=2012, month=6, day=15, hour=22, minute=2)
    azimuth = sun_position(north_pole, time)
    assert azimuth == 330.3365208965877


def test_sun_position_2():
    time = datetime(year=2012, month=6, day=15, hour=22, minute=2)
    loc = Location(80.2281362381121, -72.41454428382853)
    assert sun_position(loc, time) == 262.2580553157149


def test_sun_position_strtime():
    time = "2012-06-15 22:02"
    assert sun_position(north_pole, time) == 330.3365208965877


def test_sun_position_strtime_timezone():
    time = "2012-06-15 22:02Z"
    assert sun_position(north_pole, time) == 330.3365208965877


def test_sun_position_str_unknown():
    time = "Not a valid time"
    with pytest.raises(ValueError):
        sun_position(north_pole, time)


def test_sun_position_not_a_loc():
    loc = (22, 30)
    time = "2012-06-15 22:02Z"
    with pytest.raises(AttributeError):
        sun_position(loc, time)

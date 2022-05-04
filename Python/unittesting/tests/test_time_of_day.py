from to_test import time_of_day
import pytest
from freezegun import freeze_time
import datetime


@freeze_time("2022-05-14 05")
def test_night_time_of_day():
    assert time_of_day() == "night"


@freeze_time("2022-05-14 06")
def test_night_time_of_day():
    assert time_of_day() == "morning"


@freeze_time("2022-05-14 13")
def test_night_time_of_day():
    assert time_of_day() == "afternoon"







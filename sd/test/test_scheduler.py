import pytest
from schedule.scheduler import Scheduler
from datetime import datetime, timedelta, time, date

@pytest.mark.parametrize(
    'test_dt, expected_slot',
    [
        (datetime.combine(date.today() + timedelta(weeks=2, days=1), time(hour=16, minute=30)), (10, 15)),
        (datetime.combine(date.today() + timedelta(weeks=2, days=1), time(hour=9, minute=30)), (10, 3))
    ]
)
def test__available_index__(test_dt, expected_slot):
    indices = Scheduler.__available_index__(test_dt)
    assert indices == expected_slot

@pytest.mark.parametrize(
    'groomers, slot, checking',
    [
        (['Rachel', 'Raul', 'Renata', 'Ringo'], [], ['Rachel', 'Raul', 'Renata', 'Ringo']),
        (['Rachel', 'Raul', 'Renata', 'Ringo'], ['Raul', 'Renata'], ['Rachel', 'Ringo']),
        (['Rachel', 'Raul', 'Renata', 'Ringo'], ['Raul', 'Ringo'], ['Rachel', 'Renata']),
        (['Rachel', 'Raul', 'Renata', 'Ringo'], ['Rachel', 'Raul', 'Renata', 'Ringo'], [])
    ]
)
def test__available_groomer__(groomers, slot, checking):
    groomer = Scheduler.__available_groomer__(groomers, slot)
    assert groomer is None and len(checking) == 0 or groomer in checking

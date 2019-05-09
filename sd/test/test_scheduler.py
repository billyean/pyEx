import pytest
from final.scheduler import Scheduler
from datetime import datetime, timedelta, time


def test__available_index_afternoon__():
    now = datetime.now()

    two_weeks_one_day = datetime.combine(now.date() + timedelta(weeks=2, days=1), time(hour=16, minute=30))
    indices = Scheduler.__available_index__(two_weeks_one_day)
    assert indices == (10, 15)


def test__available_index_morning__():
    now = datetime.now()

    two_weeks_one_day = datetime.combine(now.date() + timedelta(weeks=2, days=1), time(hour=9, minute=30))
    indices = Scheduler.__available_index__(two_weeks_one_day)
    assert indices == (10, 3)


@pytest.mark.parametrize(
    'groomers, slot, checking',
    [
        (['Rachel', 'Raul', 'Renata', 'Ringo'], [], ['Rachel', 'Raul', 'Renata', 'Ringo']),
        (['Rachel', 'Raul', 'Renata', 'Ringo'], ['Raul', 'Renata'], ['Rachel', 'Ringo']),
        (['Rachel', 'Raul', 'Renata', 'Ringo'], ['Raul', 'Ringo'], ['Rachel', 'Renata']),
        (['Rachel', 'Raul', 'Renata', 'Ringo'], ['Rachel', 'Raul', 'Renata', 'Ringo'], [])
    ]
)
def test__available_grommer__(groomers, slot, checking):
    grommer = Scheduler.__available_grommer__(groomers, slot)
    assert grommer is None and len(checking) == 0 or grommer in checking

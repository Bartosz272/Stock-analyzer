import project
from datetime import date

def test_sale():
    assert project.image_ans('TSLA',date.fromisoformat('2024-12-09')) == 'SALE'
    assert project.image_ans('META',date.fromisoformat('2024-12-09')) == 'SALE'

def test_wait():
    assert project.image_ans('TSLA',date.fromisoformat('2024-12-04')) == 'HOLD'
    assert project.image_ans('^GSPC',date.fromisoformat('2024-05-20')) == 'HOLD'

def test_buy():
    assert project.image_ans('TSLA',date.fromisoformat('2024-10-12')) == 'BUY'
    assert project.image_ans('AAPL',date.fromisoformat('2024-03-05')) == 'BUY'
from money import Money

def test_usd_conversion():
    assert Money(1.1, 'usd') == Money(1, 'eur')
    assert Money(1, 'usd') != Money(1, 'eur')
    assert Money(0.011065, 'usd') == Money(1, 'jpy')
    assert Money(1, 'usd') != Money(1, 'jpy')
    assert Money(531.40, 'usd') == Money(1, 'btc')

def test_euro_conversion():
    assert Money(1, 'eur') == Money(1.1, 'usd')
    assert Money(1, 'eur') > Money(1, 'usd')
    assert Money(1, 'eur') != Money(1, 'usd')
    assert Money(1, 'eur') < Money(1, 'btc')
    assert Money(1, 'eur') != Money(1, 'btc')
    assert Money(1, 'eur') > Money(1, 'jpy')
    assert Money(1, 'eur') != Money(1, 'jpy')

def test_yen_conversion():
    assert Money(1, 'jpy') == Money(0.011065, 'usd')
    assert Money(1, 'jpy') != Money(1, 'usd')
    assert Money(1, 'jpy') < Money(1, 'usd')
    assert Money(1, 'jpy') < Money(1, 'eur')
    assert Money(1, 'jpy') != Money(1, 'eur')
    assert Money(1, 'jpy') < Money(1, 'btc')
    assert Money(1, 'jpy') != Money(1, 'btc')

def test_bitcoin_conversion():
    assert Money(1, 'btc') == Money(531.40, 'usd')
    assert Money(1, 'btc') > Money(1, 'usd')
    assert Money(1, 'btc') != Money(1, 'usd')
    assert Money(1, 'btc') > Money(1, 'eur')
    assert Money(1, 'btc') != Money(1, 'eur')
    assert Money(1, 'btc') > Money(1, 'jpy')
    assert Money(1, 'btc') != Money(1, 'jpy')

def test_invalid_entry():
    assert Money(1, 'test').currency_type == "Invalid Input"

def test_addition():
    dollars = Money(5, 'usd') + Money(10, 'eur')
    assert dollars.currency == 'usd'
    assert dollars.amount == 16.0

def test_subtraction():
    euros = Money(100, 'eur') - Money(25, 'jpy')
    assert euros.currency == 'eur'
    assert euros.amount == 109.72337500000002

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

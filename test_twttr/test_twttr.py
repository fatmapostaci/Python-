from twttr import shorten

def test_shorten():

    assert shorten('asdetilk ewSKE') == 'sdtlk wSK'.upper()
    assert shorten('Fatma Postacı') == 'Ftm Pstc'.upper()


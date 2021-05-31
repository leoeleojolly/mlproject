from mlproject.distance import haversine

def test_good_type():
    assert type(haversine(1,1,1,5))==float

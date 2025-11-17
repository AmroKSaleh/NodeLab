from nodelab.standards.creepage import creepage_distance

def test_creepage_distance():
    assert creepage_distance(10, "I", 1) == 0.08

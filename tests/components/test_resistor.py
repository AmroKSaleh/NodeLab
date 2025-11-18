from nodelab.components.resistor import Resistor

def test_resistor():
    r = Resistor(1000, [1, 2])
    assert r.value == 1000
    assert r.nodes == [1, 2]

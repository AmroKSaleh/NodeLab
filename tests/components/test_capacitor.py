from nodelab.components.capacitor import Capacitor

def test_capacitor():
    c = Capacitor(1e-6, [1, 2])
    assert c.value == 1e-6
    assert c.nodes == [1, 2]

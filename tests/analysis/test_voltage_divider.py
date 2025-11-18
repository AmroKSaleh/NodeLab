from nodelab.analysis.voltage_divider import voltage_divider

def test_voltage_divider():
    assert voltage_divider(5, 1000, 1000) == 2.5

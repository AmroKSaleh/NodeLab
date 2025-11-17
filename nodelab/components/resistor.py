from nodelab.core.component import Component

class Resistor(Component):
    """
    A resistor component.
    """

    def __init__(self, value, nodes):
        self._value = value
        self._nodes = nodes

    @property
    def value(self):
        return self._value

    @property
    def nodes(self):
        return self._nodes

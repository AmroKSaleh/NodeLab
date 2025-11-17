from abc import ABC, abstractmethod

class Component(ABC):
    """
    Abstract base class for all circuit components.
    """

    @property
    @abstractmethod
    def value(self):
        """
        The value of the component (e.g., resistance in ohms, capacitance in farads).
        """
        pass

    @property
    @abstractmethod
    def nodes(self):
        """
        The nodes the component is connected to.
        """
        pass

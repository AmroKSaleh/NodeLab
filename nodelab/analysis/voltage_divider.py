def voltage_divider(v_in, r1, r2):
    """
    Calculates the output voltage of a voltage divider.

    Args:
        v_in: The input voltage.
        r1: The resistance of the first resistor.
        r2: The resistance of the second resistor.

    Returns:
        The output voltage.
    """
    return v_in * (r2 / (r1 + r2))

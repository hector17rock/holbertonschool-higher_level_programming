#!/usr/bin/python3
def safe_print_interger(value):
    """Prints an interger using '{;d}'.format

    Args:
        Value: Any type of value.

    Returns:
        Trus if value is an interger and printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

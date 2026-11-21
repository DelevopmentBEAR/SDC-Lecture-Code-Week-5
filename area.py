# Functions for computing areas of various shapes

def triangle_area(height, base):
    """
        Compute the area of a triangle with the given height and base.
        Raises a ValueError if either height or base are negative.
    """
    if height < 0 or base < 0:
        raise ValueError('Base and height must be a positive number.')
    return height * base * 0.5
    
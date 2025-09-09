#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a_normalise = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a_normalise = (tuple_a[0], 0)
    else:
        tuple_a_normalise = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tuple_b_normalise = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b_normalise = (tuple_b[0], 0)
    else:
        tuple_b_normalise = (tuple_b[0], tuple_b[1])

    tuple_sum = (
        tuple_a_normalise[0] + tuple_b_normalise[0],
        tuple_a_normalise[1] + tuple_b_normalise[1]
    )

    return tuple_sum

    """def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
    """


from numbers import Real


def tinh_tong(a: Real, b: Real) -> Real:
    """Tra ve tong cua hai so."""
    if not isinstance(a, Real) or not isinstance(b, Real):
        raise TypeError("a va b phai la so")
    return a + b

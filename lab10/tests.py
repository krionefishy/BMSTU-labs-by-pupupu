def test(start: float, end: float, n1: float, n2: float, eps: float):
    if start >= end:
        return False 
    if n1 < 2 or n2 < 2:
        return False 
    if eps <= 0:
        return False
    return True



if __name__ == "__main__":
    pass
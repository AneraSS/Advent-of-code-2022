def is_range_in_range(range1, range2):      # bool
    a, b = range1   # pattern-matching! bc range1 is (a, b)
    c, d = range2
    if ((a<c) and (d<b)) or ((a>c) and (d>b)):
        return True
    else:
        return False
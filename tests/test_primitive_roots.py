from prng.util.util import primitive_roots
import pytest

def test_primitive_roots():
    prim_roots_sets = [
        [3, [2]],
        [7, [3,5]],
        [13, [2,6,7,11]],
        [17, [3,5,6,7,10,11,12,14]],
        [19, [2,3,10,13,14,15]],
        [31, [3,11,12,13,17,21,22,24]],
        [53, [2,3,5,8,12,14,18,19,20,21,22,26,27,31,32,33,34,35,39,41,45,48,50,51]],
        [61, [2,6,7,10,17,18,26,30,31,35,43,44,51,54,55,59]],
        [79, [3,6,7,28,29,30,34,35,37,39,43,47,48,53,54,59,60,63,66,68,70,74,75,77]],
        [103, [5,6,11,12,20,21,35,40,43,44,45,48,51,53,54,62,65,67,70,71,74,75,77,78,84,85,86,87,88,96,99,101]],
    ]

    assert all(sorted(primitive_roots(a)) == prs for a,prs in prim_roots_sets)

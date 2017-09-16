from typing import List, Set, Tuple

def saddle_points(given: List[List[int]]) -> Set[Tuple[int, int]]:
    if not all(len(given[0])==len(row) for row in given[1:]):
        raise ValueError("Non-uniform row sizes detected.  Aborting.")

    transposed = [list(c) for c in zip(*given)]
    out = []
    for ri, rv in enumerate(given):
        for ci, cv in enumerate(transposed):
            if max(rv) == min(cv) == given[ri][ci]:
                out.append((ri, ci))
    return set(out)

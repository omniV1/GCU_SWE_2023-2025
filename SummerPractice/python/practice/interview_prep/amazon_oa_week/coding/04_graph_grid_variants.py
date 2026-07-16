"""
Pattern Pack: Graph/Grid BFS-DFS Variants
"""

from collections import deque


def num_islands_v1(grid):
    """Count connected components of '1' cells (4-directional)."""
    # TODO
    pass


def shortest_path_binary_matrix_v2(grid):
    """
    Return shortest path length from top-left to bottom-right (8-directional),
    moving through 0 cells only. Return -1 if impossible.
    """
    # TODO
    pass


def flood_fill_v3(image, sr, sc, color):
    """Classic flood fill (4-directional)."""
    # TODO
    pass


if __name__ == "__main__":
    # v1 edge cases
    g1 = [
        ["1", "1", "0", "0"],
        ["1", "0", "0", "1"],
        ["0", "0", "1", "1"],
    ]
    assert num_islands_v1(g1) == 3
    assert num_islands_v1([["0"]]) == 0
    assert num_islands_v1([["1"]]) == 1

    # v2 edge cases
    assert shortest_path_binary_matrix_v2([[0, 1], [1, 0]]) == 2
    assert shortest_path_binary_matrix_v2([[1]]) == -1
    assert shortest_path_binary_matrix_v2([[0]]) == 1

    # v3 edge cases
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill_v3(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert flood_fill_v3([[0]], 0, 0, 0) == [[0]]

    print("All graph/grid variants passed.")

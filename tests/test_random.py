from n_squared import solver
from bf_solver import bf_solution
from dataset_generator import gen

def test_rand():
    for i in range(100):
        inp, out = gen()

        # sol = bf_solution(inp[0], inp[1])
        sol = solver(inp[1], inp[0])

        assert sol == out
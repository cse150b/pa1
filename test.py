from ai import AI
from game import Grid

def test():
    with open("tests") as file:
        grid = Grid()
        ai = AI(grid, "dfs")

        lines = file.readlines()
        for line_i, line in enumerate(lines):
            print("test {}/{}: ".format(line_i + 1, len(lines)))

            split = line.split()
            score = {}
            score["dfs"] = split[0]
            score["bfs"] = split[1]
            score["ucs"] = split[2]
            score["astar"] = split[3]

            grid.load(" ".join(split[4:]))

            for method in ["dfs", "bfs", "ucs", "astar"]:
                ai.set_type(method)
                ai.set_search()
                while not ai.finished:
                    ai.make_step()

                if not ai.failed:
                    ai.get_result()
                
                expected = int(score[method])
                actual = ai.final_cost

                if expected != actual:
                    print("\t {} FAILED: expected score of {}, actual {}".format(method, expected, actual))

                else:
                    print("\t {} PASSED".format(method))

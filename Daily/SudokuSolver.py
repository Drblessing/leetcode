import sys

args = sys.argv[1:]
puzzles = open(r"a1.txt").read().splitlines()
import time


def select_unassigned_var(assignment, variables, neighbors):
    unassigned = [i for i in range(len(assignment)) if assignment[i] == "."]
    if not unassigned:
        return None
    mrv = min(unassigned, key=lambda x: len(variables[x]))
    return mrv


def ordered_domain(var_index, variables, q_table):
    domain = variables[var_index]
    domain = [p for p in domain if q_table[p] != 9]
    domain = sorted(domain, key=lambda x: q_table[x])
    return domain


def update_variables(value, var_index, assignment, variables, neighbors):
    assignment = assignment[:var_index] + str(value) + assignment[var_index + 1 :]
    variables[var_index].add(value)
    for neighbor in neighbors[var_index]:
        if variables[neighbor] != None and value in variables[neighbor]:
            variables[neighbor].discard(value)
    return assignment, variables


def solve(puzzle, neighbors):
    variables, puzzle, q_table = initialize_ds(puzzle, neighbors)
    return recursive_backtracking(puzzle, variables, neighbors, q_table)


def recursive_backtracking(assignment, variables, neighbors, q_table):
    # print(display(assignment))
    if select_unassigned_var(assignment, variables, neighbors) == None:
        return assignment
    var_index = select_unassigned_var(assignment, variables, neighbors)

    myDomain = ordered_domain(var_index, variables, q_table)
    for value in myDomain:
        if value not in [assignment[i] for i in neighbors[var_index] if i != var_index]:
            new_assignment, new_variables = update_variables(
                value, var_index, assignment, variables, neighbors
            )
            result = recursive_backtracking(
                new_assignment, new_variables, neighbors, q_table
            )
            if result != None:
                return result
            else:
                assignment = assignment[:var_index] + "." + assignment[var_index + 1 :]
                variables[var_index].discard(value)
                for neighbor in neighbors[var_index]:
                    if variables[neighbor] != None:
                        variables[neighbor].add(value)
                q_table[value] -= 1
    return None


def recursive_backtracking1(assignment, variables, neighbors, q_table):
    if select_unassigned_var(assignment, variables, neighbors) == None:
        return assignment
    var_index = select_unassigned_var(assignment, variables, neighbors)

    myDomain = ordered_domain(var_index, variables, q_table)
    for value in myDomain:
        if value not in [assignment[i] for i in neighbors[var_index] if i != var_index]:
            new_assignment, new_variables = update_variables(
                value, var_index, assignment, variables, neighbors
            )

            # Forward checking
            removed = {neighbor: [] for neighbor in neighbors[var_index]}
            for neighbor in neighbors[var_index]:
                if new_variables[neighbor] != None and value in new_variables[neighbor]:
                    new_variables[neighbor].discard(value)
                    removed[neighbor].append(value)
                    if len(new_variables[neighbor]) == 0:
                        return None  # No valid assignments for neighbor, backtrack immediately

            result = recursive_backtracking(
                new_assignment, new_variables, neighbors, q_table
            )
            if result != None:
                return result
            else:
                assignment = assignment[:var_index] + "." + assignment[var_index + 1 :]
                variables[var_index].discard(value)
                for neighbor in neighbors[var_index]:
                    if variables[neighbor] != None:
                        variables[neighbor].add(value)
                q_table[value] -= 1

                # Restore the removed values
                for neighbor, values in removed.items():
                    new_variables[neighbor].update(values)
    return None


def display(solution):
    displayHeader = "---------------------\n"
    displayBody = ""
    counter = 0
    for i in range(len(solution)):
        displayBody += solution[i] + " "
        counter += 1
        if counter % 3 == 0:
            displayBody += "  "
        if counter % 9 == 0:
            displayBody += "\n"
    return displayHeader + displayBody + displayHeader


def sudoku_csp(n=9):
    return [
        [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23, 24, 25, 26],
            [27, 28, 29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42, 43, 44],
            [45, 46, 47, 48, 49, 50, 51, 52, 53],
            [54, 55, 56, 57, 58, 59, 60, 61, 62],
            [63, 64, 65, 66, 67, 68, 69, 70, 71],
            [72, 73, 74, 75, 76, 77, 78, 79, 80],
        ],  # rows
        [
            [0, 9, 18, 27, 36, 45, 54, 63, 72],
            [1, 10, 19, 28, 37, 46, 55, 64, 73],
            [2, 11, 20, 29, 38, 47, 56, 65, 74],
            [3, 12, 21, 30, 39, 48, 57, 66, 75],
            [4, 13, 22, 31, 40, 49, 58, 67, 76],
            [5, 14, 23, 32, 41, 50, 59, 68, 77],
            [6, 15, 24, 33, 42, 51, 60, 69, 78],
            [7, 16, 25, 34, 43, 52, 61, 70, 79],
            [8, 17, 26, 35, 44, 53, 62, 71, 80],
        ],  # columns
        [
            [0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80],
        ],
    ]  # boxes


def initialize_ds(puzzle, neighbors):
    q_table = {i: 0 for i in "123456789"}
    variables = {i: set() for i in range(81)}
    for i in puzzle:
        if i != ".":
            q_table[i] += 1

    all = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    for i in neighbors:
        for j in neighbors[i]:
            if puzzle[j] != ".":
                variables[j].add(puzzle[j])
    # print("VARIABLES", variables)
    for i in variables:
        variables[i] = all - variables[i]
    # print("POST VARIABLES", variables)
    return variables, puzzle, q_table


def sudoku_neighbors(
    csp_table,
):  # {0:[0, 1, 2, 3, 4, ...., 8, 9, 18, 27, 10, 11, 19, 20], 1:
    neighbors = {i: list() for i in range(81)}
    for a in neighbors:
        for rcb in csp_table:
            for myList in rcb:
                if a in myList:
                    neighbors[a] += myList
                    neighbors[a] = list(set(neighbors[a]))
    return neighbors


def checksum(solution):
    return sum(ord(char) for char in solution) - (
        len(solution) * min([ord(char) for char in solution])
    )


def main():
    csp_table = sudoku_csp()  # rows, cols, and sub_blocks
    neighbors = sudoku_neighbors(
        csp_table
    )  # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
    start_time = time.time()
    for line, puzzle in enumerate(puzzles):
        line, puzzle = line + 1, puzzle.rstrip()
        print("{}: {}".format(line, puzzle))
        solution = solve(puzzle, neighbors)
        if solution == None:
            print("No solution found.")
            break
        print(
            "{}{} {}".format(" " * (len(str(line)) + 2), solution, checksum(solution))
        )
    print("Duration:", (time.time() - start_time))


if __name__ == "__main__":
    main()
# Japneet Kaur, Period 1, 2023

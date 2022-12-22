import time
from grid import Grid
from plot_results import PlotResults

# Consistency Checking Fucntion

def is_consistent(var, grid, d):
    # Check if d is in domain of var
    domain_of_var = grid.get_cells()[var[0]][var[1]]
    if d not in domain_of_var:
        return False
    
    # Check for Row consistency
    # Var is a tuple
    row_fixed = var[0]
    for col in range(grid.get_width()):
        domain_val = grid.get_cells()[row_fixed][col]
        if (d == domain_val):
            return False
    
    # Check for Column consistency
    col_fixed = var[1]
    for row in range(grid.get_width()):
        domain_val = grid.get_cells()[row][col_fixed]
        if (d == domain_val):
            return False

    # Check for Unit consistency
    row_int = int(var[0])
    col_int = int(var[1])
    row_init = (row_int // 3)*3
    col_init = (col_int // 3) * 3

    for i in range (row_init, row_init+3):
        for j in range (col_init, col_init + 3):
            if i == row_int and j == col_int:
                continue
            domain_val = grid.get_cells()[i][j]
            if(d == domain_val):
                return False

    # Return True if all cases pass
    
    return True



def select_variable_fa(grid):
    for row in range(grid.get_width()):
        for col in range(grid.get_width()):
            len_domain = 0
            for d in grid.get_cells()[row][col]:
                len_domain += 1
            if (len_domain > 1):
                return (row, col)
    return None

def select_variable_mrv(grid):
    domain_val_dict = {}
    for row in range(grid.get_width()):
        for col in range(grid.get_width()):
            len_domain = 0
            for d in grid.get_cells()[row][col]:
                len_domain += 1
            if (len_domain > 1):   
                key = (row, col)
                val = len_domain
                domain_val_dict[key] = val
    return (min(domain_val_dict, key = domain_val_dict.get))
    return None

def var_selector(grid):
    return select_variable_mrv(grid) or select_variable_fa(grid)

def set_var(var, grid, d):
    grid.get_cells()[var[0]][var[1]] = d
    return

def search(grid, var_selector):
    if grid.is_solved():
        return grid, True
    var = var_selector(grid)
    domain_of_var = grid.get_cells()[var[0]][var[1]]
    for d in domain_of_var:
        if is_consistent(var, grid, d):
            copy_grid = grid.copy()
            set_var(var, copy_grid, d)
            (ret_grid, ret_val) = search(copy_grid, var_selector)
    return grid, False

def forward_checking(grid, variable):
    return None

def pre_process_forward_checking(grid):
    return None

file = open('tutorial_problem.txt', 'r')
problems = file.readlines()
for p in problems:
    g = Grid()
    g.read_file(p)

    # test your backtracking implementation without inference here
    # this test instance is only meant to help you debug your backtracking code
    # once you have implemented forward checking, it is fine to find a solution to this instance with inference

    (a, b) = search(g, var_selector)
    print(b)

file = open('top95.txt', 'r')
problems = file.readlines()

for p in problems:
    g = Grid()
    g.read_file(p)
    
    # test your backtracking implementation with inference here
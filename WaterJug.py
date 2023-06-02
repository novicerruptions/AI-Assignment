# 1. Write a python program to solve the waterjug problem.

# Solution: We use a recursive approach to solve this problem

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    def solve_jug_problem(jug1_amount, jug2_amount):
        if jug1_amount == target_amount or jug2_amount == target_amount:
            return True
        
        if jug1_amount == 0:
            if solve_jug_problem(jug1_capacity, jug2_amount):
                print(f"Fill jug1 ({jug1_capacity})")
                return True
        
        if jug2_amount == jug2_capacity:
            if solve_jug_problem(jug1_amount, 0):
                print(f"Empty jug2 ({jug2_capacity})")
                return True
        
        if jug1_amount > 0:
            if jug2_amount < jug2_capacity:
                amount_to_pour = min(jug1_amount, jug2_capacity - jug2_amount)
                if solve_jug_problem(jug1_amount - amount_to_pour, jug2_amount + amount_to_pour):
                    print(f"Pour {amount_to_pour} units from jug1 to jug2")
                    return True
        
        if jug2_amount > 0:
            if jug1_amount < jug1_capacity:
                amount_to_pour = min(jug2_amount, jug1_capacity - jug1_amount)
                if solve_jug_problem(jug1_amount + amount_to_pour, jug2_amount - amount_to_pour):
                    print(f"Pour {amount_to_pour} units from jug2 to jug1")
                    return True
        
        return False
    
    print("Steps to solve the water jug problem:")
    if solve_jug_problem(0, 0):
        print("Problem solved!")
    else:
        print("No solution exists.")

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

# In this program, the water_jug_problem function takes three parameters: jug1_capacity and jug2_capacity representing the maximum capacities of the jugs, and target_amount representing  
# the desired amount of water to be present in one of the jugs.

# The solve_jug_problem function is a recursive helper function that tries different combinations of pouring and filling water in the jugs to reach the target amount. It checks various 
# conditions and calls itself recursively with updated jug amounts until a solution is found or all possibilities have been exhausted.

# The program prints the steps required to solve the water jug problem. If a solution exists, it displays the steps to achieve the desired amount of water; otherwise, it informs that no
# solution exists.

# You can modify the jug1_capacity, jug2_capacity, and target_amount variables to test the program with different values.
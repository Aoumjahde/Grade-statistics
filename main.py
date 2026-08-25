# -------- pre requirments to start the app 

"""
1. User inputs Exam point and Exericice completed
in till?
2. is empty input: is user input empry input the second function start called!
3. average and percentage
4. grade_distribution function
"""
# user inputs 
def user_input():
    results = []
    while True:
        data = input("Exam points and exercises completed:")
        if  data == "":
            break
        parts = data.split()
        points = int(parts[0])
        exercices = int(parts[1])
        results.append((points, exercices))
    return results

def calculate_average_points(results):
    if not results:
        return 0

    total= sum(points for points, exercises in results)

    return total/ len(results)

def calculate_average_exercises(results):
    if not results:
        return 0
    total = sum(exercises for points, exercises in results)
    return total / len(results)

def grad_distribution(points):
    if points >= 18:
        return 5
    elif points >= 15:
        return 4
    elif points >= 12:
        return 3
    elif points >= 9:
        return 2
    elif points >= 6:
        return 1
    else:
        return 0
    

def grade(results):
    distribution = {g:0 for g in range(6)}
    for points, exercises in results:
        g = grade(points)
        distribution[g] += 1
    return distribution

def print_statistics(results):
    print(f"Average exam points: {calculate_average_points(results)}")
    print(f"Average exercises completed: {calculate_average_exercises(results)}")
    print("Grade distribution:")
    distribution = grade(results)
    for g in sorted(distribution):
        print(f"{g}: {'*' * distribution[g]}")
def main():

    results = user_input()
    print_statistics(results)


main()



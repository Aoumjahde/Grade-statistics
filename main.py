"""
Develpîng a larger programming project
--> Statistics App
In this exercise you will write a program for printing out grade statistics for a university course.
"""

#function 01: user data
#function 02: finding points average
#function 03: pass percentage
#function 04: grad distribution
# fucntion 05: is formated fuction that show up fucns(2,3,4)

'''
Why functions approach, firslly for structure and organized 
operation, and guratnted everything in output need order(end product formate)

'''

def user_input():
    points_list = []
    exercises_list = []
    while True:
        user_inpt = str(input("Exam points and exercises completed: (points exerices ex, 00 00):"))
        if user_inpt == "":
            break
        else:
            spliting_points_exers = user_inpt.split()
            points = spliting_points_exers[0]
            exercises = spliting_points_exers[1]
            if  0<= int(points) <= 20:
                points_list.append(int(points))
            else:
                pass
            if 0<= int(exercises) <=  100:
                exercises_list.append(int(exercises))
            else:
                pass
    
    return [exercises_list, points_list]


def points_average(exercises_data, points_data):
    total_list = []
    for i in range(len(points_data)):
        exam_pts = points_data[i]
        exercises = exercises_data[i]
        exercise_points = exercises // 10
        total_points = exam_pts + exercise_points
        total_list.append(total_points)


    final_value = sum(total_list) / len(total_list)

    return final_value



'''
This function call the previece fucntion "user_input": that return points lists
--> calculation of length_list_points and return final result of everage.
'''


def grade(grad_point):
    if 0<= grad_point <= 14:
        return 0
    elif 15 <= grad_point <= 17:
        return 1
    elif 18 <= grad_point <= 20:
        return 2
    elif 21 <= grad_point <= 23:
        return 3
    elif 24 <= grad_point <= 27:
        return 4
    elif 28 <= grad_point <= 30:
        return 5

def grade_distribution(exercises_data, points_data):
    grade_counts = [0, 0, 0, 0, 0, 0]
    for i in range(len(points_data)):
        exam_pts = points_data[i]
        exercises = exercises_data[i]
        exercise_points = exercises // 10  
        total_points = exam_pts + exercise_points
        student_grade = grade(total_points)
        grade_counts[student_grade] += 1

    return grade_counts 

def final_output(epv ,grad_arr):
    print("Statistics:")
    print("Points Average: ", epv)

    print("Grade distribution:")
    for i in range(5,-1,-1):
        starts = "*"*grad_arr[i]
        print(f"{i}: {starts}")




     
     


# main function that hold our process and fucntion calls
def main():
    exercises_array, points_array = user_input()
    grade_dist = grade_distribution(exercises_array, points_array)
    points_average_dict = points_average(exercises_array, points_array)
    print(final_output(points_average_dict, grade_dist))
    
main()
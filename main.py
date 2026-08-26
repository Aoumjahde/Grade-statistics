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
    sum_points_exs = sum(exercises_list) + sum(points_list)
    return sum_points_exs


'''
This function call the previece fucntion "user_input": that return points lists
--> calculation of length_list_points and return final result of everage.
'''
def points_average(final_sum):
    # points_sum = sum(points_arr)
    points_average_resulth = final_sum // 10

    return points_average_resulth

def grade(grad_point):
    if grad_point <= 14:
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


def final_output(finall_sum, grad):
    print("Statistics:\n")
    print("Points Average: ", finall_sum)
    # print("Pass percentage: ", Pass_percentage)
    print("Grade distribution: ", grad)


    pass


     
     


# main function that hold our process and fucntion calls
def main():
    user_data = user_input()
    average = points_average(user_data)
    grad = grade(average)
    # print(grad)
    # user_input()))
    print(final_output(user_data, grad))
main()
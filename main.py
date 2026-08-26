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
            points_list.append(int(points))
            exercises_list.append(int(exercises))
    return points_list


'''
This function call the previece fucntion "user_input": that return points lists
--> calculation of length_list_points and return final result of everage.
'''
def points_average(points_arr):
    user_input()
    length_points = len(points_arr)
    points_sum = 0
    for num in points_arr:
        points_sum += num

    points_average_resulth = points_sum / length_points

    return points_average_resulth



# main function that hold our process and fucntion calls
def main():
    user_data = user_input()
    points_average_var = points_average(user_data)
    print(points_average_var)

main()
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
    return points_list, exercises_list

# main functio that hold our process and fucntion calls
def main():
    print(user_input())

main()
# Grade Statistics

This project is a Python-based grade statistics application for a university course. It reads student exam results and exercise completion data, calculates a final score, assigns grades, and prints a summary of the course performance.

## Overview

The program repeatedly asks the user for student data until an empty line is entered. Each valid input line contains:
- exam points between 0 and 20
- completed exercises between 0 and 100

The application then processes the information and outputs:
- the average total score
- the grade distribution across students
- a visual histogram using stars

## Project objectives

The goal of this project is to practice:
- working with user input
- processing lists of data
- using functions to structure logic
- performing calculations based on course rules
- presenting results in a readable format

## Program behavior

The program follows a simple workflow:
1. Read student input from the terminal.
2. Validate the numbers.
3. Convert exercise count to exercise points.
4. Add the exam points and exercise points for each student.
5. Calculate the average score.
6. Map each total to a grade.
7. Count the number of students in each grade category.
8. Print the statistics summary.

## Implementation approach

### 1. Functional decomposition

The code is divided into separate functions to keep the logic organized and easy to understand. This structure improves readability and makes maintenance easier.

The main functions are:
- user_input(): collects and validates input values
- points_average(): calculates the average total points
- grade(): converts a total score into a grade level
- grade_distribution(): counts how many students received each grade
- final_output(): prints the final statistics
- main(): runs the full process in the correct order

### 2. Input handling

The application uses a while loop to continue reading input until the user enters an empty string. This is the central interactive feature of the project and matches the assignment requirements.

Each non-empty line is split into two values, and both are checked against the valid range before being stored. This prevents invalid data from affecting the final results.

### 3. Exercise points calculation

The exercise contribution is computed with the rule:
- exercise points = exercises // 10
- total points = exam points + exercise points

This follows the course rules used in the project and keeps the calculations consistent.

### 4. Grade mapping

A dedicated grade() function maps the total point value into the course grade scale:
- 0 to 14 -> 0
- 15 to 17 -> 1
- 18 to 20 -> 2
- 21 to 23 -> 3
- 24 to 27 -> 4
- 28 to 30 -> 5

This keeps the grading behavior isolated and easy to adjust if rules change.

### 5. Grade distribution logic

The program stores grade counts in a list where each index corresponds to a grade level. This makes it simple to count students in each category and print the distribution in order.

### 6. Output formatting

The final statistics are presented in a readable format:
- average points are printed first
- grade distribution is shown next
- stars represent how many students are in each grade category

This keeps the output clear and easy to interpret.

## Example input

```text
10 20
15 30
18 40
20 50

```

## Example output

```text
Statistics:
Points Average: 20.0
Grade distribution:
5: *
4: 
3: 
2: 
1: 
0: 
```

## How to run

From the project directory, run:

```bash
python main.py
```

## Project status

This project is complete as a working course exercise and demonstrates the use of Python functions, loops, validation, calculations, and result formatting in a realistic data-processing scenario.

## Summary

This grade statistics project is a solid example of a beginner-to-intermediate Python application that collects user data, processes it with structured logic, and outputs a clear statistical summary. The design prioritizes readability, maintainability, and straightforward problem solving, which makes it suitable as a training project and a foundation for future extensions.

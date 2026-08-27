# Grade Statistics

This project is a university grade statistics application developed as a larger programming exercise. The goal is to collect student exam results and exercise progress, calculate grade statistics, and print a clear summary of performance.

## Project goal

The program asks the user for results from multiple students. Each record contains:
- exam points between 0 and 20
- completed exercises between 0 and 100

The program keeps asking for input until the user enters an empty line.

## What the program does

After collecting the data, the application:
- calculates the average total score
- converts total points into a grade
- counts how many students fall into each grade category
- prints the final statistics in a readable format

## Implementation decisions and approach

### 1. Function-based structure

I chose a modular design instead of writing everything in one long block. This makes the code easier to read, test, and maintain.

The main functions are:
- user_input()
  - collects student data from the user
  - reads input in a loop until an empty line is entered
  - splits each line into exam points and exercise count
  - validates that values are within the allowed ranges
- points_average(exercises_data, points_data)
  - calculates the total points for each student
  - adds exercise points using the rule: exercises // 10
  - computes the average of all totals
- grade(grad_point)
  - maps total score to a grade using the defined grade scale
- grade_distribution(exercises_data, points_data)
  - counts students in each grade category
  - returns a list representing the distribution
- final_output(epv, grad_arr)
  - prints the summary statistics and grade histogram
- main()
  - coordinates the whole workflow by calling the functions in the correct order

### 2. Input handling approach

The input process is controlled by a while loop that continues until the user enters a blank line. This matches the exercise requirement and keeps the application interactive.

For every non-empty input line:
- the data is split into two values
- each value is checked against the expected range
- valid values are stored in their respective lists
- invalid values are ignored for safety

This approach keeps the program simple and robust without overcomplicating the logic.

### 3. Exercise points conversion

The project uses a simplified rule for exercise contribution:
- exercise points are calculated as exercises // 10
- total score = exam points + exercise points

This follows the course rules and keeps the calculation consistent with the expected grade statistics model.

### 4. Grade mapping strategy

A separate grade() function was used to convert each total score into a grade. This keeps the grading logic isolated and easy to change if the grading thresholds need to be adjusted later.

The grade ranges are mapped as follows:
- 0 to 14 -> 0
- 15 to 17 -> 1
- 18 to 20 -> 2
- 21 to 23 -> 3
- 24 to 27 -> 4
- 28 to 30 -> 5

This makes the logic explicit and easy to understand.

### 5. Grade distribution design

Instead of printing grades one by one, the program stores them in a grade_counts list. Each index represents a grade level, and the value at that index stores how many students received that grade.

This makes it easy to:
- count students in each category
- print the final distribution in order
- produce a star-based histogram for the output

### 6. Output formatting decision

The final output is structured in a readable statistical format:
- average points are printed first
- grade distribution is printed afterwards
- stars are used to show how many students achieved each grade

This makes the report easy to read even when there are many results.

## Why this approach was chosen

This project is a learning exercise, so the main priorities were:
- clear logic
- maintainable code
- step-by-step problem solving
- readability over optimization

By separating responsibilities into small functions, the code becomes easier to follow and to extend later if more features are added.

## Current status

The project is implemented as a working grade statistics program using a modular approach with input validation, grade calculation, distribution tracking, and final reporting.

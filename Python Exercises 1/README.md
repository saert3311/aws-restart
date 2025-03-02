# Python Exercises 1 – Lists and Dictionaries

## Basic Exercises (1-4)

### Exercise 1: List Creation and Indexing
Create a list of your five favorite foods. Then print the first and last items in the list.

### Exercise 2: List Modification
Create a list with three numbers. Add two more numbers to the end of the list, then replace the middle number with 99. Print the final list.

### Exercise 3: Dictionary Creation and Access
Create a dictionary mapping three countries to their capitals. Print the capital of the second country you added.

### Exercise 4: Dictionary Update
Create a dictionary with your name, age, and favorite color. Change your favorite color to a new value, then add a new key-value pair for your favorite food. Print the final dictionary.

---

## Method-Based Exercises (5-10)

### Exercise 5: List Methods - `append()` and `insert()`
Create an empty list. Use the `append()` method to add three fruits. Then use the `insert()` method to add `"Apple"` at the beginning of the list. Print the list.  

**Hint:**  
- `append()` adds an item to the end of a list.  
- `insert()` adds an item at a specific position.

### Exercise 6: List Methods - `remove()` and `pop()`
Create a list with five animals. Use `remove()` to delete one animal by its value. Then use `pop()` to remove the last animal and store it in a variable. Print both the final list and the removed animal.  

**Hint:**  
- `remove()` deletes by value.  
- `pop()` removes by position and returns the removed item.

### Exercise 7: List Methods - `sort()` and `reverse()`
Create a list of five numbers in random order. Use the `sort()` method to arrange them in ascending order. Then use the `reverse()` method to reverse the order. Print the list after each operation.  

**Hint:**  
- `sort()` arranges items in ascending order.  
- `reverse()` flips the order of the list.

### Exercise 8: Dictionary Methods - `get()`
Create a dictionary of three book titles and their authors. Use the `get()` method to retrieve an author, providing a default value of `"Unknown"` if the book isn't found. Try it with both an existing book and a non-existent book.  

**Hint:**  
- `get()` allows you to specify a default value to return if the key doesn't exist.

### Exercise 9: Dictionary Methods - `keys()` and `values()`
Create a dictionary mapping five subjects to their classroom numbers. Use the `keys()` method to get all subjects, and the `values()` method to get all classroom numbers. Print both results.  

**Hint:**  
- `keys()` returns all keys in the dictionary.  
- `values()` returns all values.

### Exercise 10: Dictionary Methods - `update()`
Create two dictionaries: one with three student names and their grades, and another with two different student names and their grades. Use the `update()` method to combine them into the first dictionary. Print the final dictionary.  

**Hint:**  
- `update()` merges a dictionary with another dictionary or with key-value pairs.

---

## Complex Exercises (11-12)

### Exercise 11: Multi-step List Processing
1. Ask the user to input ten integers between 1 and 100, one at a time.  
2. Create a new list containing only the numbers from the user's input that are greater than 50.  
3. Calculate the average of these numbers and add this average to the end of the new list.  
4. Print both lists and the calculated average.  

**Hint:**  
- Use a `for` loop with `range(10)` to collect the inputs.  
- Use the `sum()` and `len()` functions for calculating the average.

### Exercise 12: Nested Data Structures
Create a program that collects information about departments and employees:

1. Ask the user for the number of departments (at least 2).  
2. For each department, ask for the department name.  
3. For each department, ask how many employees are in that department (at least 2).  
4. For each employee, ask for their name and salary.  
5. Store all this information in a dictionary where keys are department names and values are lists of employee tuples `(name, salary)`.  
6. Calculate and print the total salary for each department.  
7. Find and print the name of the highest-paid employee across all departments.  

**Hint:**  
- You can use the `max()` function with a `key` parameter to find the highest value based on the second element of each tuple.

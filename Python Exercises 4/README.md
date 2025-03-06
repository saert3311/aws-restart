# Python Exercises 4 - Comprehensive

## Exercise 1: Shopping List Manager
Create a **shopping list manager** that allows users to maintain a grocery list with prices. The program should:

1. Start with an **empty dictionary** for the shopping list (**items as keys, prices as values**).
2. Present a **menu** to the user with options:
   - **(a) Add item**: Prompt for item name and price, add to dictionary.
   - **(b) Remove item**: Prompt for item name and remove from dictionary.
   - **(c) View list**: Display all items and prices in a readable format.
   - **(d) Calculate total**: Show the sum of all prices.
   - **(e) Exit**: End the program.
3. After each operation, **show the menu again** until the user chooses to exit.
4. **Include input validation** to ensure prices are positive numbers.

**Hint:**  
- Use a `while` loop for the menu.  
- Use conditionals for each option.  
- Use appropriate dictionary methods for adding, removing, and displaying items.  

---

## Exercise 2: Student Grade Analyzer
Create a program that **analyzes student grades** for multiple subjects. The program should:

1. Ask the user to input the **number of students**.
2. For each student:
   - Ask for the **student's name**.
   - Create a **dictionary** for that student with **subject names as keys** and **grades as values**.
   - Ask for the **number of subjects**.
   - For each subject, ask for the **subject name and grade (0-100)**.
3. After all data is collected, the program should **calculate and display**:
   - Each student's **average grade** across all subjects.
   - The **highest scoring student** for each subject.
   - The **overall class average**.
   - A **list of students with failing grades** (below **60**) in any subject.

**Hint:**  
- Use **nested dictionaries** for storing student data.  
- Use **lists and loops** for input collection.  
- Use **conditionals** for analysis and determining failing grades.  

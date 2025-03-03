# Python Exercises 2 - Conditionals

## Basic Exercises (1-3)

### Exercise 1: Simple Comparison
Create two variables with different numeric values. Write a conditional statement that prints `"Greater"` if the first value is greater than the second, and `"Less or Equal"` otherwise.

### Exercise 2: String Equality
Create a variable containing a color. Write a conditional statement that prints `"My favorite color!"` if the color is `"blue"`, and `"Nice color"` otherwise.

### Exercise 3: Multiple Conditions
Create variables for temperature and weather (sunny/rainy). Write conditional statements that recommend what to wear based on the conditions:

- If it's **sunny** and over **20°C**: `"T-shirt and shorts"`
- If it's **sunny** and under **20°C**: `"Light jacket"`
- If it's **rainy** and over **15°C**: `"Rain jacket"`
- If it's **rainy** and under **15°C**: `"Coat and umbrella"`

---

## Advanced Exercises (4-6)

### Exercise 4: Nested Conditionals
Create variables for a username and password. Write nested conditional statements that:

1. First check if the username is correct.  
2. If the username is correct, then check if the password is correct.  
3. Print appropriate messages for each case:  
   - `"Correct credentials"` if both are correct.  
   - `"Incorrect password"` if only the username is correct.  
   - `"Incorrect username"` if the username is incorrect.  

### Exercise 5: Logical Operators
Ask the user for their age and whether they have a membership (yes/no). Write a conditional statement using logical operators (`and`, `or`, `not`) that determines their ticket price based on:

- **Children (under 12)** pay **$5**  
- **Seniors (65 or older)** pay **$8**  
- **Members** pay **$10**  
- **Everyone else** pays **$15**  

Print the appropriate ticket price.  

**Hint:** Convert the membership input to a boolean using:  
```python
is_member = (membership.lower() == "yes")
```
### Exercise 6: Ternary Conditional Expressions
Ask the user for a product price and whether it's on sale (yes/no). Use a ternary conditional expression to calculate the final price (25% off if on sale). Print both the original and final price.

**Hint:** A ternary expression in Python has the form:

```python
value_if_true if condition else value_if_false
```
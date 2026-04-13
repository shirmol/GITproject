def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# בדיקה קצרה
num = 10
if is_even(num):
    print(f"The number {num} is even!")
else:
    print(f"The number {num} is odd.")
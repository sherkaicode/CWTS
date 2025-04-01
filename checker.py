# checker.py (hidden from students)
import keyword
import numpy as np
correct_answers = np.genfromtxt("Answers/Intro_Python.csv", delimiter=",", dtype=None, encoding="utf-8",  names=True)
def checker_ans(user_func, num, score):
    if num < 17:
        if str(user_func).strip().upper() == str(correct_answers[num-1][1]).strip().upper():
            score[f"{num}"] = 1
            return "Correct! Proceed to the next question"
        else:
            score[f"{num}"] = 0
            return "Try again"
    elif num == 17:
        try:
            result = user_func()
            score[f"{num}"] = 0
            # Check if the result is 42
            assert result == 42, "❌ Incorrect"

            # Ensure the user used a valid variable name
            assert isinstance(result, int), "❌ Ensure you assign an integer."

            print("✔️ Well done!")
            score[f"{num}"] = 1
        except AssertionError as e:
            print(e)
    elif num == 18:
        try:
        # Check if the class exists
            user_class = user_func()
            score[f"{num}"] = 0
            assert hasattr(user_class, "greet"), "❌ The class must have a method named 'greet'."

            # Create an instance of the class
            obj = user_class()

            # Ensure greet() is callable
            assert callable(getattr(obj, "greet")), "❌ 'greet' must be a method."

            # Check if greet() returns "Hello"
            assert obj.greet() == "Hello", "❌ 'greet()' must return 'Hello'."

            print("✔️ Well done!")
            score[f"{num}"] = 1

        except AssertionError as e:
            print(e)
    elif num == 19:
        user_func = user_func()
        try:
            score[f"{num}"] = 0
        # Ensure the function is callable
            assert callable(user_func), "❌ You must define a function."

        # Check the return value
            assert user_func() == "Whatt", "❌ The function must return the string 'Whatt'."

            print("✔️ Well done!")
            score[f"{num}"] = 1

        except AssertionError as e:
            print(e)
    elif num == 20:
        try:
            score[f"{num}"] = 0
            user_list = user_func()
        # Expected output
            expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

        # Check if the answer is a list
            assert isinstance(user_list, list), "❌ Your answer must be a list."

        # Check if it contains exactly one element, which should also be a list
            assert len(user_list) == 1 and isinstance(user_list[0], list), "❌ The list must contain exactly one nested list."

        # Check if the inner list is sorted correctly from 1 to 10
            assert user_list[0] == expected[0], "❌ The inner list must contain numbers from 1 to 10 in sorted order."

            print("✔️ Well done!")
            score[f"{num}"] = 1

        except AssertionError as e:
            print(e)
    else:
        print("Something is wrong")

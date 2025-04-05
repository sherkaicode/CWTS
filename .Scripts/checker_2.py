def check(num, answer, score):
    def wrong(reason = "Wrong, Try again"):
        score[f"{num}"] = 0
        return reason

    def correct():
        score[f"{num}"] = 1
        return "Correct, proceed to the next num"

    if num == 1:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip() == "No" else wrong()

    elif num == 2:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip() == "False" else wrong()

    elif num == 3:
        if not isinstance(answer, bool): return wrong("Answer must be a boolean")
        return correct() if answer is True else wrong()

    elif num == 4:
        if not isinstance(answer, bool): return wrong("Answer must be a boolean")
        return correct() if answer is False else wrong()

    elif num == 5:
        if not isinstance(answer, bool): return wrong("Answer must be a boolean")
        return correct() if answer is True else wrong()

    elif num == 6:
        if not isinstance(answer, bool): return wrong("Answer must be a boolean")
        return correct() if answer is False else wrong()

    elif num == 7:
        if not isinstance(answer, list): return wrong("Answer must be a list")
        return correct() if answer == [1, 3] else wrong()

    elif num == 8:
        if not isinstance(answer, list): return wrong("Answer must be a list")
        return correct() if answer == [0, 2, 2, 6, 4] else wrong()

    elif num == 9:
        if not isinstance(answer, list): return wrong("Answer must be a list")
        return correct() if answer == [5, 4, 3, 2, 1] else wrong()

    elif num == 10:
        if not isinstance(answer, list): return wrong("Answer must be a list")
        return correct() if answer == [0, 1] else wrong()

    elif num == 11:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip() == "B" else wrong()

    elif num == 12:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip().upper() == "D" else wrong()

    elif num == 13:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip().upper() == "D" else wrong()

    elif num == 14:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip() == "Ha?" else wrong()

    elif num == 15:
        if not isinstance(answer, list): return wrong("Answer must be a list")
        return correct() if answer == [1, 3, 4, 5] else wrong()

    elif num == 16:
        if not isinstance(answer, str): return wrong("Answer must be a string")
        return correct() if answer.strip().upper() == "B" else wrong()

    elif num == 17:
        try:
            if not callable(answer): return wrong("Answer must be a function")
            test = [3, 1, 2, 3, 1]
            output = answer(test)
            if output != [1, 2, 3]: return wrong()
            return correct()
        except:
            return wrong("Function failed")

    elif num == 18:
        try:
            if not isinstance(answer, list): return wrong("Answer must be a list of lists")
            flat = [i for row in answer for i in row]
            if len(answer) != 5 or any(len(row) != 5 for row in answer): return wrong("Matrix must be 5x5")
            for i, val in enumerate(flat):
                if i % 3 == 0 and val != "X": return wrong("Expected 'X'")
                elif i % 3 != 0 and val != i: return wrong(f"Expected {i}, got {val}")
            return correct()
        except:
            return wrong("Matrix logic error")

    elif num == 19:
        try:
            if not callable(answer): return wrong("Answer must be a function")
            test_cases = {
                15: "FizzBuzz",
                9: "Fizz",
                10: "Buzz",
                7: "Prime",
                -2: "Negative",
                8: "Other"
            }
            for n, expected in test_cases.items():
                if answer(n) != expected:
                    return wrong(f"Expected {expected} for {n}")
            return correct()
        except:
            return wrong("Function error")

    elif num == 20:
        try:
            if not callable(answer): return wrong("Answer must be a function")
            test_input = list(range(11))
            expected = test_input[1:9:2] + test_input[-4:][::-1] + test_input[2::-1]
            if answer(test_input) != expected:
                return wrong("Incorrect output for slice logic")
            return correct()
        except:
            return wrong("Function failed")

    return "Wrong, Try again"

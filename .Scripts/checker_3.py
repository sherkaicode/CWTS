import numpy as np
def check(num, answer, score):
    def wrong(num, reason = "Wrong, Try again"):
        score[f"{num}"] = 0
        return reason

    def correct(num):
        score[f"{num}"] = 1
        return "Correct, proceed to the next num"
    if num == 1:
        # Check type 
        if not isinstance(answer, bool): return wrong(num, "Answer must be a boolean")
        return correct(num) if answer == False else wrong(num)
    
    elif num == 2:
        # Check type
        if not isinstance(answer, bool): return wrong(num, "Answer must be a boolean")
        return correct(num) if answer == True else wrong(num)
    
    elif num == 3:
        # Check type
        if not isinstance(answer, bool): return wrong(num, "Answer must be a boolean")
        return correct(num) if answer == True else wrong(num)
        
    elif num == 4:
        # Check type
        if not isinstance(answer, np.ndarray): return wrong(num, "Answer must be a NumPy array")
        if answer.shape != (5, 5): return wrong(num, "Wrong shape, try again")
        if not np.all(np.isin(answer, np.arange(0, 21, 5))): return wrong(num)
        np.random.seed(5)
        expected_array = np.random.choice(list(np.arange(0, 21, 5)), size=(5, 5))
        return correct(num) if np.array_equal(answer, expected_array) else wrong(num, "Array does not match expected random generation.")
        
    elif num == 5:
        # Check type
        if not isinstance(answer, list): return wrong(num, "Answer must be a list")
        return correct(num) if np.array_equal(answer, [20, 40]) else wrong(num)
    elif num == 6:
        # Check type
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)
        
    elif num == 7:
        # Check type
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "A" else wrong(num)
        
    elif num == 8:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)
        
    elif num == 9:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)
    
    elif num == 10:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)
        
    elif num == 11:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)
    
    elif num == 12:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "A" else wrong(num)
    
    elif num == 13:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)
        
    elif num == 14:
        if not callable(answer): return wrong(num, "Answer must be a function")
        sinvals = answer()
        angles_ans = np.array([0, np.pi / 2, np.pi])
        sine_values_ans = np.sin(angles_ans)
        return correct(num) if np.array_equal(sinvals, sine_values_ans) else wrong(num)
        
    elif num == 15:
        if not callable(answer): return wrong(num, "Answer must be a function")
        exp_vals = answer()
        x_ans = np.linspace(-5, 5, 1)
        exp_values_ans = np.exp(x_ans)
        return correct(num) if np.array_equal(exp_vals, exp_values_ans) else wrong(num)
        
    elif num == 16:
        if not callable(answer): return wrong(num, "Answer must be a function")
        tests = [1, np.pi, 4, 2*np.pi]
        tests_true = [False, False, True, True]
        return correct(num) if (np.sum([answer(tests[i]) == tests_true[i] for i in range(len(tests))]) == 4) else wrong(num)
        
    elif num == 17: 
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "YES" else wrong(num)
        
    elif num == 18:
        # Check type
        if isinstance(answer, tuple): return wrong(num, "Try looking at the variable and see what you need")
        if not isinstance(answer, np.ndarray): return wrong(num, "Answer must be a NumPy Array")
        arr_ans = np.array([1, 5, 3, 5, 2])
        ans = np.where(arr_ans == 5)[0]
        return correct(num) if np.array_equal(answer, ans) else wrong(num)
        
    elif num == 19:
        # Check type
        if not isinstance(answer, np.ndarray): return wrong(num, "Answer must be a NumPy Array")
        ans = np.zeros((5, 5), dtype=int)
        np.fill_diagonal(ans, 9)
        return correct(num) if np.array_equal(answer, ans) else wrong(num)

    elif num == 20:
        if not callable(answer): return wrong(num, "Answer must be a function")
        a = np.array([1, 2, 3])
        b = np.array([2, 3, 4])
        ans = answer(a, b)
        a1 = np.array([1, 2, 3])
        b1 = np.array([1, 2])
        ans1 = answer(a1, b1)
        return correct(num) if np.array_equal(ans, a+b) and ans1.upper() == "INVALID" else wrong(num)
        
        
        

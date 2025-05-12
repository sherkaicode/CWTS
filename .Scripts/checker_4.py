import numpy as np
import importlib
import matplotlib.pyplot as plt
import os

def checker_ans(answer, num, score):
    def wrong(num, reason="Wrong, Try again"):
        score[f"{num}"] = 0
        return reason

    def correct(num):
        score[f"{num}"] = 1
        return "Correct, proceed to the next num"

    # True/False Questions
    if num == 1:
        if not isinstance(answer, bool): return wrong(num, "Answer must be a boolean")
        return correct(num) if answer == False else wrong(num)

    elif num == 2:
        if not isinstance(answer, bool): return wrong(num, "Answer must be a boolean")
        return correct(num) if answer == False else wrong(num)

    elif num == 3:
        if not isinstance(answer, bool): return wrong(num, "Answer must be a boolean")
        return correct(num) if answer == True else wrong(num)

    # Multiple Choice (as string input)
    elif num == 4:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "B" else wrong(num)

    elif num == 5:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "A" else wrong(num)

    elif num == 6:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.upper() == "C" else wrong(num)

    elif num == 7:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.lower() == "b" else wrong(num)

    elif num == 8:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.lower() == "c" else wrong(num)

    elif num == 9:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.lower() == "b" else wrong(num)

    elif num == 10:
        if not isinstance(answer, str): return wrong(num, "Answer must be a string")
        return correct(num) if answer.lower() == "b" else wrong(num)

    # Code-based Tasks
    elif num == 11:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()  # Clear any existing plots
            answer()   # Call the user function
            ax = plt.gca()
            collections = ax.collections
            if len(collections) == 0:
                return wrong(num, "No scatter plot found")
            offsets = collections[0].get_offsets()
            expected = np.array([[1, 4], [2, 5], [3, 6]])
            return correct(num) if np.array_equal(offsets, expected) else wrong(num, "Scatter data is incorrect")
        except Exception as e:
            return wrong(num, f"Error while plotting: {e}")

    elif num == 12:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()  # Clear figure
            answer()   # Call the user's plotting function

            # Get current axes and title
            ax = plt.gca()
            title = ax.get_title()
            if title != "Sine wave.":
                return wrong(num, f"Title must be 'Sine wave.', but got '{title}'")

            # Check if any lines were plotted
            lines = ax.get_lines()
            if not lines:
                return wrong(num, "No line plot found")

            # Verify the y-values match a sine function
            x_data = lines[0].get_xdata()
            y_data = lines[0].get_ydata()

            expected_y = np.sin(x_data)
            if len(y_data) != len(expected_y):
                return wrong(num, "Sine wave y-data length mismatch")

            if not np.allclose(y_data, expected_y, atol=0.01):
                return wrong(num, "y-values do not match sine wave")

            return correct(num)

        except Exception as e:
            return wrong(num, f"Error while plotting: {e}")

    elif num == 13:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()

            ax = plt.gca()
            lines = ax.get_lines()
            if not lines:
                return wrong(num, "No line found in the plot")

            line = lines[0]

            # Check color
            color = line.get_color()
            if color != 'red' and color.lower() != '#ff0000':
                return wrong(num, f"Line color is not red, found: {color}")

            # Check linewidth
            lw = line.get_linewidth()
            if lw != 3:
                return wrong(num, f"Line width is not 3, found: {lw}")

            return correct(num)
        except Exception as e:
            return wrong(num, f"Error while plotting: {e}")


    elif num == 14:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()

            ax = plt.gca()
            bars = ax.patches  # Bar containers
            if not bars or len(bars) != 3:
                return wrong(num, "Expected 3 bars, but got a different number")

            heights = [bar.get_height() for bar in bars]
            expected_heights = [91, 85, 79]
            if not np.allclose(heights, expected_heights):
                return wrong(num, f"Bar heights do not match expected scores: {heights}")

            labels = [tick.get_text() for tick in ax.get_xticklabels()]
            expected_labels = ["Puffy", "Jelly", "Judy"]
            if not all(name in labels for name in expected_labels):
                return wrong(num, f"x-axis labels do not match expected names: {labels}")

            return correct(num)
        except Exception as e:
            return wrong(num, f"Error while plotting: {e}")

    elif num == 15:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()

            saved_file = None  # to store captured filename

            # Wrap plt.savefig to capture filename
            original_savefig = plt.savefig
            def savefig_wrapper(fname, *args, **kwargs):
                nonlocal saved_file
                saved_file = fname
                return original_savefig(fname, *args, **kwargs)
            plt.savefig = savefig_wrapper

            answer()  # run the student's function

            # Restore the original savefig
            plt.savefig = original_savefig

            if not saved_file:
                return wrong(num, "plt.savefig was not called")

            if not os.path.exists(saved_file):
                return wrong(num, f"File {saved_file} was not created")

            if saved_file != "output.png":
                os.remove(saved_file)
                return wrong(num, f"Expected filename 'output.png' but got '{saved_file}'")

            os.remove(saved_file)
            return correct(num)

        except Exception as e:
            # Cleanup if anything was saved
            if saved_file and os.path.exists(saved_file):
                os.remove(saved_file)
            return wrong(num, f"Error while executing: {e}")

    elif num == 16:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()
            if not callable(plt.title):
                importlib.reload(plt)
                return wrong(num, "The title is wrong")
            else:
                return correct(num)
        except Exception as e:
            return f"Error while running your code: {e}"

    elif num == 17:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()
            return correct(num)
        except Exception as e:
            return f"Error while running your code: {e}"

    elif num == 18:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()
            return correct(num)
        except Exception as e:
            return f"Error while running your code: {e}"

    elif num == 19:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()
            if not callable(plt.xlabel):
                importlib.reload(plt)
                return wrong(num, "The label is wrong")
            else:
                return correct(num)
        except Exception as e:
            return f"Error while running your code: {e}"

    elif num == 20:
        if not callable(answer): return wrong(num, "Answer must be a function")
        try:
            plt.clf()
            answer()
            return correct(num)
        except Exception as e:
            return f"Error while running your code: {e}"


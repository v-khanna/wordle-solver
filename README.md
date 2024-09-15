# Wordle Solver with GUI

A Python-based Wordle solver application featuring a graphical user interface (GUI) built with Tkinter. This application allows users to solve Wordle puzzles efficiently by suggesting optimal guesses based on previous feedback. Users can enter their own guesses or let the algorithm suggest the best possible next guess.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run the Application](#how-to-run-the-application)
- [How to Use the Wordle Solver](#how-to-use-the-wordle-solver)
- [Customization](#customization)
- [Credits](#credits)
- [License](#license)

## Features

- **Graphical User Interface**: Intuitive GUI using Tkinter for easy interaction.
- **Wordle Solver Algorithm**: Efficient algorithm to suggest optimal guesses based on feedback.
- **Manual or Suggested Guesses**: Users can input their own guesses or use the algorithm's suggestions.
- **Feedback Processing**: Accepts feedback in the form of 'g' (green), 'y' (yellow), and '_' (gray) to filter possible words.
- **Possible Words Display**: Shows the number of possible words remaining and lists them when few are left.
- **Reset Functionality**: Easily reset the solver to start a new game.

## Project Structure

    wordle-solver/
    ├── data/
    │   └── word_list.txt
    ├── src/
    │   ├── __init__.py
    │   ├── gui.py
    │   └── solver.py
    ├── main.py
    └── README.md

- **`data/word_list.txt`**: Contains the list of acceptable 5-letter words.
- **`src/__init__.py`**: Indicates that `src` is a Python package.
- **`src/gui.py`**: Contains the GUI code (`WordleSolverApp` class).
- **`src/solver.py`**: Contains the Wordle solving logic (`WordleSolver` class).
- **`main.py`**: The main script to run the application.
- **`README.md`**: Project documentation.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **Tkinter**: Tkinter comes pre-installed with most Python distributions. If not, you may need to install it separately.

### Steps

1. **Clone or Download the Repository**

   Clone the repository or download the source code into a directory on your computer.

2. **Prepare the Word List**

   Ensure that you have a `word_list.txt` file containing acceptable 5-letter words in the `data/` directory. Each word should be on a separate line, in lowercase, with no extra spaces.

3. **Install Required Packages**

   The application uses standard Python libraries. No additional packages are required.

## How to Use the Wordle Solver

### Making Your Own Guesses

1. **Enter Your Guess**

   In the "Enter your guess:" field, type a valid 5-letter word.

2. **Submit Your Guess**

   Click the **"Submit Guess"** button. Your guess will be recorded.

3. **Enter Feedback**

   In the "Enter feedback:" field, input the feedback received from the Wordle game using:

   - **'g'** for a correct letter in the correct position (green).
   - **'y'** for a correct letter in the wrong position (yellow).
   - **'_'** for an incorrect letter (gray).

   Example feedback: `g_y__`

4. **Submit Feedback**

   Click the **"Submit Feedback"** button. The solver will process the feedback and update the possible words.

### Using Algorithm Suggestions

1. **Get a Suggested Guess**

   Click the **"Suggest Guess"** button. The algorithm will provide the best next guess based on current information.

2. **Submit the Suggested Guess**

   The suggested word will appear in the guess entry field. Click **"Submit Guess"** to submit it.

3. **Enter and Submit Feedback**

   Provide the feedback from the Wordle game as described above.

### Viewing Algorithm Details

- The text area at the bottom of the GUI displays:

  - Each attempt and the guess submitted.
  - Feedback received for each guess.
  - The number of possible words remaining.
  - A list of possible words when few remain.

### Resetting the Solver

- Click the **"Reset Solver"** button at any time to start a new game.

## Customization

You can customize various aspects of the application:

- **Word List**

  - Update the `word_list.txt` file in the `data/` directory with your own list of 5-letter words.

- **Algorithm Enhancements**

  - Modify `solver.py` to implement more advanced algorithms for suggesting guesses.

- **GUI Adjustments**

  - Customize the GUI appearance and functionality by modifying `gui.py`.

## Credits

- **Developer**: Vir Khanna

## License

This project is licensed under the MIT License.

---

**Enjoy using the Wordle Solver! If you have any questions or need further assistance, feel free to reach out.**
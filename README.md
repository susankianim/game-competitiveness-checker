# Game Competitiveness Checker

**Game Competitiveness Checker** is a Python tool that determines whether a two-player matrix game is *strictly competitive* by analyzing utility matrices in strategic form. It uses two sorting algorithms: Merge Sort (optimized for time complexity) and Merge Insertion Sort (optimized for fewer comparisons). The project supports both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter, and includes a standalone `.exe` for Windows users.

## How It Works
1. **Input**: Provide the number of actions for Player 1 (rows) and Player 2 (columns), then enter two utility matrices.
2. **Processing**: Converts matrices to strategic form, sorts payoff tuples using the chosen algorithm (Merge Sort for speed, Merge Insertion Sort for minimal comparisons), and analyzes competitiveness.
3. **Output**: 
   - CLI: Prints result and sorted payoffs to the console.
   - GUI: Shows result in a message box, with sorted payoffs in the console.

## Installation

### Running from Source
1. Clone the repository:
   ```bash
   git clone https://github.com/susankianim/game-competitiveness-checker.git
   cd game-competitiveness-checker
   ```
2. Run in GUI mode (default):
   ```bash
   python main.py
   ```
3. Run in CLI mode:
   ```bash
   python main.py --mode cli
   ```

### Using the Executable
1. Download `game-competitiveness-checker.exe` from the [Releases](https://github.com/susankianim/game-competitiveness-checker/releases) page.
2. Double-click to run (Windows, GUI mode only).

## Usage

### CLI Mode
1. Run `python main.py --mode cli`.
2. Enter the number of actions for Player 1 and Player 2.
3. Choose a sorting method (1 for Merge Sort, 2 for Merge Insertion Sort).
4. Input utility matrices row by row (space-separated integers).
5. View the result and sorted payoff tuples in the terminal.

**Example:**
```
Enter the number of actions for Player 1: 2
Enter the number of actions for Player 2: 2
Enter the utility matrix for Player 1:
Row 1: 1 0
Row 2: 0 1
Enter the utility matrix for Player 2:
Row 1: 0 1
Row 2: 1 0
Choose a sorting function: (1) Merge Sort (2) Merge-Insertion Sort
Enter 1 or 2: 1
Game is strictly competitive! (5 comparisons)
Sorted Payoff Tuples:
(0, 1)
(0, 1)
(1, 0)
(1, 0)
```

### GUI Mode
1. Run `python main.py` or the `.exe`.
2. Enter the number of actions for Player 1 and Player 2.
3. Select a sorting method via radio buttons (Merge Sort for speed, Merge Insertion Sort for fewer comparisons).
4. Click "Create Matrices" to generate input fields.
5. Fill in the utility matrices.
6. Click "Submit" to see the result in a popup and sorted payoffs in the console.

**Example:** Same 2x2 game as above yields "Strictly Competitive".

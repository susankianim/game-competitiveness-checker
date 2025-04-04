import argparse
from gui import MatrixGUI
import tkinter as tk
from logic import process_matrices
from merge_sort import merge_sort
from merge_insertion_sort import merge_insertion_sort
from PayoffTuple import PayoffTuple

def get_matrix(rows, cols, player):
    print(f"Enter the utility matrix for Player {player}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Invalid row length. Please re-enter.")
            return get_matrix(rows, cols, player)
        matrix.append(row)
    return matrix

def run_cli():
    print("Game Competitiveness Checker (CLI Mode)")

    rows = int(input("Enter the number of actions for Player 1: "))
    cols = int(input("Enter the number of actions for Player 2: "))

    matrix1 = get_matrix(rows, cols, 1)
    matrix2 = get_matrix(rows, cols, 2)

    print("Choose a sorting function: (1) Merge Sort (2) Merge-Insertion Sort")
    choice = input("Enter 1 or 2: ")
    sort_function = merge_sort if choice == "1" else merge_insertion_sort

    result, sorted_payoffs = process_matrices(matrix1, matrix2, sort_function)

    print("\n" + result)
    if sorted_payoffs:
        print("Sorted Payoff Tuples:")
        for p in sorted_payoffs:
            print(p)

def run_gui():
    root = tk.Tk()
    app = MatrixGUI(root)
    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game Competitiveness Checker")
    parser.add_argument("--mode", choices=["cli", "gui"], default="gui", help="Choose mode: cli (command-line) or gui (graphical)")
    args = parser.parse_args()

    if args.mode == "cli":
        run_cli()
    else:
        run_gui()

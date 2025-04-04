import tkinter as tk
from tkinter import messagebox, ttk
from logic import process_matrices
from merge_sort import merge_sort
from merge_insertion_sort import merge_insertion_sort


class MatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Competitiveness Checker (GUI Mode)")
        self.root.geometry("700x700")
        self.root.configure(bg="#f0f0f0")

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=5)
        style.configure("TLabel", font=("Helvetica", 11), background="#f0f0f0")

        self.sort_method = tk.StringVar(value="merge_sort")  # Default to Merge Sort
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)

        dim_frame = ttk.LabelFrame(main_frame, text="Number of Actions", padding="10")
        dim_frame.pack(fill="x", pady=(0, 10), padx=20)

        dim_inner = ttk.Frame(dim_frame)
        dim_inner.pack(expand=True)

        ttk.Label(dim_inner, text="Number of actions of player 1:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.entry_m = ttk.Entry(dim_inner, width=10)
        self.entry_m.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(dim_inner, text="Number of actions of player 2:").grid(
            row=1, column=0, padx=5, pady=5
        )
        self.entry_n = ttk.Entry(dim_inner, width=10)
        self.entry_n.grid(row=1, column=1, padx=5, pady=5)

        # Radio buttons for sort method
        sort_frame = ttk.LabelFrame(main_frame, text="Sort Method", padding="10")
        sort_frame.pack(fill="x", pady=(0, 10), padx=20)
        ttk.Radiobutton(
            sort_frame,
            text="Merge Sort",
            variable=self.sort_method,
            value="merge_sort"
        ).pack(side="left", padx=5)
        ttk.Radiobutton(
            sort_frame,
            text="Merge Insertion Sort",
            variable=self.sort_method,
            value="merge_insertion_sort"
        ).pack(side="left", padx=5)

        ttk.Button(
            dim_inner,
            text="Create Matrices",
            command=lambda: self.create_matrix_inputs(main_frame),
        ).grid(row=2, column=0, columnspan=2, pady=10)

        self.matrix_frame = None

    def create_matrix_inputs(self, main_frame):
        try:
            m = int(self.entry_m.get())
            n = int(self.entry_n.get())

            if m <= 0 or n <= 0:
                messagebox.showerror("Error", "Dimensions must be positive")
                return

            if self.matrix_frame:
                self.matrix_frame.destroy()

            self.matrix_frame = ttk.LabelFrame(
                main_frame, text="Utility Matrices Input", padding="10"
            )
            self.matrix_frame.pack(fill="both", expand=True, padx=20)

            canvas = tk.Canvas(self.matrix_frame, bg="#f0f0f0")
            v_scrollbar = ttk.Scrollbar(
                self.matrix_frame, orient="vertical", command=canvas.yview
            )
            h_scrollbar = ttk.Scrollbar(
                self.matrix_frame, orient="horizontal", command=canvas.xview
            )
            scrollable_frame = ttk.Frame(canvas)
            
            def update_scroll_region(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
            
            scrollable_frame.bind("<Configure>", update_scroll_region)
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
            
            v_scrollbar.pack(side="right", fill="y")
            h_scrollbar.pack(side="bottom", fill="x")
            canvas.pack(side="left", fill="both", expand=True)

            matrix_container = ttk.Frame(scrollable_frame)
            matrix_container.pack(expand=True, pady=10)

            ttk.Label(
                matrix_container, text="Matrix 1", font=("Helvetica", 12, "bold")
            ).grid(row=0, column=0, columnspan=n, pady=(0, 10))
            self.matrix1_entries = []
            for i in range(m):
                row = []
                for j in range(n):
                    entry = ttk.Entry(matrix_container, width=8, justify="center")
                    entry.grid(row=i + 1, column=j, padx=2, pady=2)
                    entry.insert(0, "0")
                    row.append(entry)
                self.matrix1_entries.append(row)

            ttk.Label(
                matrix_container, text="Matrix 2", font=("Helvetica", 12, "bold")
            ).grid(row=m + 2, column=0, columnspan=n, pady=(20, 10))
            self.matrix2_entries = []
            for i in range(m):
                row = []
                for j in range(n):
                    entry = ttk.Entry(matrix_container, width=8, justify="center")
                    entry.grid(row=i + m + 3, column=j, padx=2, pady=2)
                    entry.insert(0, "0")
                    row.append(entry)
                self.matrix2_entries.append(row)

            ttk.Button(matrix_container, text="Submit", command=self.get_matrices).grid(
                row=2 * m + 4, column=0, columnspan=n, pady=20
            )

            # Update scroll region after all widgets are added
            self.root.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for m and n")

    def get_matrices(self):
        try:
            m = int(self.entry_m.get())
            n = int(self.entry_n.get())

            matrix1 = [
                [float(self.matrix1_entries[i][j].get()) for j in range(n)]
                for i in range(m)
            ]
            matrix2 = [
                [float(self.matrix2_entries[i][j].get()) for j in range(n)]
                for i in range(m)
            ]

            # Choose sort function based on radio selection
            sort_func = merge_sort if self.sort_method.get() == "merge_sort" else merge_insertion_sort
            # Process the matrices with the selected sort function
            result, sorted_items = process_matrices(matrix1, matrix2, sort_func)

            # Display the result
            messagebox.showinfo("Result", result)
            if sorted_items:
                print("Sorted items:", sorted_items)  # Still prints to console

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")


if __name__ == "__main__":
    root = tk.Tk()
    root.update_idletasks()
    app = MatrixGUI(root)
    root.mainloop()
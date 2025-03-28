from tkinter import *
from tkinter import messagebox, ttk

from file import load_coin_denominations
from denomination import solve_coin_change

class CoinChangeGUI:
    def __init__(self, root, coin_data):
        self.root = root
        self.root.title("Coin Change Solver")
        self.root.geometry("800x600")
        self.coin_data = coin_data
        
        # GUI Setup
        Label(root, text="Coin Change Solver", font=("Arial", 14)).pack(pady=10)
        
        Label(root, text="Select Country:").pack()
        self.country_var = StringVar()
        self.country_combo = ttk.Combobox(root, textvariable=self.country_var)
        self.country_combo['values'] = list(self.coin_data.keys())
        self.country_combo.pack(pady=5)
        
        Label(root, text="Enter Target Amount:").pack()
        
        # Validation function for numerical input
        validate_command = root.register(self.validate_decimal_input)
        self.target_entry = Entry(root, validate="key", validatecommand=(validate_command, '%P'))
        self.target_entry.pack(pady=5)
        
        Button(root, text="Calculate", command=self.calculate).pack(pady=10)
        
        self.result_text = Text(root, height=15, width=70)
        self.result_text.pack(pady=10)
    
    # validate decimal input
    def validate_decimal_input(self, input_value):
        if input_value == "": # Allow empty input
            return True
        try:
            # Check if the input is a valid float
            value = float(input_value)
            # Check if it has at most 2 decimal places
            if '.' in input_value and len(input_value.split('.')[-1]) > 2:
                return False
            return True
        except ValueError:
            return False
    
    # validate user input
    def validate_input(self, country, target_str):
        if not country:
            raise ValueError("Please select a country!")
        if not target_str:
            raise ValueError("Please enter a target amount!")
        try:
            target = float(target_str)
            if target <= 0:
                raise ValueError("Please enter a positive amount!")
            return target
        except ValueError as e:
            if str(e) == "Please enter a positive amount!":
                raise
            raise ValueError("Please enter a valid number!")
    
    # calculate coin change
    def calculate(self):
        self.result_text.delete(1.0, END)
        
        try:
            country = self.country_var.get()
            target_str = self.target_entry.get()
            target = self.validate_input(country, target_str)
            
            result, _ = solve_coin_change(country, target, self.coin_data)
            self.result_text.insert(END, result)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def main():
    def initialize_gui():
        # Setup GUI
        root = Tk()
        coin_data = load_coin_denominations()
        if not coin_data:
            messagebox.showerror("Error", "Failed to load coin data. Exiting...")
            root.destroy()
            return None
        app = CoinChangeGUI(root, coin_data)
        return root, app
    
    try:
        gui_setup = initialize_gui()
        if gui_setup:
            root, _ = gui_setup
            root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to initialize program: {str(e)}")

if __name__ == "__main__":
    main()
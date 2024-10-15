# Python-Gui_Calculator

A simple yet powerful Python-based GUI calculator built using the Tkinter library. This calculator supports all basic arithmetic operations, along with additional features such as clearing the display, handling errors, and displaying results in a message box.

## Features

- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, and Division.
- **Advanced Functions**: Percentage, Square, and Square Root.
- **Clear Entry**: Allows you to clear the current input.
- **Error Handling**: Handles divide-by-zero errors and other invalid inputs, displaying appropriate message boxes.
- **Message Box**: Displays results, error messages, and confirmations using message boxes.
- **User-Friendly GUI**: Easy-to-use buttons and display area for seamless user experience.

## Screenshots


![calculator_upload](https://github.com/user-attachments/assets/e70718fb-9b0a-4966-abe8-2c780d8998be)


*Figure 1: Calculator interface showing basic operations.*

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/python-gui-calculator.git
   cd python-gui-calculator
   ```

2. Install the necessary dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: This project uses Python's built-in Tkinter module, so no additional libraries are required for the GUI.

3. Run the `calculator.py` script:
   ```bash
   python calculator.py
   ```

## How to Use

1. **Perform Calculations**:  
   - Click the numeric buttons to enter numbers.
   - Use the operator buttons (`+`, `-`, `*`, `/`) for basic operations.
   - Use the `=` button to evaluate the result.
   
2. **Clear Display**:  
   - Click `AC` to clear the entire display.

3. **Advanced Functions**:  
   - Use `%` for percentage calculations.
   - Use `√` for square roots, `x²` for squares
   
4. **Error Handling**:  
   - If you attempt to divide by zero, an error message will appear in a pop-up message box.
   - Invalid inputs or operations will trigger appropriate error messages.

## Code Structure

- `calculator.py`: The main Python script containing the logic for the calculator.
- `README.md`: This documentation file.
- `images/`: Folder containing images/screenshots of the calculator.

## Message Box Usage

- The application utilizes `messagebox.showinfo()` and `messagebox.showerror()` to display results and error messages.
- Example:
  - On a successful calculation, a message box displays the result.
  - On an error (e.g., dividing by zero), a message box alerts the user with an error message.

## Future Enhancements

- Add more advanced mathematical functions (e.g., trigonometric functions, logarithms).
- Implement a history feature to keep track of previous calculations.
- Add themes or skins to enhance the visual appearance.

## Contributing

If you'd like to contribute to this project, please feel free to open a pull request or issue.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

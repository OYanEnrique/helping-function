# 🐍 PyHELP - Interactive Help System

A user-friendly, interactive command-line tool that provides a colorful interface for Python's built-in `help()` system. Users can type any function or module name to view its official documentation directly in the terminal.

## Features

* **Interactive Help**: Look up documentation for any Python command (e.g., `print`, `list`, `random`) without leaving the terminal.
* **Colorized UI**: Uses ANSI escape codes to create a colorful and visually appealing interface with custom titles, making the output easy to read.
* **Modular Functions**: The code is organized into reusable functions for displaying titles (`title()`) and fetching help (`helping()`).
* **Looping Input**: Allows the user to look up multiple commands in a single session.

## How to Use

1.  Ensure you have a terminal that supports ANSI color codes (most modern terminals do).
2.  Save the code as a `.py` file (e.g., `pyhelp.py`).
3.  Run the script from your terminal:
    ```sh
    python pyhelp.py
    ```
4.  The program will display a green title and prompt you to enter a function name.
5.  Type the name of any Python function or module and press Enter.
6.  The script will display the official help documentation for that command.
7.  To exit the program, type `END` at the prompt.

### Example Session

```sh
> python pyhelp.py
~~~~~~~~~~~~~~~~~~~~~~
  HELP SYSTEM PyHELP
~~~~~~~~~~~~~~~~~~~~~~
Enter the name of the function!
list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Accessing the command manual 'list' 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
...

~~~~~~~~~~~~~~~~~~~~~~
  HELP SYSTEM PyHELP
~~~~~~~~~~~~~~~~~~~~~~
Enter the name of the function!
END
Program finished!
~~~~~~~~~~~~~~~~~~
  Until next time!
~~~~~~~~~~~~~~~~~~
```

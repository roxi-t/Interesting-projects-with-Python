# Tic-Tac-Toe Game(exersises-project)

This project is a simple Tic-Tac-Toe game written in Python. You can play against the computer by running this code.

## How to Use

1. **Install Dependencies**

   First, you need to install the `termcolor` library. You can use pip for this:
```shell
   python main.py
```
# Run the Game

After installing the dependencies, you can run the main.py file:
  ```shell
   python main.py
  ```
# How to Play

The player uses the X symbol, and the computer uses the O symbol.
The player should enter a number from 1 to 9 to make a move.
The game continues until either player wins or all spaces are filled

# Code Structure
`print_board`: Prints the game board
`make_move`: Makes a move
`can_move`: Checks if a move is possible
`is_winner`: Checks if a player has won
`has_empty_space`: Checks for empty spaces on the board
`computer_move`: Executes the computer's move
# Example
Here is an example of how the Tic-Tac-Toe game is played:
```shell
Player: X
Computer: O

[1] [2] [3] 

[4] [5] [6] 

[7] [8] [9] 

Choose your move (1-9): 1

[X] [2] [3]

[4] [5] [6]

[7] [8] [9] 
```

# Encryption/Decryption Tool (exersises-project2)

This project is a simple tool for encrypting and decrypting text using a basic algorithm written in Python.

## How to Use

1. **Run the Script**

   Run the `encryption_tool.py` file:
   ```shell
   python encryption_tool.py
   ```
   Options

The script will prompt you to choose an option:
`1` for encryption
`2` for decryption
`3` to exit the program
## Encryption

If you choose `1`, you will be prompted to enter the text you want to encrypt.
The script will encrypt the text using the formula: `x = ord(c) * 2 + 5` for each character `c` in the input text.
The encrypted text will be displayed.
Exit
If you choose `3`, the program will exit with a goodbye message.
# Code Structure
while True:: `Continuously prompts the user to choose an option until they choose to exit.`
if 'y' in Choice.lower():: `Checks if the user wants to start the encryption/decryption process.`
if choice == "1":: `Handles the encryption process.`
if choice == "2":: `Handles the decryption process.`
if choice == "3":: `Exits the program.`
else:: Handles invalid input.
## Example
Here is an example interaction with the encryption/decryption tool:
```shell
Do you want to start? (y/n): y
Enter hour: 0
Enter minutes: 1
Enter seconds: 30
Timer starts now...
90
89
88
...
Timer ended...
Do you want to start? (y/n): y
Choose your option:
    1 (Encrypt)
    2 (Decrypt)
    3 (Exit)
Your Choice: 1
Text: hello
Encrypted Text: ÏÝããØ
****************************************

Choose your option:
    1 (Encrypt)
    2 (Decrypt)
    3 (Exit)
Your Choice: 2
Encrypted Text: ÏÝããØ
Decrypted Text: hello
****************************************

Choose your option:
    1 (Encrypt)
    2 (Decrypt)
    3 (Exit)
Your Choice: 3
Bye!
****************************************
```

### Countdown Timer (exersises-project3)

```markdown
# Countdown Timer
```
This project is a simple countdown timer written in Python. The user can set a specific time duration, and the timer will count down to zero.

## How to Use

1. **Run the Script**

   Run the `timer.py` file:
   ```shell
   python timer.py
   ```
# Set the Timer

The script will prompt you to start the timer.
Enter the hours, minutes, and seconds for the countdown.

# Timer Operation

The timer will display the remaining time and update every second.
The screen will be cleared each second to show the updated time.
When the timer reaches zero, a message will be displayed indicating that the timer has ended.

# Code Structure
The script uses a loop to continuously prompt the user to start the timer or exit.
It calculates the total time in seconds based on user input.
The countdown loop updates the remaining time every second and clears the screen for updated display.
The screen is cleared using the appropriate command for the operating system (`cls` for Windows, `clear` for Unix-based systems).
## Example
Here is an example interaction with the countdown timer:
```shell
Do you want to start? (y/n): y
Enter hour: 0
Enter minutes: 1
Enter seconds: 30
Timer starts now...
90
89
88
...
Timer ended...
```
**I hope you enjoy this project! If you have any questions or feedback, feel free to reach out.**


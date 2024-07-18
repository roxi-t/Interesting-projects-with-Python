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

### Countdown Timer

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


**I hope you enjoy this project! If you have any questions or feedback, feel free to reach out.**


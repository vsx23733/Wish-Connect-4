# Wish-Connect-4
A connect four game in terminal made by little Axel (when I was beginning)
It allows players to play against each other (PvP), against an AI (PvB), or let two AIs compete (BvB). The AI uses the minimax algorithm (not totally effective yet, I was yooung!) to make strategic moves.



## Features

  Player vs. Player (PvP)
  Player vs. AI (PvB)
  AI vs. AI (BvB)
  Gravity mechanics to ensure proper token placement
  AI decision-making using Minimax Algorithm

## Installation
Prerequisites
Ensure you have Python 3 installed along with the necessary dependencies.

Install Dependencies

```pip install numpy```



## How to Run
  Open a terminal or command prompt.

  Navigate to the directory where ConnectAI.py is located.

  Run the script using:
  
  ```python ConnectAI.py```
  
  Follow the on-screen instructions to set up the game mode and play.

  

## Gameplay Modes
  PvP (Player vs. Player) - Two human players take turns.
  
  PvB (Player vs. AI) - A player competes against an AI opponent.
  
  BvB (AI vs. AI) - Two AI players compete automaticall

## Demo

## Example Gameplay

```
Enter the number of rows (n > 4): 6
Enter the number of columns (m > 4): 7
Do you want to play? (y/n): y
Do you want to play against another player? (y/n): n
Enter your name brave player: John
The token @ will be assigned to you
Player vs CPU
```

## AI Behavior

The AI makes decisions using:

  Random moves in early rounds

  Valid move detection

  Minimax Algorithm for optimal decision-making (Note that if you enter the code I let you some space to choice how the AI can behave)



## Future Improvements

  Improve AI difficulty levels

  Enhance UI with a graphical interface



## License

  This project is licensed under the MIT License.



## Author

  Axel (A younger version of me now)



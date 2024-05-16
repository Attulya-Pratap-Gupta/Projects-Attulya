# Klondike Solitaire Python Program

This is a Python program for playing a simplified version of the Klondike solitaire card game. The program manages the game according to specific rules and provides a text-based interface for the user to interact with the game.

## Table of Contents
- [Game Overview](#game-overview)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)

## Game Overview

Klondike is a popular solitaire card game played with a standard 52-card deck. The objective of the game is to build four foundations (one for each suit) from Ace to King, with the Ace as the foundation's bottom card.

In this simplified version of Klondike, the game follows these rules:

1. **Initial Setup**: The deck is shuffled, and 28 cards are dealt into 7 columns to form the tableau. The remaining 24 cards become the stock. The top card in the stock is turned over and placed face up in the waste pile (talon).

2. **Foundation Building**: Aces can be moved to the foundations, followed by cards of the same suit in ascending order (Two on Ace, Three on Two, and so on).

3. **Moving Cards from Waste to Foundation**: Cards from the waste pile can be moved to the foundation if they match the suit and rank criteria.

4. **Moving Cards from Waste to Tableau**: Cards from the waste pile can be moved to the tableau if they match the color and rank criteria.

5. **Moving Cards Within Tableau**: Cards from one column in the tableau can be moved to another column if they match the color and rank criteria.

6. **Empty Columns**: If a tableau column becomes empty, only a King can be moved into that column.

7. **Refilling Stock**: At any point, the player can turn over the top card from the stock and place it face up in the waste pile. When the stock becomes empty, the talon is turned over and becomes the stock.

The program uses a Python module (`cards.py`) to model the cards and deck of cards.

## Game Rules

For detailed game rules and instructions, please refer to the [Game Rules](#game-rules) section in the assignment prompt.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone link
   ```

2. Navigate to the project directory:
   ```bash
   cd klondike-solitaire
   ```

3. Run the program:
   ```bash
   python Klondike.py
   ```

## Usage

Once you have installed the program, follow these steps to play Klondike Solitaire:

1. Run the program using the command mentioned in the installation section.

2. The program will display the current state of the game, including the tableau, stock, foundations, and waste pile.

3. The program will prompt you to enter a command. Available commands are:
   - `SW`: Move one card from the stock to the waste (talon).
   - `WF N`: Move one card from the waste to foundation N.
   - `WT N`: Move one card from the waste to column N in the tableau.
   - `TF N1 N2`: Move one card from column N1 of the tableau to foundation N2.
   - `TT N1 N2`: Move one card from column N1 to column N2 of the tableau.
   - `H`: Display the legal commands.
   - `R`: Restart the game (shuffle the deck).
   - `Q`: Quit the game.

4. Follow the on-screen prompts to enter your desired command and continue playing the game.

5. The program will validate your input and perform the specified moves or display error messages if the moves are invalid.

6. Continue playing until you win the game or decide to quit.

## Code Structure

The code is organized as follows:

- `Klondike.py`: The main Python program that implements the Klondike Solitaire game according to the assignment specifications.

- `README.md`: This README file, providing information about the game, installation instructions, and usage guidelines.

## Contributing

Contributions to this project are welcome. If you have any suggestions or improvements, please open an issue or create a pull request.
New York Stock Exchange Data Handling

This repository contains the source code for focusing on designing, implementing, and testing a Python program that utilizes dictionaries and sets. The program is aimed at processing stock market data from 2010-2016, allowing users to perform various tasks related to the data.

## Assignment Overview

In this project, a Python program reads two files: one containing stock prices with company codes and another containing company information with codes. The program will use dictionaries, sets, and lists to handle and display the data based on user input. The main functionalities include:

1. Opening files for stock prices and company information.
2. Reading and processing the company information file to create a set of company names and a master dictionary.
3. Adding stock price data to the master dictionary.
4. Finding the maximum stock price and its date for a specific company.
5. Finding the company with the highest stock price.
6. Calculating the average high stock price for a specific company.
7. Displaying lists of data in a formatted manner.

## Implementation

The project includes the following functions:

- `open_file()`: Opens the necessary input files and returns file pointers for both.
- `read_file(securities_fp)`: Reads the company information file, creates a set of company names, and builds a master dictionary.
- `add_prices(master_dictionary, prices_file_pointer)`: Adds stock price data to the master dictionary.
- `get_max_price_of_company(master_dictionary, company_symbol)`: Finds the maximum high stock price and its date for a specific company.
- `find_max_company_price(master_dictionary)`: Identifies the company with the highest stock price.
- `get_avg_price_of_company(master_dictionary, company_symbol)`: Calculates the average high stock price for a specific company.
- `display_list(list_of_strings)`: Displays a list of strings in a formatted manner.

The `main()` function is the entry point of the program and allows users to interact with the functionalities mentioned above. Users can choose from various options, such as displaying company information, finding maximum stock prices, calculating averages, and quitting the program.

## Usage

To use the program, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed (preferably Python 3).
3. Run the `proj09.py` file to start the program.
4. Follow the on-screen instructions to interact with the program.


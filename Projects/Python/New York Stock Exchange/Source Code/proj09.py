#############################################################
#
#  Algorithm
#       Importing math and csv library
#       Printing Welcome Banner
#       Calling the open file function to get both file pointers
#       Calling the read_file function to get the master dictionary
#       Calling the add_prices function to add the price list to the master  dictionary
#       Ask the user for an option until he chooses the option 6
#       if user chooses option 1
#           Converting the company names set into a list and sorting the list
#           Call the display function
#       if user chooses option 2
#           Make a list of company symbols and sort them
#           Call the display function
#       if user chooses option 3
#           Input a valid company symbol
#           Call the get_max_price_of_company function
#           Print the highest price and date accordingly
#       if user chooses option 4
#           Call the find_max_company_price function
#           print the company symbol and price accordingly
#       if user chooses option 5
#           Input a valid company symbol
#           Call the get_avg_price_of_company function
#           Print the avg price with appropriate message
#       if user chooses option 6
#           exit 
#       if user chooses option >6
#           print error message
#       Reprompt for option
#############################################################

import csv
#importing csv library
import math
#importing math library
MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''Returns two file pointers for prices and securities respectively
       Displays Error messages if necessary
       Doesn't take any parameters'''

    input_msg_lst = ["\nEnter the price's filename: ", "\nEnter the security's filename: "]
    file_name = input(input_msg_lst[0])
    #asking for file one name
    while True:
        file_name = file_name.lower()
        try:
            file_pointer1 = open(file_name, "r")
            break
        except FileNotFoundError:
            print("\nFile not found. Please try again.")
            #error message if file not present
            file_name = input(input_msg_lst[0])
    file_name = input(input_msg_lst[1])
    #asking for file two name
    while True:
        file_name = file_name.lower()
        try:
            file_pointer2 = open(file_name, "r")
            break
        except FileNotFoundError:
            print("\nFile not found. Please try again.")
            file_name = input(input_msg_lst[1])
    return file_pointer1, file_pointer2
    #returning file pointers

def read_file(securities_fp):
    '''Takes the securities file pointer and returns a set of company names and a master dictionary 
       Doesn't display any error messages'''
    file_reader = csv.reader(securities_fp)
    next(file_reader, None)
    #skipping the header line
    master_dictionary = {}
    #empty dictionary
    company_names_lst = []
    #empty list
    for value in file_reader:
        #reading each line
        company_names_lst.append(value[1])
        iteration_code = value[0]
        #getting the key
        iteration_lst = [value[1], value[3], value[4], value[5], value[6], []]
        #getting the value
        master_dictionary[iteration_code] = iteration_lst
        #adding to dictionary
    final_set = set(company_names_lst)
    return final_set, master_dictionary
    #returning final set and dictionary

def add_prices (master_dictionary, prices_file_pointer):
    '''Adds a price list to the 5th index of master dictionary
       Doesn't return anything
       Takes main dictionary and prices fp as the parameters'''
    file_reader = csv.reader(prices_file_pointer)
    next(file_reader, None)
    #skipping header
    for value in file_reader:
        iteration_lst = [value[0], float(value[2]), float(value[3]), float(value[4]), float(value[5])]
        #making list
        iteration_code = value[1]
        try:
            master_dictionary[iteration_code][5].append(iteration_lst)
            #adding list at index if key present
        except KeyError:
            continue
    
def get_max_price_of_company (master_dictionary, company_symbol):
    '''Returns a float of max price and date respectively
       Doesn't display anything and takes main dictionary and symbol as parameters'''
    company_lst = []
    for key,value in master_dictionary.items():
        if key == company_symbol:
            #if key and symbol are equal
            iteration_lst = master_dictionary[company_symbol][5]
            if(len(iteration_lst)==0):
                iteration_tup = (None,None)
                return (None,None)
            else:
                for lst in iteration_lst:
                    date_str = lst[0]
                    iteration_tup = lst[4], date_str
                    company_lst.append(iteration_tup)
                    #appending occurence to list
    if(len(company_lst)==0):
        return (None,None)
        #returning none if length of list is 0
    max_price = max(company_lst)
    #getting max price tuple
    return max_price
    #returning max price as a tuple

def find_max_company_price (master_dictionary):
    '''Takes the main dictionary as parameter and returns a tuple containing 
       company symbol and max price of stock
       Doesn't display anything'''
    company_lst = []
    #creating empty list
    for key,value in master_dictionary.items():
        iteration_tup = get_max_price_of_company(master_dictionary, key)
        if(iteration_tup[0]==None):
            continue
        final_tup = key, iteration_tup[0]
        #creating a tuple
        company_lst.append(final_tup)
        #appending tuple
    max_tup = (0,0)
    for value in company_lst:
        if(value[1]>max_tup[1]):
            max_tup = value
            #getting max tuple
    return max_tup
    #returning max price of company

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''The main dictionary and company symbol are taken as parameter and a float value is returned containing avg price
        Doesn't display anything'''
    company_sum = 0
    company_counter = 0
    for key,value in master_dictionary.items():
        if key == company_symbol:
            iteration_lst = master_dictionary[company_symbol][5]
            if(len(iteration_lst)==0):
                return 0
            else:
                for lst in iteration_lst:
                    company_sum += lst[4]
                    #adding value of each high occurence
                    company_counter += 1
                    #counting number of occurences
    if(company_counter==0):
        return 0
        #preventing division by zero
    avg_price = company_sum/company_counter
    #calculating average
    return round(avg_price,2)
    #returning rounded value
        
def display_list (lst):  # "{:^35s}"
    '''Takes a list as a parameter and displays it in 3 columns'''
    counter = 0
    #making a counter to get list values
    for i in range(math.ceil(len(lst)/3)):
        for j in range(3):
            print("{:^35s}".format(lst[counter]), end = "")
            #printing each value
            counter+=1
            if counter==len(lst):
                break
        print()
    if((len(lst))%3==0):
        print("\n")
    else:
        print()

def main():
    print(WELCOME)
    #printing welcome banner
    prices_fp, security_fp = open_file()
    #getting both file pointers
    company_names_set, program_dictionary = read_file(security_fp)
    #getting company name set and dictionary
    add_prices(program_dictionary,prices_fp)
    #adding price values to dictionary
    print(MENU)
    #printing menu
    option_int = int(input("\nOption: "))
    #getting option
    while(option_int!=6):
        if(option_int==1):
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            sorted_set = list(company_names_set)
            sorted_set.sort()
            #sorting list
            display_list(sorted_set)
            #calling display
        if(option_int == 2):
            print("\ncompanies' symbols:")
            symbol_lst = []
            for key,value in program_dictionary.items():
                symbol_lst.append(key)
            symbol_lst.sort()
            #sorting symbol list
            display_list(symbol_lst)
            #displaying symbol list
        if(option_int==3):
            company_symb = input("\nEnter company symbol for max price: ")
            while True:
                #asking for company symbol until correct one is entered
                company_symb.upper()
                if(company_symb in program_dictionary):
                    break
                else:
                    print("\nError: not a company symbol. Please try again.")
                company_symb = input("\nEnter company symbol for max price: ")
            max_price_tup = get_max_price_of_company(program_dictionary, company_symb)
            #getting max price of stock
            stock_price = max_price_tup[0]
            date_str = max_price_tup[1]
            if(stock_price==None):
                print("\nThere were no prices.")
            else:
                print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(stock_price, date_str))
                #printing maximim stock and date
        if(option_int == 4):
            max_tup = find_max_company_price(program_dictionary)
            #calling function to get highest stock and price
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(max_tup[0], max_tup[1]))
            #printing highest stock and its price
        if (option_int == 5):
            company_symbol = input("\nEnter company symbol for average price: ")
            while True:
                #prompting for correct company symbol
                if(company_symbol in program_dictionary):
                    break
                else:
                    print("\nError: not a company symbol. Please try again.")
                company_symbol = input("\nEnter company symbol for average price: ")
            avg_price_float = get_avg_price_of_company(program_dictionary, company_symbol)
            #Calling function to get average price
            if(avg_price_float==0):
                print("\nThere were no prices.")
                #Output if no prices
            else:
                print("\nThe average stock price was ${:.2f}.\n".format(avg_price_float))
                #printing average price of stock
        if(option_int > 6):
            print("\nInvalid option. Please try again.")
        print(MENU)
        option_int = int(input("\nOption: "))
        #getting option again

            
       
if __name__ == "__main__": 
    main() 
#end of program
#############################################################
#
# Algorithm
#       Importing Card and Deck from cards
#       Initializing the game by calling the initialize() function
#       Printing the Menu
#       Displaying the board using display() function
#       Asking the user for an option
#       Checking validity using parse_option() function
#       If user chooses TT or TF:
#           Calling tableau_to_tableau() or tableau_to_foundation() respectively
#           Displaying Error message if move unsuccessful
#           Checking for win if move from tableau to foundation
#           Displaying the board either way
#       If user chooses WT:
#           Calling the waste_to_tableau()
#           If move unsuccessful display error message
#           Displaying the board
#       If user chooses WF:
#           Calling the waste_to_foundation() function
#           If move unsuccessful displaying the error message
#           If successful check for win
#               If win break and print winning message
#           Display the board
#       If user chooses SW:
#           Call stock_to_waste() to check if card can be moved
#           Display Error Message if move unsuccessful
#           Display the board
#       If user chooses R:
#           Call the initialize() function to reset data structures
#           Print the Menu and Display new board
#       If user chooses H:
#           Print the Menu
#       If user chooses Q:
#           Quit the game and end process
#       If wrong option entered Display Error message and the board
#       Ask user for option again and check validity
#       End of program
#
#############################################################

from cards import Card, Deck
#importing card and deck from cards

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    ''' This function takes no parameters and initializes four lists of data and returns them. 
        The function doesn't display anything'''
    card_deck = Deck()
    #Getting a deck of cards
    Deck.shuffle(card_deck)
    #Shuffling the deck
    tableau_lst = [[],[],[],[],[],[],[]]
    #initializing empty tableau
    for i in range(7):
        for j in range(i,7):
            card_value = Deck.deal(card_deck)
            tableau_lst[j].append(card_value)
        Card.flip_card(tableau_lst[i][i])
    #appending card values to tableau and flipping last card
    for i in range(7):
        for j in range(i,7):
            Card.flip_card(tableau_lst[j][i])
            #flipping all cards to get the desired tableau
    foundation_lst = [[],[],[],[]]
    #initializing foundation
    stock_lst = card_deck
    #getting the left stock
    waste_lst = []
    talon_card = Deck.deal(stock_lst)
    waste_lst.append(talon_card)
    return tableau_lst, stock_lst, foundation_lst, waste_lst
    #returning required data structures
    

def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''Checks if a card can be moved from stock to the waste and returns a boolean answer. Takes two parameters, stock and waste respectively. Doesn't display anything'''
    moved_card = Deck.deal(stock)
    #pops a card from the stock and stores a value if stock not empty else None
    if(moved_card == None):
        return False
    waste.append(moved_card)
    #Appends value to waste
    return True
    #returns boolean answer
    
       
def waste_to_tableau( waste, tableau, t_num ):
    '''Takes three parameters waste, tableau and a tableau column index and returns a boolean value regarding if a card can be moved from the waste to the tableau. Doesn't display anything'''
    moved_card = waste.pop()
    #gets the last card from the waste
    moved_card_rank = Card.rank(moved_card)
    moved_card_suit = Card.suit(moved_card)
    #Getting the suit and rank of the card
    tableau_column = len(tableau[t_num])
    if(tableau_column == 0):
        #if tableau is empty checks if the incoming card is a King
        if(moved_card_rank == 13):
            tableau[t_num].append(moved_card)
            return True
        else:
            waste.append(moved_card)
            return False
    comparing_card = tableau[t_num].pop()
    #Getting the topmost card in the tableau
    comparing_card_rank = Card.rank(comparing_card)
    comparing_card_suit = Card.suit(comparing_card)
    #Getting the rank and suit
    card1_suit = 'red' if 1<comparing_card_suit<4 else 'black'
    card2_suit = 'red' if 1<moved_card_suit<4 else 'black'
    #Determining suit colour
    if(comparing_card_rank - moved_card_rank== 1 and card1_suit != card2_suit):
        tableau[t_num].append(comparing_card)
        tableau[t_num].append(moved_card)
        #Checking if card can be moved and returning an answer accordingly
        return True
    else:
        tableau[t_num].append(comparing_card)
        waste.append(moved_card)
        return False


def waste_to_foundation( waste, foundation, f_num ):
    '''Takes waste, foundation and a foundation index number to check if a card can be moved from the waste to the foundation. Doesn't display anything. Returns a boolean value'''
    moved_card = waste.pop()
    moved_card_rank = Card.rank(moved_card)
    #Getting last card and rank
    try:
        required_rank = len(foundation[f_num])
    except IndexError:
        return False
    moved_card_suit = Card.suit(moved_card)
    if(required_rank>0):
        required_suit = Card.suit(foundation[f_num][0])
    transferable_bool = moved_card_suit == required_suit if required_rank>0 else True
    #Checks if the card is transferable
    if(moved_card_rank - required_rank == 1 and transferable_bool == True):
        foundation[f_num].append(moved_card)
        return True
    else:
        waste.append(moved_card)
        return False
    #returning boolean value

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''Takes four parameters, namely the tableau, foundation and their respective index numbers. Doesn't display anything and returns a boolean value of if a move from tableau to foundation is possible'''
    try:
        moved_card = tableau[t_num].pop()
        compare_card = foundation[f_num].pop() if len(foundation[f_num])>0 else 0
        #checking if index numbers are in range
    except IndexError:
        return False
    moved_card_rank = Card.rank(moved_card)
    moved_card_suit = Card.suit(moved_card)
    #Getting rank and suit
    if(compare_card==0):
        if(moved_card_rank == 1):
            foundation[f_num].append(moved_card)
            if(len(tableau[t_num])!=0 and Card.is_face_up(tableau[t_num][-1])==False):
                Card.flip_card(tableau[t_num][-1])
                #Card flipping
            return True
        else:
            tableau[t_num].append(moved_card)
            return False
    compare_card_rank = Card.rank(compare_card)
    compare_card_suit = Card.suit(compare_card)
    #getting rank and suit
    if(moved_card_rank-compare_card_rank==1 and moved_card_suit==compare_card_suit):
        #Suit and rank comparison
        foundation[f_num].append(compare_card) 
        foundation[f_num].append(moved_card)
        if(len(tableau[t_num])!=0 and Card.is_face_up(tableau[t_num][-1])==False):
                Card.flip_card(tableau[t_num][-1])
                #Card flipping
        return True
    else:
        foundation[f_num].append(compare_card)
        tableau[t_num].append(moved_card)
        return False
        #returning boolean value

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''Takes the tableau and two column indexes to check if a move is possible. Returns a boolean value and doesn't display anything'''
    try:
        moved_card = tableau[t_num1][-1]
        compare_card = tableau[t_num2][-1] if len(tableau[t_num2])>0 else 0
        #Checking valid input
    except IndexError:
        return False
    moved_card_rank = Card.rank(moved_card)
    moved_card_suit = Card.suit(moved_card)
    #Getting rank and suit
    if(compare_card == 0):
        if(moved_card_rank == 13):
            tableau[t_num1].pop()
            if(len(tableau[t_num1])!=0 and Card.is_face_up(tableau[t_num1][-1])==False):
                Card.flip_card(tableau[t_num1][-1])
                #Flipping card
            tableau[t_num2].append(moved_card)
            return True
        else:
            return False
            #returning boolean value
    compare_card_rank = Card.rank(compare_card)
    compare_card_suit = Card.suit(compare_card)
    card1_suit = 'red' if 1<compare_card_suit<4 else 'black'
    card2_suit = 'red' if 1<moved_card_suit<4 else 'black'
    #Getting the colour of the suit for comparison
    if(compare_card_rank - moved_card_rank== 1 and card1_suit != card2_suit):
        #Checking validity
        tableau[t_num2].append(moved_card)
        tableau[t_num1].pop()
        if(len(tableau[t_num1])!=0 and Card.is_face_up(tableau[t_num1][-1])==False):
                Card.flip_card(tableau[t_num1][-1])
                #Flipping the card
        return True
    else:
        return False
        #returning boolean value


def check_win (stock, waste, foundation, tableau):
    '''Checks win of game and returns a boolean value. Takes four parameters stock, waste, foundation and tableau. Doesn't display anything'''
    counter = 0
    for suit in foundation:
        if(len(suit)!=13):
            counter+=1
            #Checking if each suit is full
    for column in tableau:
        if(len(column)!=0):
            counter+=1
            #Checking if each column in the tableau is empty
    if(len(stock)==0 and len(waste)==0 and counter==0):
        return True
        #returning bool value
    else:
        return False

    
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    tableau, stock, foundation, waste = initialize()
    #Calling initialize function
    print(MENU)
    #Printing the Menu
    display(tableau, stock, foundation, waste)
    #Displaying the data structures
    option_str = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
    validity_lst = parse_option(option_str)
    #Inputting option and checking validity
    while True:
        if(validity_lst==None):
            display(tableau, stock, foundation, waste)
            #If not valid displaying the data structures
        elif(validity_lst[0].upper() == 'TT'):
            transfer_bool = tableau_to_tableau(tableau, validity_lst[1]-1, validity_lst[2]-1)
            #Checking if tableau to tableau possible
            if(transfer_bool==False):
                print("\nInvalid move!\n")
                #Printing Error Message
                display(tableau, stock, foundation, waste)
            else:
                display(tableau, stock, foundation, waste)
                #Displaying the data structures
        elif(validity_lst[0].upper()=='TF'):
            transfer_bool= tableau_to_foundation(tableau, foundation, validity_lst[1]-1, validity_lst[2]-1)
            #Checking if tableau to foundation possible
            if(transfer_bool==True):
                win = check_win(stock, waste, foundation, tableau)
                if(win==True):
                    #If possible checking for win
                    print("You won!")
                    #Winning message
                    display(tableau, stock, foundation, waste)
                    break
                else:
                    display(tableau, stock, foundation, waste)
            else:
                print("\nInvalid move!\n")
                #Error Message
                display(tableau, stock, foundation, waste)
        elif(validity_lst[0].upper()=='WT'):
            transfer_bool = waste_to_tableau(waste, tableau, validity_lst[1]-1)
            #Checking if waste to tableau possible
            if(transfer_bool==False):
                print("\nInvalid move!\n")
                #Error Message
                display(tableau, stock, foundation, waste)
            else:
                display(tableau, stock, foundation, waste)
        elif(validity_lst[0].upper()=='WF'):
            transfer_bool = waste_to_foundation(waste, foundation, validity_lst
            [1]-1)
            #Checking if waste to foundation possible
            if(transfer_bool==False):
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
            else:
                win = check_win(stock, waste, foundation, tableau)
                #Checking for win
                if(win==True):
                    print("You won!")
                    display(tableau, stock, foundation, waste)
                    break
                display(tableau, stock, foundation, waste)
                #Displaying tableau
        elif(validity_lst[0].upper()=='SW'):
            transfer_bool = stock_to_waste(stock , waste)
            #Checking if stock to waste possible
            if(transfer_bool==False):
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
            else:
                display(tableau, stock, foundation, waste)
        elif(validity_lst[0].upper()=='R'):
            tableau, stock, foundation, waste = initialize()
            #Resetting tableau
            print(MENU)
            display(tableau, stock, foundation, waste)
        elif(validity_lst[0].upper()=='H'):
            print(MENU)
            #Printing Menu
        elif(validity_lst[0].upper()=='Q'):
            break
            #Quitting game
        option_str = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")
        validity_lst = parse_option(option_str)
        #Getting another option
        

       

if __name__ == '__main__':
     main()

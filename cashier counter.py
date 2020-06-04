#Anas Alkhaldi
# ID number: 217882737
from time import sleep
import datetime # for now() function
basket = dict() #the initially empty basket which will include the username as a key and another dictionary of products and their amounts as the username's value
basket_for_update = dict() # initially empty dictionary for later use in the sub menu
users = {'ahmet':'sehir123','meryem':'4444','osama': 'osama@1959', 'ahmad': 'ertugrul','bader':'bamsi','baraa':'turgut','adnan':'1234','1':'1'}# users data (username and password)
inventory = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7], 'apples': [20, 5], 'banana': [10, 8],
                 'berries': [30, 3], 'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12],
                 'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], 'grape juice': [10, 9]}
def login(): #login function
    global username,basket,basket_for_update # for avoiding any problems with local variables (this is used throughout the whole code)
    print '****Welcome to Sehir Online Market****'
    print 'Please log in by providing your user credentials:'
    username = raw_input('User Name:')#asking for username
    password = raw_input('Password:')#asking for password
    while username not in users or users[username] != password: #in case the username is not in defined in the users dictionary or the password does not match with the username
        print 'Your user name and/or password is not correct. Please try again!'
        username = raw_input('User Name:')
        password = raw_input('Password:')
    for username_check in basket: # loop for checking the username of the original basket AFTER LOGGING OUT
        if username_check != username: # in case ANOTHER user logged in and wanted to fill their NEW BASKET, the old saved basket WILL BECOME INITIALLY EMPTY again for the NEW user
            basket = dict()
            basket_for_update = dict()
    print 'Successfully logged in!'
    main_menu() # calling the main menu function so that the user will be able to choose a choice from its available options (THIS WILL BE USED THROUGHOUT THE WHOLE CODE IN DIFFERENT PLACES SO THAT THE MAIN MENU COMES OUT AGAIN OR THE USER WILL REFER TO IT BY CLICKING 0)
def main_menu(): #function starting from the main menu
    global username,basket,basket_for_update
    if basket == dict(): # This will print the following statement only when the basket is initially empty (only at the beginning) to avoid any mistakes
        print 'Welcome',username + '!','Please choose one of the following options by entering the corresponding menu number.'
    print 4*' ','Please choose one of the following services:'
    print 4*' ','1. Search for a product'
    print 4*' ','2. See Basket'
    print 4*' ','3. Check Out'
    print 4*' ','4. Logout'
    print 4*' ','5. Exit'
    choice = int(raw_input('Your Choice:')) # asking for main menu choice of user
    while choice > 5 or choice < 1: # in case his input was out of range
        choice = int(raw_input('Your Choice:'))
    num,Total,counter = 1,0,0 # initial number for showing the numbers besides each resulting item. And initial Total value for summing all the "totals" in the basket. And finally a counter for placing the found items (after searching) in an empty dictionary called dictOfItems
    if choice == 1: #in case the user chose option one from the main menu
        searchWord = raw_input('what are you searching for?') #asking the user for the items he is searching for or trying to find
        searchWord.lower() # for manipulating all capital letters (if typed by the user) and changing them to small case letters since ALL of them are small in the inventory
        dictOfItems = dict() #initially empty dictionary used for including the items resulted AFTER THE SEARCH along with their numbers
        listOfKeys = inventory.keys() #acquiring the keys from the inventory dictionary and placing them in a list for the next modification
        list_to_word = ' '.join(listOfKeys) #joining all the items in the 'listOfKeys' into one STRING separated by a space after each item so that the program can check for availability in each STRING
        while searchWord not in list_to_word and searchWord != str(0) : #in case no similar items in the inventory were found with regards to the letter or word typed by the user in the search option
            print 'Your search did not match any items. Please try something else (Enter 0 for main menu):'
            searchWord = raw_input('what are you searching for?')
        if searchWord == str(0):# for returning back to main menu if user typed 0
            main_menu()
        for item in inventory: # loop for counting the available items in the inventory which are matching or similar to the search word, and are available in the stock
            if searchWord in item and inventory[item][0] > 0:
                counter+=1
                dictOfItems[item] = counter # for including the matching items in the previously defined dictionary along with their corresponding numbers
        print 'found',counter,'similar items'
        if counter == 0: # in case the item that the user is trying to look for was out of stock (no remaining amount)
            print 'Sorry! the item you are trying to search for seems to be out of stock. You will be redirected to main menu...'
            main_menu()
        for k in inventory: # loop for PRINTING the matching results along with their prices
            if searchWord in k and inventory[k][0] > 0:
                print 4*' ',str(num) + '.' + k, str(inventory[k][1]) + '$'
                num += 1
        items_choice = int(raw_input('Please select which item you want to add to your basket (Enter 0 for main menu):')) #asking the user to choose one of the resulting items
        while items_choice != 0 and (items_choice > counter or items_choice < 1): # in case the user typed a number not in range of the number of resulted items
            items_choice = int(raw_input('Please select which item you want to add to your basket (Enter 0 for main menu):'))
        if items_choice == 0: # returning back to main menu
            main_menu()
        for product in dictOfItems:
            if dictOfItems[product] == items_choice: # when the product in the acquired dictionary matches the number typed by the user
                print 'adding',product + '.', # THERE IS A MODIFICATION HERE
                amount = int(raw_input('Enter Amount:')) # THIS HAS TO BE ON THE SAME LINE WITH ABOVE
                while amount > inventory[product][0] and amount != str(0): # in case the amount typed by the user exceeds the stock amount of the item
                    print 'Sorry! The amount exceeds the limit, Please try again with smaller amount (Enter 0 for main menu):'
                    amount = int(raw_input('Enter Amount:'))
                if amount == 0:
                    main_menu()
                else:
                    if username not in basket: # when the user adds an item into their basket for THE FIRST TIME only
                        print 'added',product,'into your Basket.'
                        basket[username] = {product:amount} # adding the username as a key to the basket dictionary, and the product with its amount (nested dictionary) as a value
                        print 'Going back to main menu...'
                        main_menu()
                    else: # when its NOT THE FIRST TIME that the user adds an item into their basket
                        print 'added', product, 'into your Basket.'
                        basket[username][product] = amount # adding the product with its amount as a value to the ALREADY DEFINED username (key) in the basket
                        print 'Going back to main menu...'
                        main_menu()
    elif choice == 2: # in case the user chooses the second option
        if basket == {}: # in case the basket was empty (no item was added)
            print'your basket is empty!! Total price = 0$'
            main_menu()
        else: # in case there was one or more items
            print 'your basket contains:'
            for product in basket[username]: # loop for the products in the basket
                for item in inventory: # loop for the items in the inventory
                    if product == item: # this condition is to print out the price of the product by obtaining it from the INVENTORY'S DICTIONARY
                        total = float((inventory[item][1])*(basket[username][product])) # total money (considering the amount with it) for a single product
                        print 4*' ',str(num)+'.'+product,'price = ',str(inventory[item][1])+'$','amount=',basket[username][product],'total=',str(total)+'$'
                        basket_for_update[num] = product # adding the number of each product as a key into a dictionary and the product as its value for later usage in the sub-menu
                        num += 1
                        Total += total # for summing all the price in the basket (considering the product prices with their amounts too)
            print 'Total',str(Total)+'$'
            basket_sub_menu() # for taking the user to the sub menu after they see their basket
    elif choice == 3: # in case user chose option three in the main menu
        if basket == {}: # in case they wanted to check out with an empty basket
            print 'your basket is empty!! please insert some stuff inside it before check out'
            main_menu()
        else:
            layout() # calling the layout function
            print''# for the next line not to print on the same line of the 'processing your receipt' line since in the layout function there is a comma ',' at the end
            print '******* Sehir Online Market ********\n************************************\n    44 44 0 34\n    sehir.edu.tr\n------------------------------------'
            for product in basket[username]: # same as mentioned above about this whole loop
                for item in inventory:
                    if product == item:
                        total = float((inventory[item][1]) * (basket[username][product]))
                        print product, str(inventory[item][1]) + '$', 'amount=', basket[username][product], 'total=', str(total) + '$'
                        Total += total
            print '------------------------------------ \n  Total:', 2*' ', str(Total) + '$','\n------------------------------------','\n',datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),'\n', 'Thank You for using our Market! '
            for product in basket[username]: # loop for subtracting the amount of the item in the stock (inventory) by the amount the user chooses when buying
                for item in inventory:
                    if product == item:
                        inventory[item][0] -= basket[username][product] # after the checkout is done
            main_menu()
    elif choice == 4: # in case the user chooses the fourth option in the menu, the program will return to the login part
        login()
    elif choice == 5: # in case the user chooses the fifth option, the program will totally quit running
        quit()
def basket_sub_menu(): # function starting from sub menu
    global basket_for_update,basket
    num,Total = 1,0 # for updating the variable to prevent any mistake in the calculations
    print 'Please Choose an option:'
    print 4 * ' ', '1. update amount'
    print 4 * ' ', '2. Remove an item'
    print 4 * ' ', '3. Check Out'
    print 4 * ' ', '4. Go back to main menu'
    selection = int(raw_input('Your selection:')) # for asking the user for his choice in the sub menu from 1 to 4
    while selection > 4 or selection < 1: # in case he typed a number out of the range of the options
        selection = int(raw_input('Your selection:'))
    if selection == 1: # when the user chooses the first option
        if basket[username] == {}: # in case the user's basket became empty after removing all products inside it
            print 'No more possible deletions!! Your basket became empty! Please add some stuff in it...'
            main_menu()
        modified_item = int(raw_input('Please select which item to change its amount:')) # for asking the user to choose which item among those in the basket to update by referring back to its number
        while modified_item not in basket_for_update: # in case he chose an item which was not in his basket
            print 'sorry! this item is not in your basket'
            modified_item = int(raw_input('Please select which item to change its amount:'))
        new_amount = int(raw_input('Please type the new amount: ')) # for asking the user to type the new amount he wishes to update for the product
        while new_amount > inventory[basket_for_update[modified_item]][0]: # in case the new amount he typed was more than the available amount of the product in the inventory
            print 'Sorry! The amount exceeds the limit, Please try again with smaller amount (Enter 0 for main menu):'
            new_amount = int(raw_input('Please type the new amount:'))
        basket[username][basket_for_update[modified_item]] = new_amount # for updating the amount of the product in the basket
        print 'Your basket now contains:'
        for product in basket[username]: # loop for displaying the basket contents after update as done when the user chooses to see his basket from the main menu (option 2)
            for item in inventory:
                if product == item:
                    total = float((inventory[item][1]) * (basket[username][product]))
                    print 4 * ' ', str(num) + '.' + product, 'price = ', str(inventory[item][1]) + '$', 'amount=',basket[username][product],'total=',str(total)+'$'
                    num += 1
                    Total += total
        print 'Total', str(Total) + '$'
        basket_sub_menu() # for returning back to the sub menu again
    elif selection == 2: # in case the user selected the second option in the sub menu
        if basket[username] == {}: # in case the user's basket became empty after removing all products inside it
            print 'No more possible deletions!! Your basket became empty! Please add some stuff in it...'
            main_menu()
        removed_item = int(raw_input('Which item would you like to remove?:')) # asking the user which item they wish to remove by referring back to its number
        while removed_item not in basket_for_update: # in case the user chose a number which does not refer to any item ( in case he chose an item which is not im the basket)
            print 'sorry! this item is not in your basket'
            removed_item = int(raw_input('Which item would you like to remove?:'))
        else: # in case there were still some items to remove
            del basket[username][basket_for_update[removed_item]] # for removing the item from the basket along with its amount
        for product in basket[username]: # loop for printing as described previously throughout the code
            for item in inventory:
                if product == item:
                    total = float((inventory[item][1]) * (basket[username][product]))
                    print 4 * ' ', str(num) + '.' + product, 'price = ', str(inventory[item][1]) + '$', 'amount=',basket[username][product],'total=',str(total)+'$'
                    num += 1
                    Total += total
        basket_sub_menu() # for returning back again to sub menu for user to choose
    elif selection == 3: # in case the user chose the third selection of checking out
        layout() #calling the layout function
        print ''# for the next line not to print on the same line of the 'processing your receipt' line since in the layout function there is a comma ',' at the end
        print '******* Sehir Online Market ********\n************************************\n    44 44 0 34\n    sehir.edu.tr\n------------------------------------'
        for product in basket[username]: # loop for printing out the stuff as described previously throughout the code
            for item in inventory:
                if product == item:
                    total = float((inventory[item][1]) * (basket[username][product]))
                    print product, str(inventory[item][1]) + '$', 'amount=', basket[username][product], 'total=', str(total) + '$'
                    Total += total
        print '------------------------------------ \n  Total:', 2*' ', str(Total) + '$','\n------------------------------------','\n',datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),'\n', 'Thank You for using our Market! '
        for product in basket[username]: # loop for subtracting amounts as described previously in the main menu choice of 3 too
            for item in inventory:
                if product == item:
                    inventory[item][0] -= basket[username][product] # for subtracting the amount of the product in the basket from that in the inventory
        main_menu()
    elif selection == 4: # in case the user chose to return back to the main menu by selecting choice 4
        main_menu()
def layout(): # function for showing the 'processing your receipt' part in a more REALISTIC way when the user wishes to check out
    for i in range(4):
        if i == 0:
            print 'processing your receipt',
        else:
            print '.',
        sleep(0.5) # for slowing down the loop (0.5 seconds)
login()


















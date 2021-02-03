import time, random, sys

# Init and define key variables
cookies = 0
coinpos = ['h', 't']
points = 1
multi = 1
insur = 0
upgrading = False
# Init and define upgrades lists
upgrades_text = ["1. +1 Cookies", "2. +1x Multiplier", "3. +5% Insurance"]

# This one is a little confusing (num_upgrades) but it basically keeps track of 
# how many upgrades were bought in order to scale the game properly
num_upgrades = [1, 1, 1]
upgrades_cost = [5*num_upgrades[0], 10*num_upgrades[1], 3*num_upgrades[2]]

# Define upgrade functions
def inc_cookies():
    global points
    global num_upgrades
    global cookies
    global upgrades_cost
    points += 1
    num_upgrades[0] += 1
    cookies -= upgrades_cost[0]


def inc_multi():
    global multi
    global num_upgrades
    global cookies
    global upgrades_cost
    multi += 1
    num_upgrades[1] += 1
    cookies -= upgrades_cost[1]


def inc_insur():
    global insur
    global num_upgrades
    global cookies
    global upgrades_cost
    insur += 0.05
    num_upgrades[2] += 1
    cookies -= upgrades_cost[2]

upgrades_funcs = [inc_cookies, inc_multi, inc_insur]

# generate random seed number
def generate_number():
    seed = int(time.time() * 1000)
    random.seed(seed)
    return (int(random.random()*10000000000))

# returns a 0 or 1 value for heads or tails
def check_coin(coin_num):
    if(coin_num % 2 == 0):
        coin = coinpos[0]
    else:
        coin = coinpos[1]

    return coin

# handles upgrade shop and upgrade execution
def upgrade_exec(user_choice):
    if(user_choice.lower() == 'u'):    
        global upgrades_cost
        global upgrades_funcs
        global upgrades_text
        global upgrades_cost
        global points
        global multi
        global insur
        
        print(upgrades_text)
        upgrades_cost = [5*num_upgrades[0], 10*num_upgrades[1], 3*num_upgrades[2]]
        print(upgrades_cost)
        print("Choose an upgrade! (press r to return to game)")
        upgrade_choice = input()

        while(upgrade_choice != 'r' and upgrade_choice == '1' or upgrade_choice == '2' or upgrade_choice == '3'):
            i = int(upgrade_choice) - 1
            print("Welcome to the upgrade shop!")

            if(cookies < upgrades_cost[i]):
                print("Insufficient Funds")
            else:
                upgrades_funcs[i]()
                num_upgrades[i] += 1

            if(i == 0):
                print("Cookies gained/lost is now:", points)
                break
            elif(i == 1):
                print("Multiplier is now", multi)
                break
            elif(i == 2):
                print("Insurance is now:", str(insur*100) + "%")
                break

        if(upgrade_choice.lower() == 'r'):
            return 0

        elif(upgrade_choice != '1' and upgrade_choice != '2' and upgrade_choice != '3' and upgrade_choice != 'r'):
            print("Invalid Input!")
            print("Choose an upgrade! (press r to return to game)")
            input()

    else:
        pass


def main():
    global cookies

    # main loop
    while(True):
        
        # call functions to determine coin
        coin_num = generate_number()

        coin = check_coin(coin_num)
        
        print("A coin is flipped...")
        print("Guess which side it landed on! (h for Heads/t for Tails/u for Upgrades/q to Quit)")

        # take in user input
        user_choice = input()

        upgrade_exec(user_choice)

        # check if player's choice is correct, checks for quitting, checks for upgrade shop entrance, and invalid input
        if(user_choice.lower() == coin):
            print("Congrats! You got it right!")
            cookies += multi*points
            print("+", multi*points, "Cookie(s)")
            

        if(user_choice.lower() == 'q'):
            sys.exit()

        elif(user_choice.lower() == 'h' and coin == 't' or user_choice.lower() == 't' and coin == 'h'):
            print("Damn bro... you got it wrong")
            cookies += -(multi*points) + (multi*points*insur)
            print("-", ((multi*points) - (multi*points*insur)), "Cookie(s)"),

        elif(user_choice.lower() != 't' and user_choice.lower() != 'h' and user_choice.lower() != 'u' and user_choice.lower() != 'q'):
            print("Invalid Input!")
        
        # display current cookies
        print("You currently have", int(cookies), "cookies")

# call main function
main()

import time, random

def main():
    cookies = 0
    coinpos = ['h', 't']
    coin = ' '
    points = 1
    while(True):
        u_time = time.time()
        seed = int(u_time * 1000)
        random.seed(seed)
        coin_num = (int(random.random()*10000000000))

        if(coin_num % 2 == 0):
            coin = coinpos[0]
        else:
            coin = coinpos[1]
        print("A coin is flipped...")
        print("Guess which side it landed on! (h for Heads/t for Tails)")
        user_choice = input()

        if(user_choice.lower() == 'h' and coin == 'h'):
            print("Congrats! You got it right!")
            print("Here's a cookie, you deserve it")
            print("+", 2*points, "Cookies")
            cookies += 2*points

            print("You currently have", cookies, "cookies")

        elif(user_choice.lower() == 't' and coin == 't'):
            print("Congrats! You got it right!")
            print("Here's a cookie, you deserve it")
            print("+", 2*points, "Cookie")
            cookies += 2*points
            
            print("You currently have", cookies, "cookies")

        elif(user_choice.lower() == 'h' and coin == 't'):
            print("Damn bro... you got it wrong")
            print("Sorry to do this to you but...")
            print("-", points, "Cookie"),
            cookies -= points
            print("You currently have", cookies, "cookies")

        elif(user_choice.lower() == 't' and coin == 'h'):
            print("Damn bro... you got it wrong")
            print("Sorry to do this to you but...")
            print("-", points, "Cookie")
            cookies -= points
            print("You currently have", cookies, "cookies")

        elif(user_choice.lower() == 'q'):
            return 0
            
        else:
            print("Invalid Input!")

'''
        invalid = True
        while(invalid == True):
            user_choice = input("q to quit, r to repeat...")
            if(user_choice == 'q'):
                invalid = False
                print("Thanks for playing! :)")
                return 0
            elif(user_choice == 'r'):
                print()
                invalid = False
            else:
                print("Invalid Input!")
                invalid = True
'''
    
        
        

main()
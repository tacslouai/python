import time, random

question = ""
cookie_list = []
positions = []
counter = 0

def main(human):
    global cookie_list, positions, counter
    cookies = 500
    coinpos = ['heads', 'tails']

    coin = ' '
    
    while(True):
        u_time = time.time()
        seed = int(u_time * 1000)
        random.seed(seed)
        coin_num = (int(random.random()*10000000000))
        bot_num = random.randint(0,1)
        bet = 10
        prebet = bet
        if(coin_num % 2 == 0):
            coin = coinpos[0]
        else:
            coin = coinpos[1]

        
        if(human):
            print("A coin is flipped...")
            print("Guess which side it landed on! (h for Heads/t for Tails)")
            user_choice = input().lower().strip()

            if(user_choice == coin):
                print("Congrats! You got it right!")
                print("Here's a cookie, you deserve it")
                print("+1 Cookie")
                cookies += 1
                
                print("You currently have", cookies, "cookies")

            elif(user_choice != coin):
                print("Damn bro... you got it wrong")
                print("Sorry to do this to you but...")
                print("-1 Cookie")
                cookies -= 1
                print("You currently have", cookies, "cookies")

            elif(user_choice == 'q'):
                return 0
                
            else:
                print("Invalid Input!")
        
        elif(not human):
            #print("Bot play beginning...\n")
            #time.sleep(0.0001)
            bot_choice = coinpos[1]
            if bot_choice == coin:
                cookies += bet
                #bet = bet / 2
                
            elif bot_choice != coin:
                cookies -= bet
                #bet = bet * 2
            
            counter += 1
            positions.append(counter)
            cookie_list.append(cookies)
            
            print("Cookies: ", cookies)
            print(bet)
            print("Counter: ", counter)
            
            if counter >= 100000:
                break
                
        else:
            print('idk what happened')
            break
            
            

while(question != "answered"):    
    question = input("Are you a human?").strip().lower()
    if question == "yes" or question == "y":
        print()
        question = "answered"
        human = True
    elif question == "no" or question == "n":
        print()
        question = "answered"
        human = False
    else: 
        question = "unanswered"

main(human)

write_cookies = open( 'coin_flip_lh\cookies.txt', 'w' )
for a in cookie_list:
    write_cookies.write(str(a) + '\n' )
write_cookies.close()
    
write_pos = open("coin_flip_lh\position.txt", 'w')
for a in positions:
    write_pos.write(str(a) + '\n')
write_pos.close()
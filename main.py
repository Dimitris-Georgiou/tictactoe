import time
content = [7,8,9,4,5,6,1,2,3]
round = 1
player = 1
tag = ' '
winner = False
print("TicTacToe")


def check_winner():
    global winner
    if (content[0] == content[1] and content[1] == content[2] or
        content[3] == content[4] and content[4] == content[5] or
        content[6] == content[7] and content[7] == content[8] or
        content[0] == content[3] and content[3] == content[6] or
        content[1] == content[4] and content[4] == content[7] or
        content[2] == content[5] and content[5] == content[8] or
        content[0] == content[4] and content[4] == content[8] or
        content[2] == content[4] and content[4] == content[6]):
        print("\nWE HAVE A WINNER\nNICE JOB MR '{}'".format(tag))
        winner = True

def next_round():
    global player
    global tag
    if player %2 != 0:
        tag = "X"
    else:
        tag = "O"
    player+=1             

def board():
        print("\n{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n\n".format(
            content[0],content[1],content[2],
            content[3],content[4],content[5],
            content[6],content[7],content[8]))

def choose():
    a = input()
    b = int(a)
    for n in range(len(content)):           
        if b == content[n]:    
            content[n] = tag
def new_game():
    global round
    print("Do you want to play another round? (press Y/y to play or any other key to exit!")
    next_game = input()
    if next_game == "y" or next_game == "Y":
        round = 1
        main()
    else:
        print("See you soon!")
        time.sleep(2)
        exit()

def main():
    global round
    while(round <= 9):
        board()
        next_round()
        print("Player {} choose a spot!\n".format(tag))
        choose()
        check_winner()
        if winner:
            new_game()
        round+=1
    new_game()

main()

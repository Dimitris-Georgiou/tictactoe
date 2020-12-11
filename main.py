import time

print("TicTacToe")


class TicTacToe():
    

    content = [7, 8, 9, 4, 5, 6, 1, 2, 3]

    def check_winner(tag):
        if(content[0] == content[1] and content[1] == content[2] or
            content[3] == content[4] and content[4] == content[5] or
            content[6] == content[7] and content[7] == content[8] or
            content[0] == content[3] and content[3] == content[6] or
            content[1] == content[4] and content[4] == content[7] or
            content[2] == content[5] and content[5] == content[8] or
            content[0] == content[4] and content[4] == content[8] or
            content[2] == content[4] and content[4] == content[6]):

            print("\nWE HAVE Awinner\nNICE JOB MR '{}'".format(tag))
            new_game()
          

    def board():
            print("\n{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n\n".format(
              content[0],content[1],content[2],
              content[3],content[4],content[5],
              content[6],content[7],content[8]))

    def choose(tag):
        a = input()
        b = int(a)
        for n in range(len(content)):           
            if b == content[n]:    
              content[n] = tag
    def new_game():
        print("Do you want to play another .round ? (press Y/y to play or any other key to exit!")
        next_game = input()
        if next_game == "y" or next_game == "Y":
            start_game()
        else:
            print("See you soon!")
            time.sleep(2)
            exit()

    def start_game():
        round = 1
        tag = ''
        while(round <= 9):
            player = 1
            board()
            if player %2 != 0:
               tag = "X"
            else:
               tag = "O"
            player+=1
            print("Player {} choose a spot!\n".format(tag))
            choose(tag)
            check_winner(tag)
            round +=1
        new_game()

    if __name__ == '__main__':
        start_game()
    

game_on = TicTacToe()
game_on()

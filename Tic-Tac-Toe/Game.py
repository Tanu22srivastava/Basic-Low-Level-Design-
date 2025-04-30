from Player import Player
from Board import Board
import random

class Game:
    def __init__(self,player1_name,player2_name,size):
        self.player1= Player(player1_name,"X")
        self.player2= Player(player2_name,"0")
        self.board= Board(size)
        self.current_Player= None
    
    def switch_turn(self):
        self.current_Player= self.player1 if self.current_Player!= self.player1 else self.player2
    
    def perform_toss(self):
        toss_option=["Head","Tail"]
        player1_choice= input("Which one you choose? Player 1 (Head/Tail)")
        player2_choice= input("which one you choose? Player 2 (Head/Tail)")

        if player2_choice== player1_choice:
            print("You cannot choose the same side!!!!")
            player2_choice= "Head" if player1_choice== "Tail" else "Tail"

        print(f"{self.player1.name} chooses {player1_choice}")
        print(f"{self.player2.name} chooses {player2_choice}")

        toss_result= random.choice(toss_option)
        
        print(f"The toss result is {toss_result}")
        if toss_result.strip().lower()==player1_choice.strip().lower():
            print(f"Congrats!! {self.player1.name} won the toss")
            self.current_Player= self.player1
        else:
            print(f"Congrats!! {self.player2.name} won the toss")
            self.current_Player= self.player2

    def start_game(self):
        while True:
            self.board.display()
            print(f"{self.current_Player.name}'s Turn " )
            row= int(input("Enter the row number "))
            col= int(input("Enter the col number"))
            if(self.board.place_move(row,col,self.current_Player.symbol)):
                if self.board.check_for_win(self.current_Player.symbol):
                    self.board.display()
                    print(f"yipppiiiii {self.current_Player.name} won the gameee")
                    break

                elif self.board.is_full():
                    self.board.display()
                    print("Game Draw!!!!")
                    break
                self.switch_turn()
            else:
                print("Invalid Move")

game= Game("p1","p2",4) 
game.perform_toss()
game.start_game()

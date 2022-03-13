#!/usr/bin/env python
import rospy
import numpy
import random
import time
position = None
Condizione_loop = False
Room_list = ['1.1_Kitchen','1.2_Ballroom', '1.3_Conservatory', '2.1_Diningroom', '2.3_Billiardroom', '2.4_Library', '3.1_Lounge', '3.2_Hall', '3.3_Studio']
#Room_list = ['1.1_Kitchen','1.2_Ballroom', '1.3_Conservatory',
#            '2.1_Diningroom', '2.3_Billiardroom', '2.4_Library',
#            '3.1_Lounge', '3.2_Hall', '3.3_Studio']
#2.2 is the asking room
visited_room = [1, 1, 1, 1, 1, 1, 1, 1, 1]
#########################FUNCTIONS#########################
def random_room():
    return random.choice(Room_list)
def go_to_point(ActualPosition):
    global visited_room
    print("Before the moving i am in the room" + ActualPosition)
    time.sleep(1)
    not_visited = False   
    while not_visited == False:
        print("entro qui")
        after_position = random_room()
        for x in range (9):
            if after_position == Room_list[x]:
                pos = x
        if visited_room[pos] == 0:
            not_visited = False 
            
            print("azzerato")
        else:
            not_visited = True 
            visited_room[pos] = 0
    print("skippo")
    after_position = random_room()
    print ("After the moving i am in the room" + after_position)
    return after_position

def ask_hint():
    funzione chiedi hints----------------------------
    if hint == who:
        aggiungilo
    if hint == where:
        aggiungilo
    if hint == what:
        aggiungilo

def find_position(x)
    for position_array in range(9): 
        if x = visited_room [position_array]:
            return position_array
        
    
def search_hints()
##################################################
def main():
    avvio armor----------------------------
    position = '0.0_init'
    killer_found = False
    while killer_found = True:
        while hypotesis consistent = True:
            after_position = go_to_point(position)
            ask_hint()------------------------------  
            find hypotesis consistent
        
        
        
        bool oracle_answer = ask_to_oracle()----------------
        if oracle_answer:
            Killer_found = True
    



if __name__ == '__main__':
    main()




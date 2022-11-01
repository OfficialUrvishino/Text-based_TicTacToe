game = True
valid_inputs = ['draw', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pos = {
    'topleft' : '1',
    'top' : '2',
    'topright' : '3',
    'left' : '4',
    'middle' : '5',
    'right' : '6',
    'bottomleft' : '7',
    'bottom' : '8',
    'bottomright' : '9'
    }
move_counter = 0

def evaluate(letter, pname):
    if ((pos['topleft'] == letter and pos['top'] == letter and pos['topright'] == letter) or
     (pos['left'] == letter and pos['middle'] == letter and pos['right'] == letter) or
     (pos['bottomleft'] == letter and pos['bottom'] == letter and pos['bottomright'] == letter) or
     (pos['topleft'] == letter and pos['left'] == letter and pos['bottomleft'] == letter) or
     (pos['top'] == letter and pos['middle'] == letter and pos['bottom'] == letter) or
     (pos['topright'] == letter and pos['right'] == letter and pos['bottomright'] == letter) or
     (pos['topleft'] == letter and pos['middle'] == letter and pos['bottomright'] == letter) or
     (pos['topright'] == letter and pos['middle'] == letter and pos['bottomleft'] == letter)):
        print(pname, "has won!")
        exit()
    elif move_counter == 9:
        print("This game is a draw!")
        exit()
        
#update board
def updateboard():
    print(pos['topleft'], " | ", pos['top'], " | ", pos['topright'])
    print("-------------")
    print(pos['left'], " | ", pos['middle'], " | ", pos['right'])
    print("-------------")
    print(pos['bottomleft'], " | ", pos['bottom'], " | ", pos['bottomright'])
    print("\nx----------------------------x")
    
def validate_input(input):
    global valid_inputs
    try:
        check_input = valid_inputs.index(input)
        return True
    except:
        return False

#moves
def make_move(place, letter):
    global valid_inputs
    global move_counter
    move_counter += 1
    
    if place == "1":
        pos.update({'topleft' : letter})
        updateboard()
        
    if place == "2":
        pos.update({'top' : letter})
        updateboard()
        
    if place == "3":
        pos.update({'topright' : letter})
        updateboard()
        
    if place == "4":
        pos.update({'left' : letter})
        updateboard()
        
    if place == "5":
        pos.update({'middle' : letter})
        updateboard()

    if place == "6":
        pos.update({'right' : letter})
        updateboard()
        
    if place == "7":
        pos.update({'bottomleft' : letter})
        updateboard()
        
    if place == "8":
        pos.update({'bottom' : letter})
        updateboard()
        
    if place == "9":
        pos.update({'bottomright' : letter})
        updateboard()
        
    if place == "draw":
        print("This game is a draw!")
        exit()
    
    index = valid_inputs.index(place)
    valid_inputs.pop(index)
 
#gives the players a starting board to play in
updateboard()

#main game loop
while game == True:
    position = str(input("\nPlayer 1: "))
    test = validate_input(position)
    
    if test is True:
        make_move(position, "O")
        #Win conditions for Player 1
        evaluate("O", "Player 1")
    else:
        print('Invalid input !!')
        continue
            
    position = input("\nPlayer 2: ")
    test = validate_input(position)
    if test is True:
        make_move(position, "X")
        #Win conditions for Player 1
        evaluate("X", "Player 2")
    else:
        while test is False:
            print('Invalid input !!')
            position = input("\nPlayer 2: ")
            test = validate_input(position)
            if test is True:
                make_move(position, "X")
                #Win conditions for Player 1
                evaluate("X", "Player 2")
                break
        
    
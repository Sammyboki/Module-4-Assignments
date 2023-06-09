'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {'@bongolpoc':[] , 
                    '@joaquin':["@chums","@jobenilagan"], 
                    '@chums':["@bongolpoc","@miketan","@rudyang","@joeilagan"],
                    '@jobenilagan':["@eeebeee","@joeilagan","@chums","@joaquin"], 
                    '@joeilagan':["@eeebeee","@jobenilagan","@chums"], 
                    '@eeebeee':["@jobenilagan","@joeilagan"]}
    
    def relationship_status(from_member, to_member, social_graph):
        if from_member == '@bongolpoc':
            from_list = list(social_graph.values())[0]
        elif from_member == '@joaquin':
            from_list = list(social_graph.values())[1]
        elif from_member == '@chums':
            from_list = list(social_graph.values())[2]
        elif from_member == '@jobenilagan':
            from_list = list(social_graph.values())[3]
        elif from_member == '@joeilagan':
            from_list = list(social_graph.values())[4]
        elif from_member == '@eeebeee':
            from_list = list(social_graph.values())[5]
        else:
            from_list = from_member
        
        if to_member == '@bongolpoc':
            to_list = list(social_graph.values())[0]
        elif to_member == '@joaquin':
            to_list = list(social_graph.values())[1]
        elif to_member == '@chums':
            to_list = list(social_graph.values())[2]
        elif to_member == '@jobenilagan':
            to_list = list(social_graph.values())[3]
        elif to_member == '@joeilagan':
            to_list = list(social_graph.values())[4]
        elif to_member == '@eeebeee':
            to_list = list(social_graph.values())[5]
        else:
            to_list = to_member
        
        if from_member not in to_list:
            if to_member not in from_list:
                print ('no relationship')
            else:
                print ('follower')
        else:
            if to_member not in from_list:
                print('followed by')
            else:
                print('friends')


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    character_list = []
    def tic_tac_toe(board):
        grid = len(board)
        no_winner = 0
        winner_X = 0
        winner_O = 0
    
        #horizontal wins
        for i in range(grid):
            X = 0
            O = 0 
            for j in range(grid):
                if board[i][j] == "X":
                    X += 1
                elif board[i][j] == "O":
                    O += 1
                elif board[i][j] != "O":
                    O += 0
                elif board[i][j] != "X":
                    O += 0 
            
                if X == grid:
                    winner_X += 1 
                elif O == grid:
                    winner_O += 1
        if X != grid and O != grid:
            no_winner += 1
    
        #vertical wins
        for i in range(grid):
            X = 0
            O = 0 
            for j in range(grid):
                if board[j][i] == "X":
                    X += 1
                elif board[j][i] == "O":
                    O += 1
                elif board[j][i] != "O":
                    O += 0
                elif board[j][i] != "X":
                    O += 0 
            
                if X == grid:
                    winner_X += 1 
                elif O == grid:
                    winner_O += 1
        if X != grid and O != grid:
            no_winner += 1
        
        if winner_X >= 1:
            print ("X wins")
        elif winner_O >= 1:
            print ("O wins")
        else:
            print("NO WINNER")
        

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def eta(first_stop, second_stop, route_map):
        route = list(legs)
        time = legs.values()
        time_list = list(time)
        route_1 = list(route[0])
        route_2 = list(route[1])
        route_3 = list(route[2])
        time_to_1 = list(time_list[0].values())
        time_to_2 = list(time_list[1].values())
        time_to_3 = list(time_list[2].values())
        if first_stop == route_1[0] and second_stop == route_1[1]:
            print(time_to_1[0])
        elif first_stop == route_2[0] and second_stop == route_2[1]:
            print(time_to_2[0])
        elif first_stop == route_3[0] and second_stop == route_3[1]:
            print(time_to_3[0])
        elif first_stop == second_stop:
            total_time = int(time_to_1[0])+ int(time_to_2[0])  + int(time_to_3[0])
            print(total_time)
        elif first_stop == route_2[0] and second_stop == route_3[1]:
            total_time = int(time_to_2[0])  + int(time_to_3[0])
            print (total_time)
        elif first_stop == route_1[0] and second_stop == route_2[1]:
            total_time = int(time_to_1[0])  + int(time_to_2[0])
            print (total_time)
        elif first_stop == route_3[0] and second_stop == route_1[1]:
            total_time = int(time_to_1[0])  + int(time_to_3[0])
            print (total_time)

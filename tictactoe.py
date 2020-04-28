"""
Tic Tac Toe Player
"""

import math
import copy

X="X"
O ="O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    coux=0 
    couo=0   
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                coux+=1  
            elif board[i][j]==O:
                couo+=1    
    if coux>couo:
        return O
    elif coux==couo:
        return X    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    sett=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                sett.add((i,j))
    return sett            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    bc=copy.deepcopy(board)
    h=player(bc)
    if h==X:
        bc[action[0]][action[1]]=X
    elif h==O:
        bc[action[0]][action[1]]=O
    return bc    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    counthx=0
    countho=0
    countvx=0
    countvo=0
    countdx=0
    countdo=0
    countd2x=0
    countd2o=0
    countxx=0
    # for testing horizontally
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
               counthx+=1
            elif board[i][j]==O:
                countho+=1   
            if board[j][i]==O:
                countvo+=1
            elif board[j][i]==X:
                countvx+=1
            if i==j:
                if board[i][j]==X:
                    countdx+=1
                elif board[i][j]==O:
                    countdo+=1            
            if i==0 and j==2:
                if board[i][j]==X:
                    countd2x+=1
                elif board[i][j]==O: 
                    countd2o+=1   
            elif i==1 and j==1:
                if board[i][j]==X:
                    countd2x+=1
                elif board[i][j]==O: 
                    countd2o+=1 
            elif i==2 and j==0: 
                if board[i][j]==X:
                    countd2x+=1
                elif board[i][j]==O: 
                    countd2o+=1   
        if counthx==3:
            return X
        elif countho==3:
            return O
        elif countvo==3:
            return O
        elif countvx==3:
            return X       
        elif countdo==3:
            return O
        elif countdx==3:
            return X 
        elif countd2o==3:
            return O
        elif countd2x==3:
            return X                 
        else:    
            countxx+=1
        counthx=0
        countho=0
        countvo=0
        countvx=0    
    if countxx==3:        
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    k=winner(board)
    if k==X or k==O :
        return True
    if k==None:
        return False
    else:
        return False        

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p=winner(board)
    if p==X:
        return 1
    elif p==O:
        return -1
    elif p==None:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board)==X:
        acl=[]
        for action in actions(board):
            acl.append((action,maxvalue(result(board,action))))
        for i in acl:
            if i[1]>=1:
                return i[0]
        for i in acl:
            if i[1]==0:
                return i[0]
        for i in acl:
            if i[1]==-1:
                return i[0]
    elif player(board)==O:
        aclo=[]
        for action in actions(board):
            aclo.append((action,minvalue(result(board,action))))
        print(aclo)
        for j in aclo:
            if j[1]<=-1:
                return j[0]
        for j in aclo:
            if j[1]==0:
                return j[0]
        for j in aclo:
            if j[1]==1:
                return j[0]                        
    else :
        return None    

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):    
        v=max(v,minvalue(result(board,action)))
    return v        

def minvalue(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,maxvalue(result(board,action)))
    return v            



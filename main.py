import streamlit as st
import numpy as np
import math


# From: https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return None


def checkWin(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


def tictactoe():
    st.write("")

    # Initialize state.
    if "board" not in st.session_state:
        st.session_state.board = np.full((3, 3), ".", dtype=str)
        st.session_state.next_player = "X"
        st.session_state.player = "O" if st.session_state.next_player == "X" else "X"
        st.session_state.winner = None

    # Define callbacks to handle button clicks.
    def handle_click(i, j):
        if not st.session_state.winner:
            st.session_state.board[i, j] = st.session_state.next_player
            st.session_state.next_player = (
                "O" if st.session_state.next_player == "X" else "X"
            )

            if st.session_state.player == "O":
                botMove(st.session_state.board)
                st.session_state.next_player = (
                    "O" if st.session_state.next_player == "X" else "X"
                )
            winner = checkWin(st.session_state.board)
            if winner != ".":
                st.session_state.winner = winner

    # Show one button for each field.
    for i, row in enumerate(st.session_state.board):
        cols = st.columns([0.1, 0.1, 0.1, 1.5])
        for j, field in enumerate(row):
            cols[j].button(
                field,
                key=f"{i}-{j}",
                on_click=handle_click,
                args=(i, j),
            )
    st.write(st.session_state)
    if st.session_state.winner:
        st.success(f"Congrats! {st.session_state.winner} won the game! 🎈")

    # count number of empty fields in board
    if countEmptyFields(st.session_state.board) == 0 and st.session_state.winner == None:
        st.warning("Game over! It's a draw! 🙈")


# count empty fields in board
def countEmptyFields(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                count += 1
    return count

# fill empty field with O


# def fillEmptyField(board):
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == '.':
#                 board[i][j] = 'O'
#                 return board


# bot move
def botMove(board):
    bestScore = -math.inf
    bestMove = 0
    

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                # st.write(board)
                score = minimax(board, countEmptyFields(board), False)
                # st.write("score", score)
                board[i][j] = '.'
                print("Preloop")
                if score > bestScore:
                    print("postloop")
                    bestScore = score
                # move = max(score, bestScore)
                    bestMove = [i, j]
                    print("here")
    board[bestMove[0]][bestMove[1]] = 'O'

    # print(board)
    # print(bestMove)
    # board[bestMove[0]][bestMove[1]] = 'O'


def minimax(board, depth, isMaximizing):
    result = checkWin(board)
    if result != None:
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        else:
            return 0

    if st.session_state.player == 'O':
        isMaximizing = True
    
    if isMaximizing:
        bestScore = -math.inf
   
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    score = minimax(board,depth+1, False)
                    # st.write("score", score)
                    board[i][j] = '.'
                    bestScore = max(score, bestScore)
        # st.write("Best Score", bestScore)
        return bestScore
    else:
        bestScore = math.inf
    
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    score = minimax(board,depth+1, True)
                    board[i][j] = '.'
                    bestScore = min(score, bestScore)
        # st.write("Min_score", bestScore)
        return bestScore


if __name__ == '__main__':
    tictactoe()

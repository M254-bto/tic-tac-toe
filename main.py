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
        st.session_state.winner = None

    # Define callbacks to handle button clicks.
    def handle_click(i, j):
        if not st.session_state.winner:
            st.session_state.board[i, j] = st.session_state.next_player
            st.session_state.next_player = (
                "O" if st.session_state.next_player == "X" else "X"
            )
            if st.session_state.next_player == "O":
                    minmax(1, st.session_state.board, True)
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

    #count number of empty fields in board
    
    #if count == 0:
    #    st.write("It's a draw!")
    

#count empty fields in board
def countEmptyFields(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                count += 1
    return count

#fill empty field with O
def fillEmptyField(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                return board


def minmax(depth, board, isMaximizer):
    global counter
    winner = st.session_state.winner
    if winner:
        counter += 1
        if winner == 'X':
            return -10 + depth
        elif winner == 'O':
            return 10 +depth
        else:
            return 0

    if isMaximizer:
        bestScore = -100
        for i in range(countEmptyFields(st.session_state.board)):
            newBoard = np.copy(st.session_state.board)
            index = fillEmptyField(newBoard)
            eval = minmax(depth -1, newBoard, False)
            if eval > bestScore:
                bestScore = eval
                bestMove = index
        if depth == 0:
             return bestMove
        return bestScore
    else:
        bestScore = 100
        for i in range(countEmptyFields(st.session_state.board)):
            newBoard = np.copy(st.session_state.board)
            index = fillEmptyField(newBoard)
            eval = minmax(depth - 1, newBoard, True)
            if eval < bestScore:
                bestScore = eval
                bestMove = index
        if depth == 0:
            return bestMove
        return bestScore
        




if __name__ == '__main__':
    tictactoe()

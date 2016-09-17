#!/usr/bin/python3

WHITE = 0
BLACK = 1
EMPTY = 2
# PIECE[WHITE] = "X"
# PIECE[BLACK] = "O"
# PIECE[EMPTY] = "."
PIECE=["X", "O", "."]

class Board():
    def __init__(self, myColor):
        self.myColor = myColor
        self.opponentColor = 1 - myColor
        self.board = list()
        for i in range(8):
            self.board.append([EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY])
        self.board[3][3] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[4][4] = WHITE
        # score[WHITE] = 2
        # score[BLACK] = 2
        self.score = [2, 2]
        self.filledSquares = 4

    def printBoard(self):
        print("\n[INFO] Current board:")
        print("  ", end="")
        for i in range(8):
            print(i, end=" ")
        print("\n  ", end="")
        for i in range(8):
            print("_", end=" ")
        print("")
        for i in range(8):
            print(i, end="|")
            for j in range(8):
                if self.board[i][j] == WHITE:
                    print(PIECE[WHITE], end="")
                elif self.board[i][j] == BLACK:
                    print(PIECE[BLACK], end="")
                elif self.board[i][j] == EMPTY:
                    print(PIECE[EMPTY], end="")
                if j == 7:
                    print("|", end="")
                else:
                    print(" ", end="")
                if i == 2 and j == 7:
                    print("\tScoreboard:", end="")
                if i == 3 and j == 7:
                    print("\tWhite", end="")
                    if self.myColor == WHITE:
                        print(" (You)", end="")
                    print(": " + str(self.score[WHITE]), end="")
                if i == 4 and j == 7:
                    print("\tBlack", end="")
                    if self.myColor == BLACK:
                        print(" (You)", end="")
                    print(": " + str(self.score[BLACK]), end="")
            print("")
        print("  ", end="")
        for i in range(8):
            print("~", end=" ")
        print("")

    def getFinalScore(self):
        print("\nScoreboard:")
        print("White", end="")
        if self.myColor == WHITE:
            print(" (You)", end="")
        print(": " + str(self.score[WHITE]))
        print("Black", end="")
        if self.myColor == BLACK:
            print(" (You)", end="")
        print(": " + str(self.score[BLACK]))
        if self.score[self.myColor] > self.score[self.opponentColor]:
            print("\t\tYou Win!!")
        elif self.score[self.myColor] < self.score[self.opponentColor]:
            print("\t\tYou Lost!!")
        else:
            print("\t\tIt's a tie!!")

    def isBoardFull(self):
        if self.filledSquares == 64:
            return True
        else:
            return False

    def validateMove(self, move):
        if len(move) == 2:
            if move == "-1":
                return 100

            validMoves = self.legalMoves()
            try:
                validMoves.index(move)
                return move
            except Exception as e:
                return -1
        else:
            return -1

    def legalMoves(self):
        moves = list()
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == self.myColor:
                    opponentPiecePresent = False

                    # Check for vertical moves
                    for x in range(i - 1, -1, -1):
                        if self.board[x][j] == self.opponentColor:
                            opponentPiecePresent = True
                        if opponentPiecePresent and self.board[x][j] == EMPTY:
                            moves.append(str(x) + str(j))
                            opponentPiecePresent = False
                            break
                    for x in range(i + 1, 8):
                        if self.board[x][j] == self.opponentColor:
                            opponentPiecePresent = True
                        if opponentPiecePresent and self.board[x][j] == EMPTY:
                            moves.append(str(x) + str(j))
                            opponentPiecePresent = False
                            break

                    # Check for horizontal moves
                    for y in range(j - 1, -1, -1):
                        if self.board[i][y] == self.opponentColor:
                            opponentPiecePresent = True
                        if opponentPiecePresent and self.board[i][y] == EMPTY:
                            moves.append(str(i) + str(y))
                            opponentPiecePresent = False
                            break
                    for y in range(j + 1, 8):
                        if self.board[i][y] == self.opponentColor:
                            opponentPiecePresent = True
                        if opponentPiecePresent and self.board[i][y] == EMPTY:
                            moves.append(str(i) + str(y))
                            opponentPiecePresent = False
                            break

                    # Check for moves on main diagoanl
                    for p in range(1, 8):
                        if i - p >= 0 and j - p >= 0:
                            if self.board[i - p][j - p] == self.opponentColor:
                                opponentPiecePresent = True
                            if opponentPiecePresent and self.board[i - p][j - p] == EMPTY:
                                moves.append(str(i - p) + str(j - p))
                                opponentPiecePresent = False
                                break
                        else:
                            break
                    for p in range(1, 8):
                        if i + p <= 7 and j + p <=7:
                            if self.board[i + p][j + p] == self.opponentColor:
                                opponentPiecePresent = True
                            if opponentPiecePresent and self.board[i + p][j + p] == EMPTY:
                                moves.append(str(i + p) + str(j + p))
                                opponentPiecePresent = False
                                break
                        else:
                            break

                    # Check for moves on anti-diagonal
                    for p in range(1, 8):
                        if i + p <= 7 and j - p >= 0:
                            if self.board[i + p][j - p] == self.opponentColor:
                                opponentPiecePresent = True
                            if opponentPiecePresent and self.board[i + p][j - p] == EMPTY:
                                moves.append(str(i + p) + str(j - p))
                                opponentPiecePresent = False
                                break
                        else:
                            break
                    for p in range(1, 8):
                        if i - p >= 0 and j + p <=7:
                            if self.board[i - p][j + p] == self.opponentColor:
                                opponentPiecePresent = True
                            if opponentPiecePresent and self.board[i - p][j + p] == EMPTY:
                                moves.append(str(i - p) + str(j + p))
                                opponentPiecePresent = False
                                break
                        else:
                            break
        return moves

    def updateBoard(self, move):
        # TODO
        pass

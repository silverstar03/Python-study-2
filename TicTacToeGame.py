# GUI 프로젝트 할 때 Qt 사용해보기

import tkinter
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.current_turn = "O"
        self.board = ["."] * 9

    def get(self, row, col):
        return self.board[(row * 3) + col] #[[".", ".", "."], [".", ".", "."], [".", ".", "."]]

    def check_winner(self):
        check = self.current_turn
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check \
                or self.get(0,i) == self.get(1,i) == self.get(2, i) == check:
                return check

        if(self.get(0, 0) == self.get(1,1) == self.get(2, 2) == check) \
            or (self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check):
            return check

        if not "." in self.board:
            return "d"

    def set(self, row, col):
        if self.get(row, col) == ".":
            self.current_turn = "X" if self.current_turn == "O" else "O"
            self.board[(row * 3) + col] = self.current_turn

    def __str__(self):
        s = ""
        for i, v in enumerate(self.board):
            s += v
            if i % 3 == 2:
                s += "\n"
        return s

# ttt = TicTacToe()
# ttt.set(0, 0)
# ttt.set(1, 1)
# ttt.set(1, 0)
# ttt.set(2,2)
# ttt.set(2,0)
#
# print(ttt)
# print(ttt.check_winner())
#
# ttt2 = TicTacToe()
# ttt2.set(0,0) #X
# ttt2.set(0,1) #O
# ttt2.set(0,2) #X
# ttt2.set(1,1) #O
# ttt2.set(1,0) #X
# ttt2.set(1,2) #O
# ttt2.set(2,1) #X
# ttt2.set(2,0) #O
# ttt2.set(2,2) #X
#
#
# print(ttt2)
# print(ttt2.check_winner())

class GameManager_GUI:
    def __init__(self):
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE / 3 #하나의 O나X가 들어갈 크기

        self.root = tkinter.Tk() #하나의 창 정보가 저장
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE))
        #원래는 self.root.geometry("300X300")처럼 숫자를 문자열에 넣어서 사이즈를 정함
        self.root.resizable(width=False, height=False) #창크기 고정
        self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)

        self.canvas.pack()
        self.images = dict()
        self.images["O"] = tkinter.PhotoImage(file="o.gif")
        self.images["X"] = tkinter.PhotoImage(file="x.gif")

        self.ttt = TicTacToe()
        self.canvas.bind("<Button-1>", self.click_handler)
        #<Button-1>는 아마도 왼쪽 마우스 클릭

    def click_handler(self, event):
        self.ttt.set(
            math.floor(event.y / self.TILE_SIZE), #소숫점 뒷자리를 제외하고 0~299를 100으로 나눠줌
            math.floor(event.x / self.TILE_SIZE))

        self.draw_board()

        self.winner = self.ttt.check_winner()
        if self.winner == "O":
            messagebox.showinfo("Game Over", "O가 이겼습니다.")
            self.root.quit()
        elif self.winner == "X":
            messagebox.showinfo("Game Over", "X가 이겼습니다.")
            self.root.quit()
        elif self.winner == "d":
            messagebox.showinfo("Game Over", "무승부입니다.")
            self.root.quit()


    def draw_board(self):
        self.canvas.delete("all")

        SIZE = 100
        x = 0
        y = 0
        for i, v in enumerate(self.ttt.board):
            if v == ".":
                pass
            elif v == "O":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["O"])

            elif v == "X":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["X"])

            #아홉개의 사진을 좌표를 이동시키면서 출력해주기 위한 코드
            x += SIZE
            if i % 3 == 2:
                x = 0
                y += SIZE

    def play(self):
        self.root.mainloop()

if __name__=='__main__':
    gm = GameManager_GUI()
    gm.play()


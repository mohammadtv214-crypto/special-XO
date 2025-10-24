import tkinter as tk
from tkinter import messagebox

class XO:
    def __init__(self):
        # ساخت پنجره اصلی
        self.root = tk.Tk()
        self.root.title("بازی XO رنگی")
        self.root.geometry("300x350")

        # بازیکن فعلی
        self.currentPlayer = 'X'

        # ساخت جدول 3x3
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # برچسب نمایش نوبت بازیکن
        self.label = tk.Label(self.root, text=f"نوبت بازیکن: {self.currentPlayer}", font=('Arial', 14))
        self.label.pack(pady=10)

        # قاب برای دکمه‌ها
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # ساخت دکمه‌ها
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame, text=' ', width=8, height=3, font=('Arial', 16),
                                command=lambda r=i, c=j: self.onClick(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        # دکمه شروع دوباره
        self.reset_btn = tk.Button(self.root, text="شروع دوباره", font=('Arial', 12), command=self.reset)
        self.reset_btn.pack(pady=10)

        self.root.mainloop()

    # کلیک روی خانه
    def onClick(self, row, col):
        if self.board[row][col] != ' ':
            messagebox.showwarning("اخطار", "این خانه پر است!")
            return

        # قرار دادن X یا O
        self.board[row][col] = self.currentPlayer
        self.buttons[row][col]['text'] = self.currentPlayer

        # تعیین رنگ بر اساس بازیکن
        if self.currentPlayer == 'X':
            self.buttons[row][col]['fg'] = 'blue'
        else:
            self.buttons[row][col]['fg'] = 'red'

        # بررسی برد
        if self.checkWin():
            messagebox.showinfo("پایان بازی", f"🎉 بازیکن {self.currentPlayer} برنده شد!")
            self.disableButtons()
            return

        # بررسی مساوی
        if self.checkDraw():
            messagebox.showinfo("پایان بازی", "😐 بازی مساوی شد!")
            self.disableButtons()
            return

        # تغییر نوبت
        self.currentPlayer = 'O' if self.currentPlayer == 'X' else 'X'
        self.label.config(text=f"نوبت بازیکن: {self.currentPlayer}")

    # بررسی برنده
    def checkWin(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != ' ':
                return True
            if b[0][i] == b[1][i] == b[2][i] != ' ':
                return True
        if b[0][0] == b[1][1] == b[2][2] != ' ':
            return True
        if b[0][2] == b[1][1] == b[2][0] != ' ':
            return True
        return False

    # بررسی مساوی
    def checkDraw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    # غیرفعال کردن دکمه‌ها
    def disableButtons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'

    # ریست بازی
    def reset(self):
        self.currentPlayer = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ' '
                self.buttons[i][j]['state'] = 'normal'
                self.buttons[i][j]['fg'] = 'black'
        self.label.config(text=f"نوبت بازیکن: {self.currentPlayer}")

# اجرای بازی
XO()

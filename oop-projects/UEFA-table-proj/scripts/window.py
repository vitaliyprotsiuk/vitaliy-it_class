import tkinter

from scripts.tournament import Tournament

class Window:
    def __init__(self, teams, games):
        self.window = tkinter.Tk()
        self.__var = tkinter.StringVar(value="1")
        self.__teams = teams
        self.__games = games
        self.tournament = Tournament(self.__games, self.__teams)

    def start_window(self):
        self.window.title("UEFA Table")
        self.window.geometry("600x400+450+200")
        self.window.resizable(False, False)
        

        self.__print_or_add()


        self.window.mainloop()


    def __checking(self):
        self.__print_table if self.__var == "1" else print(1)


    def __print_or_add(self):
        def __button_clicked():
            print_rb.destroy()
            add_game_rb.destroy()
            continue_button.destroy()

            if self.__var.get() == '1':
                self.__print_table()


        print_rb = tkinter.Radiobutton(self.window, text="Показати таблицю", variable=self.__var, value="1")
        print_rb.grid(row=0, column=0)
        add_game_rb = tkinter.Radiobutton(self.window, text="Додати гру", variable=self.__var, value="2")
        add_game_rb.grid(row=1, column=0)
        
        continue_button = tkinter.Button(self.window, text="Продовжити", command=__button_clicked)
        continue_button.grid(row=2, column=0)


    def __print_table(self):
        main_label_names = ['Назва команди                ', '| В', '| Н', '| П', '| О']
        main_labels = []
        for i in range(0, len(main_label_names)):
            main_label = tkinter.Label(self.window, text=main_label_names[i], font=("Arial", 20, "bold"))
            main_label.grid(row=0, column=i)

            main_labels.append(main_label)

        names = self.tournament.get_list_of_teams()
        wins = self.tournament.get_list_of_wins()
        draws = self.tournament.get_list_of_draws()
        loses = self.tournament.get_list_of_loses()
        points = self.tournament.get_list_of_points()

        items = []
        for i in range(0, len(names)):
            name = tkinter.Label(self.window, text=names[i], font=("Arial", 20))
            name.grid(row=i+1, column=0, sticky='w')
            win = tkinter.Label(self.window, text=f"| {wins[i]}", font=("Arial", 20))
            win.grid(row=i+1, column=1)
            draw = tkinter.Label(self.window, text=f"| {draws[i]}", font=("Arial", 20))
            draw.grid(row=i+1, column=2)
            lose = tkinter.Label(self.window, text=f"| {loses[i]}", font=("Arial", 20))
            lose.grid(row=i+1, column=3)
            point = tkinter.Label(self.window, text=f"| {points[i]}", font=("Arial", 20))
            point.grid(row=i+1, column=4)

            items.append(name)
            items.append(win)
            items.append(draw)
            items.append(lose)
            items.append(point)
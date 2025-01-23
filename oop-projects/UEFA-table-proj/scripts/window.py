import tkinter


from data.config import *
from scripts.tournament import Tournament


class Window:
    def __init__(self, teams, games):
        self.window = tkinter.Tk()
        self.__var = tkinter.StringVar(value='1')
        self.__teams = teams
        self.__games = games
        self.tournament = Tournament(self.__games, self.__teams)


    def start_window(self):
        self.window.title("UEFA Table")
        self.window.geometry("600x400+450+200") # for 1920x1080
        self.window.resizable(False, False)

        self.__print_or_add()

        self.window.mainloop()


    def __checking(self):
        return self.__print_table() if self.__var.get() == "1" else self.__add_command()


    def __print_or_add(self):
        def __button_clicked():
            print_rb.destroy()
            add_game_rb.destroy()
            continue_button.destroy()

            self.__checking()


        print_rb = tkinter.Radiobutton(self.window, text="Показати таблицю", variable=self.__var, value="1")
        print_rb.grid(row=0, column=0)
        add_game_rb = tkinter.Radiobutton(self.window, text="Додати гру", variable=self.__var, value="2")
        add_game_rb.grid(row=1, column=0)
        
        continue_button = tkinter.Button(self.window, text="Продовжити", command=__button_clicked)
        continue_button.grid(row=2, column=0)


    def __print_table(self):
        def __back_clicked():
            for item in items:
                item.destroy()

            for main in main_labels:
                main.destroy()

            self.__print_or_add()

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

        back_button = tkinter.Button(self.window, text='Назад до Головного меню', command=__back_clicked)
        back_button.grid(row=i+2)

        items.append(back_button)


    def __add_command(self):
        def __write_game():
            for inputed in entries:
                try:
                    a = int(inputed.get())
                except ValueError:
                    print(1)
                    return           
            with open(GAMES_PATH, 'a') as game:
                game.write(f"\n{id_entry.get()} {home_name_entry.get()} {away_name_entry.get()} {home_score_entry.get()} {away_score_entry.get()}")
            for item in items:
                item.destroy()


            done_label = tkinter.Label(self.window, text='Готово✅', font=('Arial', 25))
            done_label.grid(row=0)

        main_label = tkinter.Label(self.window, text="Введіть дані гри", font=('Arial', 17))
        main_label.grid(row=0)

        id_label = tkinter.Label(self.window, text='Введіть id гри', font=('Arial', 13))
        id_label.grid(row=1, column=0, sticky='w')
        id_entry = tkinter.Entry(self.window)
        id_entry.grid(row=1, column=1)
        home_name_label = tkinter.Label(self.window, text='Введіть id домашньої команди', font=('Arial', 13))
        home_name_label.grid(row=2, column=0, sticky='w')
        home_name_entry = tkinter.Entry(self.window)
        home_name_entry.grid(row=2, column=1)
        away_name_label = tkinter.Label(self.window, text='Введіть id гостьової команди', font=('Arial', 13))
        away_name_label.grid(row=3, column=0, sticky='w')
        away_name_entry = tkinter.Entry(self.window)
        away_name_entry.grid(row=3, column=1)
        home_score_label = tkinter.Label(self.window, text='Введіть забиті голи домашньої команди', font=('Arial', 13))
        home_score_label.grid(row=4, column=0, sticky='w')
        home_score_entry = tkinter.Entry(self.window)
        home_score_entry.grid(row=4, column=1)
        away_score_label = tkinter.Label(self.window, text='Введіть забиті голи гостьової команди', font=('Arial', 13))
        away_score_label.grid(row=5, column=0, sticky='w')
        away_score_entry = tkinter.Entry(self.window)
        away_score_entry.grid(row=5, column=1)

        continue_button = tkinter.Button(self.window, text="Продовжити", command=__write_game)
        continue_button.grid(row=6)


        entries = [id_entry, home_name_entry, home_score_entry, away_name_entry, away_score_entry]
        items = [main_label, id_label, id_entry, home_name_entry, home_name_label, away_name_entry, away_name_label, away_score_entry, away_score_label, home_score_entry, home_score_label, continue_button]
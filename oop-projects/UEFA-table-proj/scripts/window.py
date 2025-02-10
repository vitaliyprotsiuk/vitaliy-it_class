import tkinter
import tkinter.messagebox


from scripts.read_files import read_games, read_teams
from tkinter import ttk
from data.config import *
from scripts.tournament import Tournament


class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.__tab_control = ttk.Notebook(self.window)
        self.__tab_control.bind("<ButtonRelease-1>", self.__update_info) # to update info in table when tab changed
        self.__first_tab = ttk.Frame(self.__tab_control)
        self.__second_tab = ttk.Frame(self.__tab_control)

        # addition tabs
        self.__tab_control.add(self.__first_tab, text='Турнірна таблиця')
        self.__tab_control.add(self.__second_tab, text='Додати гру')

        self.__tab_control.grid()

        # start window
        self.manage_window()

    def __update_info(self, event=None):
        for item in self.__items:
            item.destroy()
        
        self.__print_table()

        return "break"

    def manage_window(self):
        self.window.title("UEFA Table")
        self.window.geometry("600x400+450+200") # for 1920x1080
        self.window.resizable(False, False)

        self.__print_table()
        self.__add_command()

        self.window.mainloop()


    def __print_table(self):
        self.__teams = read_teams()
        self.__games = read_games(self.__teams)
        self.tournament = Tournament(self.__games, self.__teams)
        self.__home_team_var = tkinter.StringVar(value=self.__teams[0])
        self.__away_team_var = tkinter.StringVar(value=self.__teams[1])
        main_label_names = ['Назва команди                ', '| В', '| Н', '| П', '| О']
        main_labels = []
        for i in range(0, len(main_label_names)):
            main_label = tkinter.Label(self.__first_tab, text=main_label_names[i], font=("Arial", 20, "bold"))
            main_label.grid(row=0, column=i)

            main_labels.append(main_label)

        names = self.tournament.get_list_of_teams()
        wins = self.tournament.get_list_of_wins()
        draws = self.tournament.get_list_of_draws()
        loses = self.tournament.get_list_of_loses()
        points = self.tournament.get_list_of_points()

        self.__items = []
        for i in range(0, len(names)):
            name = tkinter.Label(self.__first_tab, text=names[i], font=("Arial", 20))
            name.grid(row=i+1, column=0, sticky='w')
            win = tkinter.Label(self.__first_tab, text=f"| {wins[i]}", font=("Arial", 20))
            win.grid(row=i+1, column=1)
            draw = tkinter.Label(self.__first_tab, text=f"| {draws[i]}", font=("Arial", 20))
            draw.grid(row=i+1, column=2)
            lose = tkinter.Label(self.__first_tab, text=f"| {loses[i]}", font=("Arial", 20))
            lose.grid(row=i+1, column=3)
            point = tkinter.Label(self.__first_tab, text=f"| {points[i]}", font=("Arial", 20))
            point.grid(row=i+1, column=4)

            self.__items.append(name)
            self.__items.append(win)
            self.__items.append(draw)
            self.__items.append(lose)
            self.__items.append(point)


    def __add_command(self):
        def __get_id_by_team(self, team):
            for finded_team in self.__teams:
                if team == finded_team.get_name():
                    return finded_team.get_id()


        def __write_game():
            def __continue_clicked():
                for item in self.__items_adding:
                    item.destroy()
                continue_button.destroy()
                self.__add_command()


            for inputed in entries:
                try:
                    a = int(inputed.get())
                except:
                    tkinter.messagebox.showerror("Помилка", "Ви ввели не валідні дані")
                    return
                
            with open(GAMES_PATH, 'a') as game:
                game.write(f"\n{id_entry.get()} {__get_id_by_team(self, self.__home_team_var.get())} {__get_id_by_team(self, self.__away_team_var.get())} {home_score_entry.get()} {away_score_entry.get()}")
            
            for item in self.__items_adding:
                item.destroy()
            
            done_label = tkinter.Label(self.__second_tab, text='Готово✅', font=('Arial', 15))
            done_label.grid(row=0)

            continue_button = tkinter.Button(self.__second_tab, text='Продовжити', font=('Arial', 9), command=__continue_clicked)
            continue_button.grid(row=1)


        main_label = tkinter.Label(self.__second_tab, text="Введіть дані гри", font=('Arial', 17))
        main_label.grid(row=0)

        id_label = tkinter.Label(self.__second_tab, text='Введіть id гри', font=('Arial', 13))
        id_label.grid(row=1, column=0, sticky='w')
        id_entry = tkinter.Entry(self.__second_tab)
        id_entry.grid(row=1, column=1)
        home_name_label = tkinter.Label(self.__second_tab, text='Виберіть назву домашньої команди', font=('Arial', 13))
        home_name_label.grid(row=2, column=0, sticky='w')
        home_name_dropdown = tkinter.OptionMenu(self.__second_tab, self.__home_team_var, *self.__teams)
        home_name_dropdown.grid(row=2, column=1)
        away_name_label = tkinter.Label(self.__second_tab, text='Виберіть назву гостьової команди', font=('Arial', 13))
        away_name_label.grid(row=3, column=0, sticky='w')
        away_name__dropdown = tkinter.OptionMenu(self.__second_tab, self.__away_team_var, *self.__teams)
        away_name__dropdown.grid(row=3, column=1)
        home_score_label = tkinter.Label(self.__second_tab, text='Введіть забиті голи домашньої команди', font=('Arial', 13))
        home_score_label.grid(row=4, column=0, sticky='w')
        home_score_entry = tkinter.Entry(self.__second_tab)
        home_score_entry.grid(row=4, column=1)
        away_score_label = tkinter.Label(self.__second_tab, text='Введіть забиті голи гостьової команди', font=('Arial', 13))
        away_score_label.grid(row=5, column=0, sticky='w')
        away_score_entry = tkinter.Entry(self.__second_tab)
        away_score_entry.grid(row=5, column=1)

        continue_button = tkinter.Button(self.__second_tab, text="Продовжити", command=__write_game)
        continue_button.grid(row=6)


        entries = [id_entry, home_score_entry, away_score_entry]
        self.__items_adding = [main_label, id_label, id_entry, home_name_dropdown, away_name__dropdown, home_name_label, away_name_label, away_score_entry, away_score_label, home_score_entry, home_score_label, continue_button]

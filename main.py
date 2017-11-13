from Views.MainView import MainView
class MainApp():
    def __init__(self):
        self.__master = MainView()
        self.__master.protocol("WM_DELETE_WINDOW")

    def run(self):
        self.__master.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.run()
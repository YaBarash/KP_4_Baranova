class UserInput:
    def __init__(self, user_input):
        self.user_input = user_input

    def search_vacation(self):
        if self.user_input == 1:
            print('1. Поиск вакансии')
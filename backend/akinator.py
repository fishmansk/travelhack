messagesd = [
    "Вам подходит пляжный отдых?",
    "Вы готовы к длительному перелёту?",
    "Хотите преобщиться к местной культуре?",
    "Хотите посетить страну с безвизовым режимом?",
    "Хотите поднфться в горы?",
    "Хотите попробовать итальянскую пиццу в оригинале?",
    "Вы предпочтёте Европе Азию?",
    "Вы знаете к какой кухне относятся роллы?",
    "Вас привлекает запах круасанов по утрам?",
    "Мексика",
    "Доминиканская Республика",
    "Турция",
    "Болгария",
    "Италия",
    "Австрия",
    "Япония",
    "Китай",
    "Франция",
    "Англия"
]


def state_is_country(state):
    return state > 7

def check_yes(s):
    s = s.lower()
    return s in ['yes', 'y', 'да', 'так точно', 'конечно', '+', '1', 'true']

def check_no(s):
    s = s.lower()
    return s in ['no', 'n', 'нет', 'ноу', '-', '0', 'false']


class Akinator():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Akinator, cls).__new__(cls)

    def query(self, state=0, answer="+"):
        if state == 0:
            return 1
        elif (state == 1) or (answer == "+"):
            return 2
        elif (state == 1) or (answer == "-"):
            return 5

        elif (state == 2) or (answer == "+"):
            return 3
        elif (state == 2) or (answer == "-"):
            return 4

        elif (state == 3) or (answer == "+"):
            return 10
        elif (state == 3) or (answer == "-"):
            return 11

        elif (state == 4) or (answer == "+"):
            return 12
        elif (state == 4) or (answer == "-"):
            return 13

        elif (state == 5) or (answer == "+"):
            return 6
        elif (state == 5) or (answer == "-"):
            return 7

        elif (state == 6) or (answer == "+"):
            return 14
        elif (state == 6) or (answer == "-"):
            return 15

        elif (state == 7) or (answer == "+"):
            return 8
        elif (state == 7) or (answer == "-"):
            return 9

        elif (state == 8) or (answer == "+"):
            return 16
        elif (state == 8) or (answer == "-"):
            return 17

        elif (state == 9) or (answer == "+"):
            return 18
        elif (state == 9) or (answer == "-"):
            return 19
        else:
            return 0

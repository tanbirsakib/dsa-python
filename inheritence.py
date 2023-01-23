class Athelete:
    def __init__(self, o):
        self.occupation = 'athelete'
    def general_name(self):
        print('He is athelete')
class Footballer(Athelete):
    def __init__(self, n, c):
        self.name = n
        self.club = c
    def occupation(self):
        self.general_name()
class Criecketer(Athelete):
    def __init__(self, n, c):
        self.name = n
        self.club = c
messi = Footballer('messi', 'psg')
sakib = Criecketer('sakib', 'dhaka')
print(messi.club)
messi.occupation()
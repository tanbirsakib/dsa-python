class Footballer:
    def __init__(self, n, c, b):
        self.name = n
        self.club = c
        self.ballondeer = b
    def bestPlayer(self):
        if self.name == 'messi':
            print(f"{self.name} is the best player")
        else:
            print(f"{self.name} is the best player")
    def ballon(self):
        if self.ballondeer == 7:
            print(f"{self.name} won the maximum ballon d'or")
        else: print('he is the second best ballon wooner in the world')
    def leftClub(self):
        print(f"{self.name} left the club {self.club}")

messi = Footballer('messi', 'barcelona', 7)
messi.bestPlayer()
messi.ballon()
ronaldo = Footballer('ronaldo', 'real madrid', 5)
ronaldo.leftClub()
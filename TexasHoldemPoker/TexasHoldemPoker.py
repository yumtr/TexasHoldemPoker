from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random


class TexasHoldemPoker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem Poker")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.shared = Player("shared")
        self.betMoney = 10
        self.playerMoney = 990
        self.nCardsShared = 0
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.LcardsShared = []
        self.deckN = 0
        self.round = 0
        self.window.mainloop()

    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        # self.test = Button(self.window, text="test", width=6, height=1, font=self.fontstyle2, command=self.checkWinner)
        # self.test.place(x=500, y=500)
        # self.test["state"] = "active"
        # self.test["bg"] = "white"
        #
        # self.test2 = Button(self.window, text="test2", width=6, height=1, font=self.fontstyle2, command=self.hitShared)
        # self.test2.place(x=400, y=500)
        # self.test2["state"] = "active"
        # self.test2["bg"] = "white"

    def setupLabel(self):
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $990", width=15, height=1, font=self.fontstyle, bg="green",
                                  fg="orange")
        self.LplayerMoney.place(x=500, y=450)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=500, y=240)
        self.LplayerRank = Label(text="", width=10, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerRank.place(x=300, y=380)
        self.LdealerRank = Label(text="", width=10, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LdealerRank.place(x=300, y=100)

    def pressedCheck(self):
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            #PlaySound('sounds/chip.wav', SND_FILENAME)

    def pressedBx1(self):
        bm = self.betMoney
        self.betMoney += bm
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= bm
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            #PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= bm

    def pressedBx2(self):
        bm = self.betMoney * 2
        self.betMoney += bm
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= bm
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            #PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= bm

    def deal(self):
        if self.round == 0:
            self.player.reset()
            self.dealer.reset()  # 카드 덱 52장 셔플링 0,1,,.51
            self.shared.reset()
            self.cardDeck = [i for i in range(52)]
            random.shuffle(self.cardDeck)
            self.deckN = 0
            self.hitPlayer(0)
            self.hitDealerDown(0)
            self.hitPlayer(1)
            self.hitDealerDown(1)

        if self.round == 6:
            self.checkWinner()
        else:
            if self.round >= 1:
                self.hitShared()
            self.round += 1
            self.Check['state'] = 'active'
            self.Check['bg'] = 'white'
            self.Bx1['state'] = 'active'
            self.Bx1['bg'] = 'white'
            self.Bx2['state'] = 'active'
            self.Bx2['bg'] = 'white'
            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50 + n * 80, y=350)

    def hitDealerDown(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + n * 80, y=70)
        #PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitShared(self):
        self.nCardsShared += 1
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.shared.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsShared.append(Label(self.window, image=p))
        self.LcardsShared[self.shared.inHand() - 1].image = p
        self.LcardsShared[self.shared.inHand() - 1].place(x=80 + self.nCardsShared * 80, y=210)
        #PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def pressedDeal(self):
        self.deal()

    def pressedAgain(self):
        self.Lstatus.configure(text="")
        self.LplayerRank.configure(text="")
        self.LdealerRank.configure(text="")
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.betMoney = 10
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.playerMoney -= 10
        self.nCardsShared = 0
        for t in self.LcardsShared:
            t.destroy()
        for t in self.LcardsPlayer:
            t.destroy()
        for t in self.LcardsDealer:
            t.destroy()
        self.LcardsDealer = []
        self.LcardsPlayer = []
        self.LcardsShared = []
        self.deckN = 0
        self.round = 0
        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'white'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        for i in range(2):
            p = PhotoImage(file="cards/" + self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        self.LplayerRank.configure(text="플레이어 족보")
        self.LdealerRank.configure(text="딜러 족보")

        if self.player.value() > 21:
            self.Lstatus.configure(text="Player Busts")
            #PlaySound('sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21:
            self.Lstatus.configure(text="Dealer Busts")
            self.playerMoney += self.betMoney * 2
            #PlaySound('sounds/win.wav', SND_FILENAME)
        elif self.dealer.value() == self.player.value():
            self.Lstatus.configure(text="Push", fg="red")
            self.playerMoney += self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text="Win", fg="red")
            self.playerMoney += self.betMoney * 2
            #PlaySound('sounds/win.wav', SND_FILENAME)
        else:
            self.Lstatus.configure(text="Lose", fg="red")
            #PlaySound('sounds/wrong.wav', SND_FILENAME)

        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


TexasHoldemPoker()

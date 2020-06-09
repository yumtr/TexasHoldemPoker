# coding=utf-8
from Card import *


def Count(dice, number):
    return len([y for y in dice if y == number])


def HighestRepeated(dice, minRepeats):
    unique = set(dice)
    repeats = [x for x in unique if Count(dice, x) >= minRepeats]
    return max(repeats) if repeats else 0


def OfAKind(d, n):
    dice = [d[i].getRoll() for i in range(5)]
    return HighestRepeated(dice, n) * n


class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
               "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
               "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    def getConfigs():  # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

    def score(row, d):  # 정적 메소드: 객체생성 없이 사용 가능
        # row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
        # 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
        # 않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
        # -1을 반환합니다.
        if row >= 0 and row <= 5:
            return Configuration.scoreUpper(d, row + 1)
        elif row == 8:
            return Configuration.scoreThreeOfAKind(d)
        elif row == 9:
            return Configuration.scoreFourOfAKind(d)
        elif row == 10:
            return Configuration.scoreFullHouse(d)
        elif row == 11:
            return Configuration.scoreSmallStraight(d)
        elif row == 12:
            return Configuration.scoreLargeStraight(d)
        elif row == 13:
            return Configuration.scoreYahtzee(d)
        else:  # UPPER_TOTAL, UPPER_BONUS, LOWER_TOTAL, TOTAL
            return Configuration.sumDie(d)

    def scoreUpper(d, num):  # 정적 메소드: 객체생성 없이 사용 가능
        # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
        # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.
        s = 0
        for i in range(5):
            if d[i].getRoll() == num:
                s += num
        return s

    def scoreThreeOfAKind(d):
        return OfAKind(d, 3)

    def scoreFourOfAKind(d):
        return OfAKind(d, 4)

    def scoreFullHouse(d):  # 25
        if OfAKind(d, 3):
            m = OfAKind(d, 3) / 3
            c = d[:]
            dice = [c[i].getRoll() for i in range(5)]
            dice.remove(m)
            dice.remove(m)
            dice.remove(m)
            if dice[0] == dice[1]:
                return 25
        return 0

    def scoreSmallStraight(d):  # 30
        # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
        # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
        dice = [d[i].getRoll() for i in range(5)]
        dice = list(set(dice))
        if len(dice) == 4:
            dice.sort()
            cmp1 = [1, 2, 3, 4]
            cmp2 = [2, 3, 4, 5]
            cmp3 = [3, 4, 5, 6]
            return 30 if dice == cmp1 or dice == cmp2 or dice == cmp3 else 0
        else:
            return 0

    def scoreLargeStraight(d):  # 40
        # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        cmp1 = [1, 2, 3, 4, 5]
        cmp2 = [2, 3, 4, 5, 6]
        dice = [d[i].getRoll() for i in range(5)]
        dice.sort()
        return 40 if dice == cmp1 or dice == cmp2 else 0

    def scoreYahtzee(d):  # 50
        dice = [d[i].getRoll() for i in range(5)]
        return 50 if len(set(dice)) == 1 else 0

    def sumDie(d):
        dice = [d[i].getRoll() for i in range(5)]
        return sum(dice)

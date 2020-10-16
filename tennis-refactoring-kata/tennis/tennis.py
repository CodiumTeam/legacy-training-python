# -*- coding: utf-8 -*-

class TennisGame:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if (self.has_same_score()):
            return self.calculate_same_score()
        elif (self.is_advantage()):
            return self.calculate_advantage_score()
        elif (self.is_winner()):
            return self.calculate_winning_player()
        else:
            return self.calculate_intermediate_scores()

    def calculate_intermediate_scores(self):
        return self.calculate_partial_score(self.p1points) + "-" + self.calculate_partial_score(self.p2points)

    def calculate_partial_score(self, tempScore):
        scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", }
        return scores[tempScore]

    def calculate_same_score(self):
        scores = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All", }
        return scores.get(self.p1points, "Deuce")

    def calculate_winning_player(self):
        minusResult = self.p1points - self.p2points
        if (minusResult >= 2):
            result = "Win for " + self.player1Name
        else:
            result = "Win for " + self.player2Name
        return result

    def calculate_advantage_score(self):
        minusResult = self.p1points - self.p2points
        if (minusResult == 1):
            return "Advantage " + self.player1Name
        elif (minusResult == -1):
            return "Advantage " + self.player2Name

    def is_advantage(self):
        return self.is_long_game() and abs(self.p1points - self.p2points) == 1

    def is_long_game(self):
        return self.p1points >= 4 or self.p2points >= 4

    def has_same_score(self):
        return self.p1points == self.p2points

    def is_winner(self):
        return self.is_long_game()

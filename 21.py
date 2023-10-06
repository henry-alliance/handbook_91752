import random


class Game():
    p_count = 0
    player_cards = {}
    __deck = []

    while True:
        # get valid player count
        try:
            p_count = int(input("Player Count (1-4): "))
            if p_count < 1 or p_count > 4:
                continue
            break
        except ValueError:
            continue



    __deck = [
        "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts",
        "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades",
        "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs",
        "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds"
    ]
    random.shuffle(__deck)
    player_cards = {f"player_{str(num+1)}":[] for num in range(p_count)}
    print(__deck)
    print()


    def hit(self, p_num: int):
        j = random.choice(self.__deck)
        self.player_cards["player_{}".format(str(p_num))].append(j)
        self.__deck.remove(j)


    def serve(self):
        
        for player in range(self.p_count):
            self.hit(player+1)


    def check_winner(self):
        temp_cards = self.player_cards.copy()
        non_num_card_values = {
            "Ace of Hearts": -100, "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5, "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9, "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10,
            "Ace of Spades": -100, "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5, "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10,
            "Ace of Clubs": -100, "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5, "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9, "10 of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10,
            "Ace of Diamonds": -100, "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5, "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9, "10 of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10
        }
        for player in temp_cards:
            for card in temp_cards[player]:
                if card in list(non_num_card_values):
                    card = non_num_card_values[card]
        
        print(temp_cards)
        # for player in temp_cards:
        #     score = sum(temp_cards[player])
        #     print(player, score)
game = Game()
print(game.p_count)
print(game.player_cards)
print(game.player_cards)
game.check_winner()

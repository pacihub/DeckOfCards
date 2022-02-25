# deckofcards

Deck of Cards

# the program represents a deck of cards such as one in a casino
# implemented entirely with object oriented programming

A Deck class that represents a deck ot 52 playing cards. The Deck maintains which cards are currently in the deck and never contain duplicate cards.
Cards are represented by a string containing their value (2 - 10, J, Q, K, A) followed by their suit (D, H, C, S).
Example: Jack of clubs would be represented by "JC" and the three of hearts would be "3H".

The Deck class has the following methods:
shuffle(): This method shuffles the cards randomly, in place. 

deal(n): This method removes and returns the last n cards from the deck in a list. If the deck does not contain enough cards it returns
all the cards in the deck.

sort_by_suit(): This method sorts all the cards by suit, placing all the hearts first, diamonds second, clubs third and spades last.
The order within each suit (i.e. card values) does not matter. This method sorts the cards in place, it does not return anything.

contains(card): This method returns True if the given card exists in the deck and False otherwise.

copy(): This method returns a new Deck object that is a copy of the current deck. Any modifications made to the new Deck object should not affect the Deck
object that was copied.

get_cards(): This method returns all the cards in the deck in a list. Any modifications to the returned list should not change the Deck object.

__len__(): This method returns the number of the cards in the Deck.

The Deck always starts with exactly 52 cards that are distributed across 4 suits and 13 values where there are NO duplicate cards.


Example behavior of the Deck:

=> d = Deck()

=> d.shuffle()

=> d.deal(3)

["AS", "2H", "4D"]

=> d.contains("4D")

False

=> d.sort_by_suit()

=> d.deal(3)

['2S', '5S', 'JS']

=> d.add_to_deck(["10H", "4D", "2S"])

=> len(d)

48

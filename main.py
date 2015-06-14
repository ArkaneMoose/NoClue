import euphoria as eu

help_text = """This bot was made by Neon and "my hands are typing words". For help or more detailed information on this game and the room, ask Stormageddon or Balakirev in &xkcd.

Commands:
!help @Noclue: Get help with @Noclue
!rules: Learn about the rules of Euphorian Cluedo
!roomlist: Displays the list of rooms you can navigate to
!weapons: Displays the list of murder weapons
!suspects: Displays the list of suspects for current game
!welcome: Displays the welcome message
!roll: Rolls the dice
!map: Displays the map of the board

This bot is open-source! View the source code at https://github.com/ArkaneMoose/NoClue"""

rules_text = """How to play:
There are different rooms, suspects, and murder weapons. To win the game, you must guess the murderer, the murder weapon, and the location of the murder correctly. The cards, which contain information about location, suspects, and weapons, are dealt at the beginning to each player in &noclue. The cards that no one has are the ones involved in the murder.

The most important part of the game is the 'suggestions'. To make a suggestion, you have to be 'in' a room. You can move to the next adjacent room by rolling a 5, and any room by rolling a 10 with @DnDRoller.
Once you're 'in' a room (you never really leave this one!), you make a suggestion from that room. For example: 'I am in &xkcd, and I suggest that it was @Balakirev in &xkcd with tweezers.'
The person after you looks at their 'cards' to see if they have any of the 3 you named. If they do, they announce that they have one, and go to &noclue to show it to the person who made the suggestion. They only have to show one card, even if they have more than one, and they ONLY show it to the person who made the suggestion. I recommend sharing clues by nick-haunting.

Peeking in &noclue while someone is showing cards is cheating.

If the person next in alphabetical order doesn't have any of the cards, they must say 'I don't have any'. Then the person NEXT in alphabetical order goes through the same process.
In the end, either the person who made the suggestion gets shown one (and only one) card, or everyone in the circle (except the suggester) announces that they don't have any."""

class NoclueBot(eu.ping_room.PingRoom, eu.chat_room.ChatRoom):
    def __init__(self, roomname, password=None):
        super().__init__(roomname, password)
    
        self.nickname = "Noclue"

    def handle_chat(self, message):
        if message["content"] == "!ping":
            self.send_chat("Pong!", message["id"])
        elif message["content"].lower() == "!help @" + self.nickname.replace(" ", "").lower():
            self.send_chat(help_text, message["id"])
        elif message["content"].lower() == "!rules":
            self.send_chat(rules_text, message["id"])

def main():
    noclue = NoclueBot("test")
    eu.executable.start(noclue)

if __name__ == "__main__":
    main()

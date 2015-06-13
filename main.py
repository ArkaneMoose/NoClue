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

class NoclueBot(eu.ping_room.PingRoom, eu.chat_room.ChatRoom):
    def __init__(self, roomname, password=None):
        super().__init__(roomname, password)
    
        self.nickname = "Noclue"

    def handle_chat(self, message):
        if message["content"] == "!ping":
            self.send_chat("Pong!", message["id"])
        elif message["content"].lower() == "!help @" + self.nickname.replace(" ", ""):
            self.send_chat("Hi there!", message["id"])

def main():
    noclue = NoclueBot("")
    eu.executable.start(noclue)

if __name__ == "__main__":
    main()

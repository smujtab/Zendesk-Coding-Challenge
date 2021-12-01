from beautifultable import BeautifulTable
from warnings import simplefilter
# ignore all future warnings since beauftifultable module raises FutureWarning that is irrelevant for this code
simplefilter(action='ignore', category=FutureWarning)

class Messages:
    def menu(self):
        menu = BeautifulTable()
        menu.column_headers = ["Command", "Action"]
        menu.append_row(["'single'", " View a single ticket"])
        menu.append_row(["'all'", " View all tickets"])
        menu.append_row(["'scroll'", " View next page of tickets"])
        menu.append_row(["'menu'", " View Menu"])
        menu.append_row(["'quit'", " Exit Ticket Viewer"])
        return "Here is our menu " + "\n" +str(menu)

    def invalidInput(self):
        message = "Invalid input, please try again"
        return message

    def welcome(self):
        message = "Welcome to Ticket Viewer!"
        return message

    def goodBye(self):
        message = "Thanks for using the Ticket Viewer"
        return message

    def command(self):
        return "Enter a command: "

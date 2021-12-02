from Classes import messages
from Classes.Tickets import Ticket
from Classes import Format

# Setting up all the required objects, links, and tokens
# Please enter your own OAuth access token here and your ticket api link as well
accessToken = '05fc1151b9e184e8c2a2b9b8ed51134614b4dd95b15be9f912fdfedf229a71b7'
url = "https://zccsyedmujtaba.zendesk.com/api/v2/tickets"
message_object = messages.Messages()
newTicket = Ticket.Ticket(accessToken, url)
ticketFormat = Format.Format()
print(messages.Messages().welcome())


def main():
    '''
    The main exception loop, continues to ask for commands and
    performs respective actions until 'quit' is entered
    '''
    command = input(messages.Messages().menu() + "\n" + "Enter A command: ")
    while command != "quit":
        if command == "all":
            print(ticketFormat.displayALlTIckets(newTicket.getAllTickets()))
        elif command == 'single':
            ticket_id = input("Enter Ticket ID: ")
            print(ticketFormat.displaySingleTicket(newTicket.getSingleTicket(ticket_id)))
        elif command == 'scroll':
            print(ticketFormat.displayALlTIckets(newTicket.Scroll()))
            print(newTicket.page)
        elif command == 'menu':
            print(message_object.menu())
        else:
            print(message_object.invalidInput())
        command = input(message_object.command())

    print(message_object.goodBye())


if __name__ == "__main__":
    main()

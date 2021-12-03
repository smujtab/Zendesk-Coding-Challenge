from Classes import messages
from Classes.Tickets import Ticket
from Classes import Format
import requests

# Setting up all the required objects, links, and tokens
# Please enter your own OAuth access token here and your ticket api link as well
class main:
    accessToken = 'Enter your OAuth access token'
    url = "Enter Your tickets api link"
    response = requests.get(url, {"Authorization": "Bearer " + accessToken})
    # check if the connection to the API was successful
    if response.status_code != 200:
        print("Unable to connect to API - Status code: " + str(response.status_code))
        exit()
    message_object = messages.Messages()
    newTicket = Ticket.Ticket(accessToken, url)
    ticketFormat = Format.Format()
    print(messages.Messages().welcome())


    def main(self):
        '''
        The main exception loop, continues to ask for commands and
        performs respective actions until 'quit' is entered
        '''
        command = input(messages.Messages().menu() + "\n" + "Enter A command: ")
        while command != "quit":
            if command == "all":
                self.newTicket = Ticket.Ticket(self.accessToken,self.url)
                print(self.ticketFormat.displayALlTIckets(self.newTicket.scroll()))
                print("PAGE NUMBER : " + str(self.newTicket.page))
            elif command == 'single':
                ticket_id = input("Enter Ticket ID: ")
                print(self.ticketFormat.displaySingleTicket(self.newTicket.getSingleTicket(ticket_id)))
            elif command == 'next':
                print(self.ticketFormat.displayALlTIckets(self.newTicket.scroll()))
                print("PAGE NUMBER : " + str(self.newTicket.page))
            elif command == 'menu':
                print(self.message_object.menu())
            else:
                print(self.message_object.invalidInput())
            command = input(self.message_object.command())

        print(self.message_object.goodBye())


if __name__ == "__main__":
    main.main(main)


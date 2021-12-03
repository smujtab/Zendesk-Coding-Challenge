# this module allows the organization of data into tables for the CLI output
from beautifultable import BeautifulTable
# this module allows the compiler ignore all future warnings since beauftifultable
# module raises FutureWarning that is irrelevant for this code
from warnings import simplefilter
# ignore any FutureWarning(s) raised
simplefilter(action='ignore', category=FutureWarning)

class Format:
    '''
    The purpose of the Format class is to provide tools that take in the ticket's data as lists or dictionaries
    and return them as organized tables for the command line output
    '''

    def getInfo(self,ticket_details):
        '''
        Extracts certain ticket details from a single ticket (in the form of a dictionary) and
        returns that as a list.

        :param ticket_details:
        :return: A list of the extracted ticket details
        '''
        return [ticket_details["id"], ticket_details["subject"], ticket_details["created_at"]]

    def displaySingleTicket(self,ticket_details):
        '''
        converts a single ticket (as a dictionary) in to a table or simply returns the
        parameter if a string is passed (meaning that an error likely occurred prior )

        :param ticket_details:
        :return: table of the single ticket or the message passed in
        '''

        if isinstance(ticket_details, str):
            return ticket_details
        else:
            table = BeautifulTable()
            table.column_headers = ["Ticket ID", "Subject", "Date"]
            table.append_row(self.getInfo(ticket_details))
            return table

    def displayALlTIckets(self, ticket_list):
        '''
        converts a list of tickets into a tabl or simply returns the parameter if a string is passed
        (meaning that an error likely occurred prior)
        :parameter: list of tickets
        :return: table of tickets or message
        '''
        if isinstance(ticket_list, str):
            return ticket_list
        else:
            table = BeautifulTable()
            table.column_headers = ["Ticket ID", "Subject", "Date"]
            for ticket in ticket_list:
                table.append_row(self.getInfo(ticket))
            return table



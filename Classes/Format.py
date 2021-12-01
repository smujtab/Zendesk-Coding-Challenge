from beautifultable import BeautifulTable
from warnings import simplefilter
# ignore all future warnings since beauftifultable module raises FutureWarning that is irrelevant for this code
simplefilter(action='ignore', category=FutureWarning)

class Format:

    def getInfo(self,ticket_details):
        return [ticket_details["id"], ticket_details["subject"], ticket_details["created_at"]]

    def displaySingleTicket(self,ticket_details):
        if isinstance(ticket_details, str):
            return ticket_details
        else:
            table = BeautifulTable()
            table.column_headers = ["Ticket ID", "Subject", "Date"]
            table.append_row(self.getInfo(ticket_details))
            return table

    def displayALlTIckets(self, ticket_list):
        if isinstance(ticket_list, str):
            return ticket_list
        else:
            table = BeautifulTable()
            table.column_headers = ["Ticket ID", "Subject", "Date"]
            for ticket in ticket_list:
                table.append_row(self.getInfo(ticket))
            return table



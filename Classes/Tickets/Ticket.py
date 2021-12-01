import requests


class Ticket:

    def __init__(self, access_token, subdomain_url):
        self.header = {"Authorization": "Bearer " + access_token}
        self.link = subdomain_url
        self.page = 0

    def getAllTickets(self):
        url = self.link + '.json?per_page=25'
        response = requests.get(url, headers=self.header)

        if response.status_code != 200:
            return 'Unable to connect with API' + ' Status:' + str(response.status_code)
        if self.page == 0:
            self.page = 1
        else:
            self.page = 0
        data = response.json()
        return data["tickets"]

    def Scroll(self):
        url = self.link + f'.json?page={self.page + 1}&per_page=25'
        response = requests.get(url, headers=self.header)
        if response.status_code != 200:
            return 'Unable to connect with API' + ' Status:' + str(response.status_code)
        else:
            data = response.json()
            if data["next_page"] is None:
                self.page = 0
            else:
                self.page += 1
            return data["tickets"]

    def getSingleTicket(self, ticket_id):

        url = self.link + f'/{ticket_id}.json'
        response = requests.get(url, headers=self.header)
        if self.checkTicketNumber(ticket_id) == True:
            return response.json()["ticket"]
        else:
            return self.checkTicketNumber(ticket_id)

    def checkTicketNumber(self, ticket_id):
        url = self.link + f'/{ticket_id}.json'
        response = requests.get(url, headers=self.header)
        data = response.json()
        if "error" not in data:
            return True
        else:
            if response.status_code == 400:
                return "Invalid type for ticket number, please enter an integer "
            if response.status_code == 404:
                return "Ticket ID not found, please try again"
            if response.status_code == 401:
                return "Unable to connect to API"

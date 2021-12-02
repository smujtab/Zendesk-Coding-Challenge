import requests

class Ticket:
    '''
    This class is the bulk of the "API" implementation component in this application
    This class will provide functions that connect to the zendesk API and perform
    the specified actions using an OAuth access token and a Zendesk Tickets API link
    '''
    def __init__(self, access_token, api_link):
        # OAuth access token format
        self.header = {"Authorization": "Bearer " + access_token}
        # api link that is used through out the class
        self.link = api_link
        # this is a separate api link that will be updated as the scroll function is used
        self.nextPage = self.link +'.json?page[size]=25'
        self.page = 0

    def getAllTickets(self):
        '''
        Fetches 25 tickets from using the the zendesk tickets api
        :return: a list of tickets or a message containing the API status
        '''
        url = self.link + '.json?per_page=25'
        response = requests.get(url, headers=self.header)
        # ensures api connection to prevent raising an error later
        if response.status_code != 200:
            return 'Unable to connect with API' + ' Status:' + str(response.status_code)
        if self.page == 0:
            self.page = 1
        else:
            self.page = 0
        data = response.json()
        return data["tickets"]

    def Scroll(self):
        '''
        Scroll through the list of tickets 25 at a time and returns back to the first page if their are
        no more tickets left to go through
        This function also updates the ticket attribute of the class which is returned in CLI to indicate the
        current page number.
        :return: 25 tickets in accordance to the tickets
        '''
        response = requests.get(self.nextPage, headers= self.header)
        data = response.json()
        if data['meta']['has_more']:
            result = data['tickets']
            self.page +=1
            self.nextPage = data['links']['next']
        else:
            self.page = 0
            self.nextPage = self.link + '.json?page[size]=25'
            result = requests.get(self.nextPage, headers=self.header).json()["tickets"]
        return result


    def getSingleTicket(self, ticket_id):
        '''
        Takes in the ticket ID and then returns the details of the single ticket in the format of a dictionary
        If the ticket information is invalid, the functions returns the result from the checkTicketNumber function
        :param ticket_id:
        :return: dictionary of ticket details
        '''
        url = self.link + f'/{ticket_id}.json'
        response = requests.get(url, headers=self.header)
        # checks the validity of the parameter first
        if self.checkTicketNumber(ticket_id) == True:
            return response.json()["ticket"]
        else:
            return self.checkTicketNumber(ticket_id)

    def checkTicketNumber(self, ticket_id):
        '''
        Checks the passed in parameter for ticket validity, and returns message accordingly
        :param ticket_id:
        :return:
        '''
        url = self.link + f'/{ticket_id}.json'
        response = requests.get(url, headers=self.header)
        data = response.json()
        if "error" not in data:
            # ticket is valid and thus returns true
            return True
        else:
            # ticket is invalid and thus returns the status code paired with a respective message
            if response.status_code == 400:
                return "TIcket ID must be an integer"
            if response.status_code == 404:
                return "Ticket ID not found, please try again"
            if response.status_code == 401:
                return "Unable to connect to API"


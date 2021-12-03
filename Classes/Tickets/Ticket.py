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
        # checks if the link entered is valid
        try:
            requests.get(self.link+'.json?page[size]=25', headers=self.header)
        except:
            print("Unable to connect to your API link - Please check your URL!")
            exit()

    def scroll(self):
        '''
        Scroll through the list of tickets 25 at a time and returns back to the first page if their are
        no more tickets left to go through
        This function also updates the page attribute of the class which is returned in the CLI to indicate the
        current page number.
        :return: 25 tickets in accordance to the tickets
        '''
        response = requests.get(self.nextPage, headers= self.header)
        if response.status_code != 200:
            return "Unable to connect to API - Status code: " + str(response.status_code)

        data = response.json()
        # set the url to the next page if it is available and set the return variable to the current page

        if data['meta']['has_more']:
            result = data['tickets']
            # increment the page count
            self.page +=1
            self.nextPage = data['links']['next']
        # if no next page is available set the return variable to the first page
        else:
            # reset the page count
            self.page = 1
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
        data = response.json()
        # checks the validity of the parameter first
        if "error" not in data:
            # ticket is valid and thus returns true
            return data["ticket"]
        else:
            # ticket is invalid and thus returns the status code paired with a respective message
            if response.status_code == 400:
                return "TIcket ID must be an integer"
            if response.status_code == 404:
                return "Ticket ID not found, please try again"
            if response.status_code == 401:
                return "Unable to connect to API"
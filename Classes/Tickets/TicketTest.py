import unittest

import requests
import Ticket


class MyTestCase(unittest.TestCase):
    token = "enter your url"
    url = "enter your url"

    #should return a list if the all credentials were valid
    def test_scroll_correct_credentials(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        self.assertTrue(isinstance(test_ticket.scroll(),list))

    # should return a string in message if an invalid token passed in
    def test_scroll_wrong_credentials(self):
        token = "wrong token"
        test_ticket = Ticket.Ticket(token, self.url)
        self.assertTrue(isinstance(test_ticket.scroll(),str))

    # should increment the page attribute correctly depending on the amount of function calls
    def test_scroll_increment_page_number(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        test_ticket.scroll()
        test_ticket.scroll()
        self.assertEqual(test_ticket.page, 2)

    # should reset the page attribute when the last page has been reached
    def testScroll_update_page_number(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        test_ticket.scroll()
        while test_ticket.nextPage != self.url + '.json?page[size]=25':
            test_ticket.scroll()
        self.assertEqual(test_ticket.page, 1)

    # should return a dictionary if the ticket ID was valid
    def test_getSingleTicket_Valid_Ticket_Entry(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        self.assertTrue(isinstance(test_ticket.getSingleTicket(34), dict))

    # should return a string in message if an invalid ID passed in
    def test_getSingleTicket_ID_Not_Found(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        wrong_ID = 908098
        self.assertTrue(isinstance(test_ticket.getSingleTicket(wrong_ID), str))

    # should return a string in message if a non-Integer passed in
    def test_getSingleTicket_Invalid_I(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        Invalid_ID = "fdasdfas"
        self.assertTrue(isinstance(test_ticket.getSingleTicket(Invalid_ID), str))

    # should return a string in message if an invalid token passed in
    def test_getSingleTicket_API_connection(self):
        token = "wrong token"
        test_ticket = Ticket.Ticket(token, self.url)
        self.assertTrue(isinstance(test_ticket.getSingleTicket(20), str))

if __name__ == '__main__':
    unittest.main()

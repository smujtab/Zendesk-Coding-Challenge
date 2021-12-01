import unittest

import requests

import Ticket


class MyTestCase(unittest.TestCase):
    token = "Enter your OAuth Access Token"
    url = " Enter your Zendesk TICKETS API link"
    def test_getAllTickets_correct_credentials(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        self.assertTrue(isinstance(test_ticket.getAllTickets(),list))

    def test_getAllTickets_wrong_credentials(self):
        token = "wrong token"
        test_ticket = Ticket.Ticket(token, self.url)
        self.assertTrue(isinstance(test_ticket.getAllTickets(),str))

    def testScroll_increment_page_number(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        test_ticket.getAllTickets()
        test_ticket.Scroll()
        self.assertEqual(test_ticket.page, 2)

    def testScroll_update_page_number(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        test_ticket.page = 5
        test_ticket.Scroll()
        self.assertEqual(test_ticket.page, 0)

    def test_getSingleTicket_Valid_Ticket_Entry(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        self.assertTrue(isinstance(test_ticket.getSingleTicket(34), dict))

    def test_getSingleTicket_ID_Not_Found(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        wrong_ID = 908098
        self.assertTrue(isinstance(test_ticket.getSingleTicket(wrong_ID), str))

    def test_getSingleTicket_Invalid_I(self):
        test_ticket = Ticket.Ticket(self.token,self.url)
        Invalid_ID = "fdasdfas"
        self.assertTrue(isinstance(test_ticket.getSingleTicket(Invalid_ID), str))

    def test_getSingleTicket_API_connection(self):
        token = "wrong token"
        test_ticket = Ticket.Ticket(token, self.url)
        self.assertTrue(isinstance(test_ticket.getSingleTicket(20), str))

if __name__ == '__main__':
    unittest.main()

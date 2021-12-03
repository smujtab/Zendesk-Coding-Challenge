# Zendesk Ticket Viewer - Intern Challenge 2021

A python application that displays ticket details from a zendesk account in the command line interface.
The application interacts with the Zendesk ticket API to make real time requests and then format
that data for the Command Line. 

### What you will need:

- Latest version of python (3.01 and above) 
  - Link here: https://www.python.org/downloads/

### How to run the program 

Since the program is command line based, there may be differences in setting up and navigating to the 
project between Mac/OS and Windows. However, it should be fairly simple on either platform.

1. Open up your terminal and enter the following command:<br>
   ``git clone https://github.com/smujtab/Zendesk-Coding-Challenge.git``
2. Download pip if NOT already installed using:
   1. ``curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py``
   2. Followed by : ``python3 get-pip.py``
3. Download the required modules:
   1. ``pip install BeautifulTable``
   2. ``pip install requests``
4. Next you will have to change your credentials in the code by opening up ``main.py`` and enter your credentials into <br>``accessToken = "Enter your OAuth access token"`` and<br> 
``url = "Enter Your tickets api link"``
   1. **The URL must be your zendesk api link for tickets, ie: ``https://{subdomain}.zendesk.com/api/v2/tickets``**
   5. See the following page to learn how to get an OAuth access token: ``https://developer.zendesk.com/documentation/ticketing/working-with-oauth/creating-and-using-oauth-tokens-with-the-api/``
5. Return to the terminal and navigate to the project directory, then run the application with the following code:
   1. `` python3 main.py``

## Crossroads in design

### Aspect # 1: Object Oriented design 

When I originally started the project, I decided write the entire code base as a single script file 
that contained all the functions/methods to run the application. However, as I began to 
test and tweak the code, it became glaringly apparent to me that the lack of modularity 
would make any attempts at changing or improving the code painstakingly difficult. Realizing this,
I decided to divide up the script file into smaller chunks as classes and functions. This allowed 
code to be much cleaner and easier to understand. 

#### The program has 4 classes:

1. ``main.py`` - the main script of the program, calls all the different classes and functions
2. ``Ticket.py`` - This class contains the bulk of the API implementation required for the program, 
ie getting and returning tickets
3. ``Format.py`` - takes ticket data and converts it into beautiful tables 
(literally, the module used is called BeautifulTable) for the cli.
4. `messages.py` - contains messages that can be prompted when needed


### Aspect # 2: Off-set vs Cursor based pagination

Initially the program implemented offset pagination as it seemed relatively more intuitive and easier
than the Cursor based version. However, after reading deeper into the Zendesk API documentation it seemed that off-set
pagination some limitations with bigger data sets which would hinder the scalability of the program and so 
i decide to re-implement the pagination as cursor-based.
<br> <br> 
Surprisingly, it turns out that implementing Cursor-based Pagination actually led to number of improvements 
in the code:
1. It made tracking the page number much easier as the code no longer had to create a different
function to reset the page count, instead it just manually incremented depending on if there was a next
page existed or not
2. It made getting the next page easier as well as the class attribute ``nextPage``could
just be updated to the current response's ``next`` url link. 
3. It allowed for easier implementation of continuous scrolling past the last page to the front page
through checking the `has_more` value of the ticket response. If false, then the ``nextPage`` attribute
would just be reset to the first page URL

### Aspect # 3: OAuth vs Basic Authentication

This is the last design choice that I decided to implement into the program. After
reading up on the different authentication choices, it was evident that hard-coding the 
user's password and username would not be optimal for security. The implemented OAuth token
system allows for:
1. A more secure program as the password and username are no longer coded into the program
2. Limiting the program to only reading ticket data


### Conclusion

Working on this project has been a fun and learning challenge. It has taught me important technical
skills such as design choices, API and OAuth implementation, and even CURL. Above all
I have learnt the true importance of thoroughly reading an applications' documentation
before deciding the ways to implement it. Zendesk's API documentation was immensely helpful 
resource throughout the project. 








   




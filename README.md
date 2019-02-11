[![Build Status](https://travis-ci.org/NehemiahLimo/politicoapp-api.svg?branch=develop)](https://travis-ci.org/NehemiahLimo/politicoapp-api)  [![Coverage Status](https://coveralls.io/repos/github/NehemiahLimo/politicoapp-api/badge.svg?branch=master)](https://coveralls.io/github/NehemiahLimo/politicoapp-api?branch=master)  [![Maintainability](https://api.codeclimate.com/v1/badges/785bc4a128a9c91f7e79/maintainability)](https://codeclimate.com/github/NehemiahLimo/politicoapp-api/maintainability)

# Politico API Endpoints Summary
Polticoapp-api is a backend development for the Politico voting system, the backend provides the privilege to interact with the voting system, by allowing the creation of a party, office, political office and other fucntionalities as described in our description sector. On the other hand, it provides the admin the privilege of updating or deleting a political party or an office. Othe features provided in this API include fetching all parties by name and also offices by name.
Hosting of this API endpoint app is at Heroku


## Description
The following Enpoints are going to be tested.

| Endpoint                                   | Functionality                      |
| ----------------------------------------   |:----------------------------------:|
| POST  /api/v1/party                       | Creates a political party             |
| GET  /api/v1/parties                        | Get all political parties          |
| GET  /api/v1/party/<int:party_id>          | Get a specific political party by id           |
| DELETE  /api/v1/party                      | DELETE ONE political party         |
| PUT  /api/v1/party/<int:party_id>          | Update one political party        |
| POST  /api/v1/office                       | Creates a government office           |
| GET  /api/v1/office/<int:office_id>        | Get one government office          |
| GET  /api/v1/office                        | Get all government offices          |

## Pre-requisites
  1. python3
  2. [Postman](https://www.getpostman.com/)
  3. [Git](https://git-scm.com/)
  4. [Vscode](https://code.visualstudio.com/download)


### Installations
    1. In order to get started open your terminal and git clone this repo `git clone https://github.com/NehemiahLimo/politicoapp-api.git`
    2. cd into the project folder and create a virtual environment using the following command `virtualenv -p python3 venv`
    3. to activate your virtual environment, use `source venv/bin/activate`
    4. Install the requirements by doing `pip install -r requirements.txt`
    5. to run the application, use the command `python3 run.py`


# Running Tests
    - Run your tests by executing the `pytest` command in your terminal.
    
    
# Building environment
    1. Flask Microframework.
    2. Pip
    
    
# Acknowledgements
  - Andela Workshop
  - Team 11
  - Workshop Facilitator
  
  
# Author
  [Nehemiah Cheburet](https://github.com/NehemiahLimo)

# License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)





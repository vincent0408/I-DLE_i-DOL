
# I-DLE_I-DOL

A KKTIX ticket bot written in Python originally designed to purchase tickets for (G)I-DLE's I-DOL concert. However, by changing the event ID, its usage can be extended for other events as well.

Utilizing  Selenium to automate the ticket purchasing process and the convenience of Jupyter Notebooks, users are able to maintain the control of Chromedriver while modifying parts of the code. 

Purchasing tickets for popular events on KKTIX only requires the user to fill in the quantity of tickets, agree to the user terms and press the find tickets button, so speed and a little bit of luck is all that is required for a successful purchase. This bot not only handles the normal senarios, but also takes care of the extreme senarios that only occur on popular events, which are impossible to program and prevent if one has not experience against said senarios.

## Features

- Auto refresh until ticket available
- Select ticket by seat price or name
- Priority of seat prices and names
- Auto seek for remaining tickets
- Allowing different quantities of tickets for different prices
- Login with cookies to save time
- Allows manual and automatic seat selecting if the event provides choices

## reCAPTCHA Bypass with CapSolver

For websites that require reCAPTCHA verification, the [CapSolver](https://www.capsolver.com/) extension can be automatically installed and activated on Chromedriver startup. Download the extension from the [Official Github](https://github.com/capsolver/capsolver-browser-extension/releases) and unzip the files into a CapSolver folder and place it under the ticket bot directory. The `assets/config.json` file should be modified to login to user's CapSolver account. 

## Instructions

1. Clone this repository and unzip it somewhere
2. Install Python 3 and the required packages in crawler.ipynb
3. Modify `cred_example.txt` to your own email and password of KKTIX and rename it to `cred.txt`
4. (Optional) Unzip CapSolver extension into `/CapSolver/` and modify `assets/config.json`
5. (Optional) run `refresh_cookies` to generate cookies
6. Modify configuration to your desired event and seat price/name 
7. Run `crawler.ipynb`
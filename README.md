
# A Python based Automation program to make powerpoint presentation of songs

![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white) ![PyAutoGUI](https://img.shields.io/badge/Pyautogui-FFD43B?style=for-the-badge&logo=python&logoColor=blue) 

## Overview
This python project was built for my church to make powerpoint presentations of song lyrics in tamil & english.


## Details of Implementation 
The process of this automation can be broken down into two parts:

> ### Scraping data
- The required lyrics are scraped from a website named [Tamil Christian Songs](https://tamilchristiansongs.in/tamil/) using [Selenium](https://www.selenium.dev/documentation/). I will be migrating to some other website soon as the data in this website is unkempt and raises a lot of edge cases.  
The [data_scraping.py](/data_scraping.py) is the python file which has the class with the method to do the same.

> ### Making the powerpoint presentation
- This part of the process is implemented using the [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/).  
Note that this part of the process is highly subjective to each system and might not work without customization.


####  I will be working on building a more system-independent code in the future.

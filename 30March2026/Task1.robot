#Task1

#Navigate to Website
#scroll to popup window
#click on it
# switch to the window and return the title
#switch back to the parent window and assert the heading of the page

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling windows
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Sleep   3s
     Click Element   xpath= //button[@id="PopUp"]
     Sleep   2s

     @{windows}  Get Window Handles
     @{titles}  Get Window Titles
     Log To Console   ${titles}
     Switch Window  New
     Sleep  5s

     Switch Window  ${windows}[0]
     Log To Console   ${titles}[0]
     Page Should Contain   Automation Testing Practice
     Sleep   3s

     Close Browser
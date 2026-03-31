#implicit = global wait , found in dome structure , if it found it work
# set selenium implicit wait
#set browser implicit wait
# explicit = driver , wait for the time period if the condition is true



*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console   ${before}

    Set Selenium Implicit Wait   5s  # after this line we perform all the action

    ${after}  Get Selenium Implicit Wait
    Log To Console   ${after}

#    Get Selenium Implicit Wait :-  Returns you the time of implicit wait
#     Set Selenium Implicit Wait:-  This keywords lets you set implicit wait , usually in seconds recommantion Set B
#      Set Browser Implicit Wait:- This keyword let you set implicit wait for one browser instance , if there are multiple browsers then itll be confined that browser

    Close Browser

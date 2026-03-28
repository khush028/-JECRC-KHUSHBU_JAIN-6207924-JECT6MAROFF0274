*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
# to store in folder = Set Screenshot Directory  ${CURDIR}/../Screenshots
    Set Screenshot Directory  ${CURDIR}/../Screenshots
    Open Browser  ${url}  chrome
    Minimize Browser Window
    Sleep   3s
    
    Capture Page Screenshot  fullpage.png
    Sleep   3s
    
    Capture Element Screenshot   xpath=//img[@alt="Dhurandhar The Revenge"]  dhurandhar.png
    sleep  3s

    Close Browser
    
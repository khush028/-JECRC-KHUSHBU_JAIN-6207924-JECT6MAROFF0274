*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling single iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s

    Select Frame  id=singleframe

    Input Text   xpath=//input[@type="text"]    khush
    Sleep   3s
    Unselect Frame

    Close Browser
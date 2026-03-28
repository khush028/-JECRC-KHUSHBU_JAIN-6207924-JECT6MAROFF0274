*** Settings ***
Documentation  week checkboxes
Library  SeleniumLibrary
Library    XML

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkbox
    [Documentation]  week checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  1s


    Click Element    xpath=(//label[@for="days"])
    Page Should Contain Checkbox    xpath=//input[@id = "sunday"]

    Select Checkbox    xpath=//input[@id = "sunday"]
    Select Checkbox    xpath=//input[@id = "wednesday"]
    Sleep    2s
    Unselect Checkbox    xpath=//input[@id = "sunday"]
    Sleep    2s

    # gender
    Click Element    xpath=(//input[@id="female"])
    Sleep    3s

    Close Browser
*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling Checkbox
    [Documentation]  herokuapp checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  1s

    Click Element    xpath=//a[text()="Checkboxes"]

    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]

    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    2s

    Close Browser
*** Settings ***
Library  SeleniumLibrary
*** Variables ***
*** Test Cases ***
Open youtube in edge
     Open Edge Browser

*** Keywords ***
Open Edge Browser
    [Documentation]  Edge Browser navigation to https://www.youtube.com/
    Open Browser  https://www.youtube.com/  edge
    Maximize Browser Window

    Log  navigated to youtube
    Log To Console    navigated to youtube
    Sleep    3s

    Close Browser


*** Settings ***
Documentation  opening of browsers
Library  SeleniumLibrary

*** Test Cases ***
Opening Edge Browser
    [Documentation]  Edge Browser navigation to https://www.youtube.com/
    Open Browser  https://www.youtube.com/  edge
    Maximize Browser Window

    Log  navigated to youtube
    Log To Console    navigated to youtube
    Sleep    3s

    Close Browser


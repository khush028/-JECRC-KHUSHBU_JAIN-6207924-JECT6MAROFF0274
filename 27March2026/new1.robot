*** Settings ***
Documentation  opening of browsers
Library  SeleniumLibrary

*** Test Cases ***
Opening Chrome Browser
    [Documentation]  Chrome Browser navigation to https://www.youtube.com/
    Open Browser  https://www.youtube.com/  chrome
    Maximize Browser Window

    Log  navigated to youtube
    Log To Console    navigated to youtube
    Sleep    3s

    Close Browser


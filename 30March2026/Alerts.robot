*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alerts
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   3s
    
    Click Button   xpath=//button[@onclick="jsAlert()"]
    Sleep   5s
    Handle Alert
    Sleep   5s

    Close Browser


Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   3s

    Click Button   xpath=//button[@onclick="jsConfirm()"]
    Sleep   5s
    Handle Alert  action=DISMISS
    Sleep   5s

    Close Browser


Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep   3s

    Click Button   xpath=//button[@onclick="jsPrompt()"]
    Sleep   5s
    Input Text Into Alert   khush  action=DISMISS
    Sleep   5s

    Close Browser

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling single iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  3s

#    Scroll Element Into View   xpath=//a[text()="Iframe with in an Iframe"]
    Click Element   xpath=//a[@href="#Multiple"]
    Select Frame  xpath=//iframe[@src="MultipleFrames.html"]
    Select Frame  xpath=//iframe[@src="SingleFrame.html"]
    Input Text   xpath=//input[@type="text"]  KhushbuJain


    Sleep   3s


    Close Browser
*** Settings ***
Library  SeleniumLibrary
Library    XML

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling drag and drop
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Sleep    2s
     
     Click Element   xpath=//a[text()="Drag and Drop"]
     Sleep    2s
     
     Drag And Drop    id=column-a    id=column-b
     Sleep    2s

     Close Browser
     
Handling Mouse hover 
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Sleep    2s
     
     Click Element   xpath=//a[text()="Hovers"]
     Sleep    2s
     Mouse Over   xpath=//h5[text()="name: user2"]/ancestor::div[@class="figure"]
     Sleep    2s
     Close Browser


Handling Scroll to element
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Sleep    2s

     Scroll Element Into View   xpath=//a[text()='Typos']
     Sleep    10s
     Close Browser

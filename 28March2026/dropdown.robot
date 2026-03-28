*** Settings ***
Documentation  handling dropdown
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
handle dropdown 
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Click Element   xpath=//a[text()="Dropdown"]
     
     Page Should Contain List  id=dropdown

     ${options}=  Get List Items   id=dropdown
     Log To Console   ${options}

     # Multi select
     Select From List By Label  id=dropdown  Option 1

     ${select_options}=  Get Selected List Label  id=dropdown
     # log only take singe value argument = [[grren , blue]] = "[green,blue]"
     Log To Console   ${select_options}

     Sleep   3s

     Close Browser
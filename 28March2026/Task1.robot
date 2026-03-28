*** Settings ***
Documentation  handling dropdown
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handle dropdown
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Scroll Element Into View   xpath=//select[@id="colors"]

     Page Should Contain List  id=colors

     ${options}=  Get List Items   id=colors
     Log To Console   ${options}

     # Multi select
     Select From List By Index  id=colors  1
     Select From List By Index  id=colors  3


     @{select_options}=  Get Selected List Labels  id=colors
     Log To Console   ${select_options}

     Sleep   3s

     Close Browser
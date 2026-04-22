*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/login_page_locator.robot

*** Keywords ***
Log In The Application
    [Documentation]  this logins in the login page
    [Arguments]  ${email}  ${pwd}

    Click Element    ${account_link}
    Log    Clicking on the account link

    Input Text    ${email_label}    ${email}
    Log    Entering email

    Input Text    ${password_label}    ${pwd}
    Log    Entering password

    Click Element    ${sign_in_btn}
    Log    SIGNUP button
    Sleep    10s
    
    Page Should Contain Element    xpath=//a[@href="/account/logout"]
    Page Should Contain    Account

    Sleep    3s

    Close Browser

    


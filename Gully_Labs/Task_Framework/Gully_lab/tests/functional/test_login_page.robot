*** Settings ***
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/home_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC02 Login User
    [Documentation]  check if the user is able to login
    [Tags]  functional

    Log In The Application    ${USER_EMAIL}    ${USER_PWD}






















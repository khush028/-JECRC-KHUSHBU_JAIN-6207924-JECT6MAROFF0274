*** Settings ***
Resource  ../../resources/pages/home_page.robot
Resource  ../../resources/common_resources.robot

Test Setup  Open Application    https://gullylabs.com/
Test Teardown  Close Application

*** Test Cases ***
TC01 Navigate Accounts
    [Documentation]  this navigates to the home page

    Click Element    ${account_link}
    Log    Clicking on the account link

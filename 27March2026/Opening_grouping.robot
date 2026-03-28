*** Settings ***
Documentation  opening of browsers
Library  SeleniumLibrary


*** Test Cases ***
Opening Chrome headless Browser
    [Documentation]  Chrome headless Browser navigation to https://www.youtube.com/
# tag :- grouping testing
    [Tags]  smoke
# opening cmd = robot -d grouping_reports -i "smoke" Opening_grouping.robot

# we can't see the ui in it
    Open Browser  https://www.youtube.com/  headlesschrome
    Maximize Browser Window

    Log  navigated to youtube
    Log To Console    navigated to youtube
    Sleep    3s

    Close Browser

#robot -d reports -t "Opening Chrome Headless Browser" Open_headless.robot


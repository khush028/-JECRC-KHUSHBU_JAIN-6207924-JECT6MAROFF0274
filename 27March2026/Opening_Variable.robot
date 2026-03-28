*** Setting ***

#-- imports ,resources
#*** 2variables -- all variables ***

#*** 4keywords -- user defined keyword ***

Documentation  Opening of browser
Library  SeleniumLibrary

*** Variables ***
#scaler variable -- single and ($)
${url}  https://www.cricbuzz.com/


#list -- stores lost of elements
@{bikes}  Ktm  Kawasaki  honda pulsar  bullet


#dict vaiables
&{Cars}  nissan=gtr  honda=civic  bmw=m5


*** Test Cases ***
#test cases -- all your testscript
Opening Chrome headless Browser
    [Documentation]  chrome headless browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke  reg
#    Open Browser  https://www.cricbuzz.com/  headlesschrome
     Open Browser  ${url}  headlesschrome
    Maximize Browser Window


    Log    navigated to cricbuzz
#    Log To Console    navigated to cricbuzz
    Log To Console  ${bikes}[1]
   #   work same as print
    Log To Console  ${Cars.nissan}
    Sleep    3s
    Close Browser
*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem   # we use it for uploading and downloading

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${Check_Download}  C:\\Users\\hp\\Downloads\\abc.txt

*** Test Cases ***
File Upload
     Open Browser  ${url}  chrome
     Maximize Browser Window
     Sleep   3s

     Click Element   xpath=//a[@href="/upload"]
     Sleep   2s

     ${path}  Normalize Path    ${CURDIR}/sample.text
     Choose File   id=file-upload  ${path}
     Sleep   2s

     Click Button   id=file-submit
     Sleep   2s

     Close Browser


File Download
   Open Browser  ${url}  chrome
   Maximize Browser Window
   Sleep   3s
   
   Click Element   xpath=//a[@href="/download"]
   Sleep  3s
   
   Click Element   xpath=//a[@href="download/abc.txt"]
   Sleep   3s
   
   Wait Until Created   ${Check_Download}  timeout=10s
   File Should Exist    ${Check_Download}
   Log To Console   File Downloaded

   Close Browser



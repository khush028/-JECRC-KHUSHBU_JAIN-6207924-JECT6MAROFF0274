*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           JSONLibrary

*** Variables ***
${BASE_URL}       https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    [Documentation]    Add a new pet to the store
    Create Session    petapi    ${BASE_URL}   verify=True
    ${payload}=    Load JSON From File    ${CURDIR}/../data/add_pet.json
    Set Suite Variable    ${PET_ID}    ${payload}[id]
    ${response}=    POST On Session    petapi    /pet    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Update existing pet
    [Documentation]    Update an existing pet
    Create Session    petapi    ${BASE_URL}   verify=True
    ${payload}=    Load JSON From File    ${CURDIR}/../data/update_pet.json
    ${response}=    PUT On Session    petapi    /pet    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Upload an Image
    Create Session    petapi    ${BASE_URL}   verify=True
    ${form_data}=    Create Dictionary   additionalMetadata=Burno's img
    ${file_path}=    Set Variable     ${CURDIR}/../data/Burno's img.jpg
    ${file}=  Evaluate    {'file': open($file_path, 'rb')}
    ${response}=    POST On Session    petapi    /pet/${PET_ID}/uploadImage    data=${form_data}    files=${file}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Find pet by ID
    [Documentation]    Find pet by ID
    Create Session    petapi    ${BASE_URL}   verify=True
    ${response}=    GET On Session    petapi    /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Find pet by status
    [Documentation]    Find pet by status
    Create Session    petapi    ${BASE_URL}   verify=True
    ${qp}=   Create Dictionary   status=available
    ${response}=    GET On Session    petapi    /pet/findByStatus    params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Update pet with form data
    [Documentation]    Update pet with form data
    Create Session    petapi    ${BASE_URL}   verify=True
    ${form_data}=    Create Dictionary   name=Tillu   status=sold
    ${response}=    POST On Session    petapi    /pet/${PET_ID}    data=${form_data}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Delete pet
    [Documentation]    Delete pet by ID
    Create Session    petapi    ${BASE_URL}   verify=True
    ${response}=    DELETE On Session    petapi    /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200


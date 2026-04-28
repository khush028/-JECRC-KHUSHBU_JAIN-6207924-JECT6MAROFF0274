#pip install robotframework-requests
#pip install robotframework-jsonlibrary
#pip install jsonschema

*** Settings ***
Library   RequestsLibrary
Library   Collections
Library    String

*** Variables ***
${Base_URL}   https://petstore.swagger.io/v2

*** Test Cases ***
Pet inventories
    [Documentation]  get pet inventories by status
    Create Session    petapi    ${Base_URL}  verify=True    #to run all test cases in session by alias

    ${response}=  GET On Session    petapi    /store/inventory

    Should Be Equal As Integers    ${response.status_code}    200    #equal to int
    ${body}=  Set Variable  ${response.json()}  #scalar variable

    Log To Console   ${body}
    Log To Console   ${response.status_code}

Place Order
    [Documentation]  place an order for a pet
    Create Session    petapi    ${Base_URL}  verify=True    #to run all test cases in session by alias

    ${playload}=  Create Dictionary
    ...     id=12345
    ...     petId=54321
    ...     quantuty=1
    ...     shipDate=2026-04-28T06:56:01.3962
    ...     status=placed
    ...     complete=true

    ${response}=  POST On Session  petapi   /store/order  json=${playload}
    Should Be Equal As Integers   ${response.status_code}    200
    ${body}=  Set Variable  ${response.json()}

    Should Be Equal As Integers   ${body}[id]    12345

    Should Be Equal As Strings     ${body}[status]    placed

    Log To Console   ${body}
    Log To Console   ${response.status_code}

    Set Suite Variable   ${ORDER_ID}  ${body}[id]   # it create variable for that file robot
                                                    # global for all robot it can overlap
     
Get Order By ID
    [Documentation]  Find order by id
    Create Session    petapi    ${Base_URL}  verify=True    #to run all test cases in session by alias

    ${response}=  GET On Session    petapi    /store/order/${ORDER_ID}
    
    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}


Delete purchase by order id
    [Documentation]  del order by Id
    Create Session    petapi    ${Base_URL}  verify=True    #to run all test cases in session by alias

    ${response}=  DELETE On Session    petapi    /store/order/${Order_ID}

    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

E2E
    Create Session    e2eapi   ${BASE_URL}   verify=True
    ${payload}=    Create Dictionary
    ...    id=12345
    ...    petId=54321
    ...    quantity=1
    ...    shipDate=2026-04-28T07:00:48.883Z
    ...    status=placed
    ...    complete=true
    ${response1}=    POST On Session    e2eapi    /store/order    json=${payload}
    Should Be Equal As Integers    ${response1.status_code}    200
    ${body}=  Set Variable     ${response1.json()}
    Set Suite Variable    ${ORDER_ID}    ${body}[id]
    Log To Console    Created an order by id
    ${response2}=    GET On Session    e2eapi    /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response2.status_code}    200
    Log To Console    Got the order by id
    ${response3}=    DELETE On Session    e2eapi    /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response3.status_code}    200
    Log To Console    Deleted the order by id
    Log To Console    e2e completed

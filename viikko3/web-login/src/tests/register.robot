*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Login Page

*** Test Cases ***

Register With Valid Username And Password
    Go To Register Page
    Set Username  asd
    Set Password  asd123xd
    Set Confirm Password    asd123xd
    Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  as
    Set Password  asd123xd
    Set Confirm Password    asd123xd
    Register
    Register Should Fail With Message    Username must be at least 3 characters
    
Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  asd
    Set Password  asd
    Set Confirm Password    asd
    Register
    Register Should Fail With Message    Password must be at least 3 characters and contain non alphabetical characters

Register With Valid Username And Invalid Password
    Go To Register Page
    Set Username  asd
    Set Password  asd
    Set Confirm Password    asd
    Register
    Register Should Fail With Message    Password must be at least 3 characters and contain non alphabetical characters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  asd
    Set Password  testing1
    Set Confirm Password    testing2
    Register
    Register Should Fail With Message    Password and Password confirmation must match

Register With Username That Is Already In Use
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Confirm Password    kalle123
    Register
    Register Should Fail With Message    Username already taken

Login After Successful Registration
    Go To Main Page
    Click Button    Logout
    Login Page Should Be Open
    Set Username    kalle
    Set Password    kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Register Page
    Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

*** Keywords ***
Register Should Succeed
    Welcome to Ohtu Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register
    Click Button  Register


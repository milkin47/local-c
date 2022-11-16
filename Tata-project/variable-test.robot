*** Settings ***
Documentation  Testing Variable

*** Test Cases ***
TC1: Variable Testing
    Addition    ${a}   ${b}
    log  ${a}

*** Keywords ***
Addition
    [Arguments]     ${a}   ${b}
    should be equal as strings  ${a}    ${b}
    log to console  ${a}
    log to console  hai
    #[Arguments]    ${a}  ${b}
    #log  ${a}   ${b}

*** Settings ***
Library         TestProjectLibrary
Suite Setup     Init Session
Suite Teardown  Close Session

*** Test Cases ***
Set Session
    ${previous kw}=     Register Keyword To Run On Failure      None
Login With Incorrect Password
    Base Login          ${INCORRECT_PASSWORD}
Login With Correct Password
    Base Login          ${CORRECT_PASSWORD}
Fill Form
    Select From List By Label   css:#country    Australia
    FOR     ${input}    IN      @{INPUT_ELEMENTS}
        Input Text      ${input}    ${INPUT_VALUES}[${INDEX}]
        ${INDEX}=       Evaluate    ${INDEX} + 1
    END
    Static Sleep
Submit Form
    Click Button    css:#save
    Click Button    css:#logout

*** Keywords ***
Init Session
    #${options}=                 Headless Chrome
    Init Testproject Driver     chrome      job_name=TestProject Robot  url=https://example.testproject.io/web/
    #desired_capabilities=${options}   disable_reports=False

Close Session
    Close All Browsers

Equals
    [Arguments]                     ${x}    ${y}
    Should Be Equal As Strings      ${x}    ${y}

Clear Fields
    Clear Element Text     css:#name
    Clear Element Text     css:#password

Headless Chrome
    ${chrome_options} =     Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    headless
    Call Method    ${chrome_options}    add_argument    disable-gpu
    [Return]       ${chrome_options}

Base Login
    [Arguments]               ${input_password}
    Press Keys                css:#name                       ${EMAIL}
    Input Text                css:#password                   ${input_password}
    ${password}=              Get Value                       css:#password
    ${result}=                Run Keyword And Return Status   Equals    ${password}    ${CORRECT_PASSWORD}
    Run Keyword If            "${result}" == "True"           Run Keywords True
    ...     ELSE              Clear Fields

Run Keywords True
    Click Button      css:#login
    Sleep             3s

Static Sleep
    Sleep             3s


*** Variables ***
${EMAIL}                test@testproject.io
${INCORRECT_PASSWORD}   67890
${CORRECT_PASSWORD}     12345
${INDEX}                0
${CAPABILITIES}         ${EMPTY.join(${_tmp})}
@{INPUT_ELEMENTS}       css:#address    css:#email    css:#phone
@{INPUT_VALUES}         Melbourne       test@test.io  7521234545
@{_tmp}                 browserName: chrome,
...                     version: 91,
...                     name: RobotFramework Test

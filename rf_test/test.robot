*** Settings ***
Library    SeleniumLibrary
Library    RobotEyes

*** Test Cases ***
Sample visual regression test case  # Name of the example test case
    Open Browser    https://www.google.com/    chrome
    Maximize Browser Window
    Open Eyes    SeleniumLibrary(AppiumLibrary)  5
    Wait Until Element Is Visible    id=lst-ib
    Capture Full Screen
    Compare Images
    Close Browser
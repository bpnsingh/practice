*** Settings ***
Documentation    Example using the space separated plain text format.
Library          OperatingSystem
Resource         ${var}.robot

*** Test Cases ***
TC1
    Log  ${user1}
    Log To Console   ${android_phone_1}


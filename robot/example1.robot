*** Settings ***
Documentation    Example using the space separated plain text format.
Library          OperatingSystem

*** Test Cases ***
Example
    Create File   ${TEMPDIR}/empty.txt
    create file   hello.txt      Hello world of python \n


*** Keywords ***
List Files
    [Arguments]     ${path}=.      ${optuins}=
    Execute
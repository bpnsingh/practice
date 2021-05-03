*** Settings ***
Documentation    Example using the space separated plain text format.
Library          OperatingSystem

*** Test Cases ***
Normal Error
    Fail        This is rather boring example


HTML Error
    Should Be Equal     35    42
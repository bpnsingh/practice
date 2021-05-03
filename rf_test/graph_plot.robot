*** Settings ***
Library    RobotChart
Library    Process
Test Template     Measure Square And Cubic
Suite Teardown    Embed Chart Diagrams
Force Tags    chart
Documentation   Parse the sleep time from console and collect the measured values for a chart diagram, the suite-teardown will embed the chart diagram to log-file.

*** Variables ***
${chart_title}      Sleep Measurement
${sq_label}         Square
${cb_label}         Cubic
${x_axis_label}     Latency [us]

*** Test Cases ***
Measure Sq And Cb 1     1
Measure Sq And Cb 2     2
Measure Sq And Cb 3     3
Measure Sq And Cb 4     4
Measure Sq And Cb 5     5
Measure Sq And Cb 6     6
Measure Sq And Cb 7     7


*** Keywords ***
Measure Square And Cubic
        [Arguments]   ${testinput}
    ${reference_value} =   Set Variable  ${testinput}

    ${proc} =    Start Process  /usr/bin/python  -c  print 'square %.2f inverse %.2f\\ncubic %.2f inverse %.2f' % (${testinput}*${testinput}, 1000/(${testinput}*${testinput}), ${testinput}*${testinput}*${testinput}, 1000/(${testinput}*${testinput}*${testinput}))
    ${result} =   Wait For Process    ${proc}
    Log  ${result.stderr}
        Process Should Be Stopped    ${proc}
    Should Be Equal As Integers   ${result.rc}   0
        ${amtch}  ${sq}  ${sqinv}  ${cb}  ${cbinv} =    Should Match Regexp   ${result.stdout}      [^\\d]+(\\d+.\\d+)[^\\d]+(\\d+.\\d+)[^\\d]+(\\d+.\\d+)[^\\d]+(\\d+.\\d+)
    Add To Chart   ${sq_label}  ${testinput}   ${sq}   ${sqinv}
    Add To Chart   ${cb_label}  ${testinput}   ${cb}   ${cbinv}


Embed Chart Diagrams
    Embed Bar Chart  Square Demo Chart  x_axis=0   y_axis=1   outfile=out-square.svg
    Embed Bar Chart  Inverse Demo Chart   x_axis=0   y_axis=2   outfile=out-inverse.svg
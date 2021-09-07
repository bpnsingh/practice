*** Variables ***
#possible values android or iOS
${mob}                     android
#possible values for env are beta,stag,prod
${env}                          beta
${PROJECT_DIR}                 /Users/bipinsengar/PycharmProjects/qa_bipin
#Nexus device info
&{android_phone_1}                      name=NEXUS  udid=emulator-5554  version=7.0  port=4724    platformName=android
#PIXEL Device info
&{android_phone_2}                      name=PIXEL  udid=a12b614d8558e539  version=10  port=4724   platformName=android
&{android_phone_3}                      name=SMSNG  udid=988913483844424937  version=8.0.0  port=4723  platformName=android
&{android_phone_4}                      name=PIXEL_OFFICE  udid=HT78P1A01760   systemPort=8200   version=11    port=4723  platformName=android
&{android_phone_5}                      name=MI            udid=9506301159ec   systemPort=8201   version=11    port=4724  platformName=android
&{sim_iphone_11}                        name=iPhone 11   udid=974C81AC-D1A0-430E-BD73-FE03A199C749    version=13.4
                                   ...  port=4724  platformName=ios
${REMOTE_URL}                 http://127.0.0.1:4723/wd/hub
&{dpbeta_app}                 pkg=co.switchapp.beta
                         ...  activity=co.switchapp.activity.LaunchActivity

&{textnow_app}                pkg=com.enflick.android.TextNow
                         ...  activity=com.enflick.android.TextNow.activities.MainActivity
${autoGrantPermissions}       true
${platformName}               android
${kill_appium_cmd}            ps -aef|grep appium|grep -v grep|awk '{print $2}'|xargs kill -9
${start_appium_cmd}           /usr/local/bin/appium -a 127.0.0.1 -p
&{android_app}                        beta=${PROJECT_DIR}/app/android/Dialpad Beta_V6.7.3-BETA.apk
                         ...  stag=${PROJECT_DIR}/app/android/Dialpad Beta_V6.1.1-BETA.apk
                         ...  prod=${PROJECT_DIR}/app/android/Dialpad Beta_V6.6-BETA.apk
${ios_app}                    ${PROJECT_DIR}/app/ios/Dialpad.app
${chromedriver}               ${PROJECT_DIR}/Resources/chromedriver
&{user1}                      email=tuxeved@royal-soft.net   password=Makesmartercalls     name=Env_Bipin Sengar
...                           did=(415) 469-1802  fname=Env_Bipin  account_type=opensignup
&{user2}                      email=socekox400@onmail.top    password=Makesmartercalls     name=HTHIRTEEN DIALPAD
...                           did=(415) 223-0552  fname=HTHIRTEEN  account_type=opensignup
&{okta_user}                  email=qa@gizmo9.com  password=Skunkworks1  name=QA_qa Gizmo9  did=(408) 713-1671
...                           fname=NA  account_type=okta   domain=gizmo9.com
&{O365_user}                  email=dialpad11@projectgemma.onmicrosoft.com  password=Makesmartercalls   name=Dialpad Eleven
...                           did=(415) 636-6962   fname=DIALPAD  account_type=o365
&{gsuite_user}                email=na  password=na  name=hone dialpad  did=(415) 223-0032   account_type=gsuite
&{pstn_user}                  email=na  password=na  name=Text Now PSTN  did=(415) 223-0032  fname=TEXT  account_type=textnow

#15_CallerID.robot
&{personal_caller_id}         name=Automation  number=+1(415) 223-0552
&{main_line_caller_id}        name=Automation Mainline  number=+1(415) 223-0570
&{dept_caller_id}             name=Android Dept  number=+1(415) 223-1029  dept=Android Dept
&{blocked_caller_id}          name=Unknown Number  number=NA  #number will be hidden for blocked

#16_Channels.robot
${channel}                    channel-automation
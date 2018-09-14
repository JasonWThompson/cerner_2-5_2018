@echo off

:: Kill-BadWebApp.bat
:: Author: Jason W. Thompson
:: Commentary: Not all automation tasks need to be super fancy to be useful. Nothing was more annoying than to get to 
:: work, order an omolette at the café, pull out my device, and find the battery drained. It turned out the culprit was
:: a web application that I used in my day to day duties. Even after I closed the browser, the application would stay 
:: running. It would use 100% of a CPU core. And this application even prevented my device from sleeping.
::
:: The solution was to write this very short, but powerful three line script to kill this application every day near the
:: end of my day. Fortunatly, I now use a better solution, but I keep this around to modify for the next time I run into
:: a similar application. I've changed the name of the executable in order to not unnecessarily reveal what software is 
:: running here at work. cerner_2^5_2018

taskkill /IM Bad-WebApp.exe /F 2> nul
exit /b 0
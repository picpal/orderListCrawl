if not exist "C:\chromeprofileDebug" mkdir "C:\chromeprofileDebug"
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dirs="C:\chromeprofileDebug"

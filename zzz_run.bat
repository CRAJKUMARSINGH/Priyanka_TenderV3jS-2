@echo off
echo Starting the app...

:: Start the server in a new command prompt
if exist server\package.json (
    echo Starting server...
    start cmd /k "cd server && npm start"
) else (
    echo No package.json found in server directory, skipping...
)

:: Start the client in a new command prompt
if exist client\package.json (
    echo Starting client...
    start cmd /k "cd client && npm start"
) else (
    echo No package.json found in client directory, skipping...
)

echo App is starting...
pause
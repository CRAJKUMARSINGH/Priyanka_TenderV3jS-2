@echo off
echo Installing npm dependencies for the app...

:: Navigate to the root directory and install dependencies
if exist package.json (
    echo Installing root dependencies...
    npm install
) else (
    echo No package.json found in root directory, skipping...
)

:: Navigate to client directory and install dependencies
if exist client\package.json (
    echo Installing client dependencies...
    cd client
    npm install
    cd ..
) else (
    echo No package.json found in client directory, skipping...
)

:: Navigate to server directory and install dependencies
if exist server\package.json (
    echo Installing server dependencies...
    cd server
    npm install
    cd ..
) else (
    echo No package.json found in server directory, skipping...
)

echo Installation complete!
pause
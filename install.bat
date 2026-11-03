@echo off
echo ==============================
echo ESP32 Data Logger Installer
echo ==============================

:: Check if Python is installed
echo Checking for Python installation...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Installing Python...
    start /wait "" installer\python_installer.exe /quiet
)

:: Install Python dependencies
echo Installing required Python dependencies...
installer\python\python.exe -m pip install -r installer\requirements.txt

:: Check ESP32 USB Drivers (CP210x and CH340)
echo Checking ESP32 USB Drivers...
IF NOT EXIST "C:\Windows\System32\drivers\silabser.sys" (
    echo Installing CP210x driver...
    start /wait "" installer\drivers\CP210x_Windows.exe /silent
)

IF NOT EXIST "C:\Windows\System32\drivers\ch341ser.sys" (
    echo Installing CH340 driver...
    start /wait "" installer\drivers\CH340_Windows.exe /silent
)

:: Create Shortcut on Desktop
echo Creating desktop shortcut...
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('C:\Users\%USERNAME%\Desktop\ESP32 Data Logger.lnk'); $s.TargetPath='%~dp0python_gui\ESP32Logger.exe'; $s.Save()"

:: Launch the Application
echo Installation complete. Launching application...
start "" python_gui\ESP32Logger.exe

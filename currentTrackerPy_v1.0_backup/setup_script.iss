[Setup]
AppName=CurrentTracker_v1.0
AppVersion=1.0
DefaultDirName={pf}\currentTracker_v1.0
DefaultGroupName=currentTracker_v1.0
OutputBaseFilename=currentTracker_v1.0Installer
SetupIconFile=installer\assets\icon.ico
WizardImageFile=installer\assets\installer_banner.bmp
WizardSmallImageFile=installer\assets\small_logo.bmp

[License]
LicenseFile=installer\license.txt

[Files]
Source: "dist\CurrentTracker_v1.0.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "installer\python_installer.exe"; DestDir: "{app}\python"; Flags: ignoreversion
Source: "installer\install_deps.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "path\to\dist\currentTrackerPy_v1.0.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "path\to\dist\pandas"; DestDir: "{app}\pandas"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "path\to\dist\pyqtgraph"; DestDir: "{app}\pyqtgraph"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "path\to\dist\pyqt5"; DestDir: "{app}\pyqt5"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "path\to\dist\serial"; DestDir: "{app}\serial"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "path\to\dist\sd"; DestDir: "{app}\sd"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\CurrentTracker_v1.0"; Filename: "{app}\CurrentTracker_v1.0.exe"

[Run]
Filename: "{app}\python\python_installer.exe"; Parameters: "/quiet"; Flags: waituntilterminated
Filename: "{app}\install_deps.bat"; Flags: waituntilterminated
Filename: "{app}\CurrentTracker_v1.0.exe"; Description: "Launch CurrentTracker_v1.0"; Flags: postinstall

[Code]
procedure InitializeWizard;
var
    CheckBox: TNewCheckBox;
begin
    CheckBox := TNewCheckBox.Create(WizardForm);
    CheckBox.Caption := 'I Agree to the Terms of Use';
    CheckBox.Parent := WizardForm.LicensePage;
    CheckBox.Left := ScaleX(10);
    CheckBox.Top := ScaleY(120);
    CheckBox.Width := ScaleX(200);
    CheckBox.Checked := False;

    WizardForm.NextButton.Enabled := False;
    CheckBox.OnClick := @CheckBoxClicked;
end;

procedure CheckBoxClicked(Sender: TObject);
begin
    WizardForm.NextButton.Enabled := TNewCheckBox(Sender).Checked;
end;

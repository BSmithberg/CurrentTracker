#define MyAppName "CurrentTracker"
#define MyAppVersion "1.0"
#define MyAppPublisher "Brian"
#define MyAppURL "https://github.com"
#define MyAppExeName "CurrentTracker.exe"

[Setup]
AppId={{ED5C73C1-2D89-4D7D-A3F5-4A61B20A12F1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\CurrentTracker
DefaultGroupName=CurrentTracker

OutputDir=Output
OutputBaseFilename=CurrentTrackerSetup

Compression=lzma
SolidCompression=yes

WizardStyle=modern

SetupIconFile=CurrentTracker.ico

PrivilegesRequired=lowest

UninstallDisplayIcon={app}\{#MyAppExeName}

DisableProgramGroupPage=yes

ChangesAssociations=no

ArchitecturesInstallIn64BitMode=x64compatible

VersionInfoVersion=1.0.0.0

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]

Name: "desktopicon"; \
Description: "Create a desktop shortcut"; \
GroupDescription: "Additional icons:"; \
Flags: unchecked

[Files]

Source: "dist\CurrentTracker\*"; \
DestDir: "{app}"; \
Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]

Name: "{group}\CurrentTracker"; \
Filename: "{app}\{#MyAppExeName}"

Name: "{autodesktop}\CurrentTracker"; \
Filename: "{app}\{#MyAppExeName}"; \
Tasks: desktopicon

[Run]

Filename: "{app}\{#MyAppExeName}"; \
Description: "Launch CurrentTracker"; \
Flags: nowait postinstall skipifsilent
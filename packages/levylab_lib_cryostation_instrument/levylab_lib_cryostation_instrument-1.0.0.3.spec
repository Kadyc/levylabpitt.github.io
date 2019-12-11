[Package]
Name="levylab_lib_cryostation_instrument"
Version="1.0.0.3"
Release=""
ID=5f93371551e0875c860a32144c00e646
File Format="vip"
Format Version="2017"
Display Name="Cryostation"


[Description]
Description="Program for logging Montana Instruments Cryostation status to the DSC. Provides a UI and API for getting information from the Cryostation."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.0.3]\0A- Initial build of Cryostation Monitor application and APIs"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=16.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall=""
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires="levylab_lib_levylab_instruments>=1.2.4.37"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=19
File 0="user.lib/LevyLab/PPMS Instrument/Cryostation Monitor and Control.vi"
File 1="user.lib/LevyLab/PPMS Instrument/Cryostation_inst.lvproj"
File 2="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation UI/Create UI.vi"
File 3="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation UI/Instrument.Cryostation UI.lvclass"
File 4="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation UI/Launch Cryostation UI.vi"
File 5="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation UI/Process.vi"
File 6="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Close Instrument.vi"
File 7="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Create Instrument SMO Name.vi"
File 8="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Cryostation Client.vi"
File 9="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Get Public API.vi"
File 10="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Get Temperature.vi"
File 11="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/getAll.vi"
File 12="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Handle Command.vi"
File 13="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/instrument.Cryostation.lvclass"
File 14="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/instrument.Cryostation.TestLauncher.vi"
File 15="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Open Instrument.vi"
File 16="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Process.vi"
File 17="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Typedefs/Commands-enum.ctl"
File 18="user.lib/LevyLab/PPMS Instrument/instrument.Cryostation/Typedefs/getAll--Cryostation--cluster.ctl"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Cryostation_Instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

[Package]
Name="levylab_lib_ppms_instrument"
Version="1.8.7.3"
Release=""
ID=c679a4ae9d950aceaa6d493fd7e3bdc3
File Format="vip"
Format Version="2017"
Display Name="PPMS Monitor and Control"


[Description]
Description="Monitor and Control application inheritng from Instrument Framework and SMO\0A- Log instrument status to the PGSQL database.\0A- UI and API for controlling magnet field, temperature, and rotator angle (PPMS2 only)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/PPMS-Monitor-and-Control"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Update to Instrument Framework v1.12\0A- UI improvements"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=19.0"
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
Requires="levylab_lib_levylab_instruments>=1.11.2.1"
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
Num Files=116
File 0="user.lib/LevyLab/PPMS Instrument/PPMS Monitor and Control.vi"
File 1="user.lib/LevyLab/PPMS Instrument/PPMS_inst.lvproj"
File 2="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Get SMO Name.vi"
File 3="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Get SMO PGSQL Log Paths.vi"
File 4="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Get SMO Port.vi"
File 5="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Get SMO Public API.vi"
File 6="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Handle getAll.vi"
File 7="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/instrument.PPMS3.lvclass"
File 8="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Magnet Limits.vi"
File 9="user.lib/LevyLab/PPMS Instrument/instrument.PPMS3/Typedefs/PPMS3.Commands-enum.ctl"
File 10="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get SMO Name.vi"
File 11="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get SMO PGSQL Log Paths.vi"
File 12="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get SMO Port.vi"
File 13="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Get SMO Public API.vi"
File 14="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Handle getAll.vi"
File 15="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/instrument.PPMS2.lvclass"
File 16="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Magnet Limits.vi"
File 17="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/PPMS2 Current to Field (Oe).vi"
File 18="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/PPMS2 Field (Oe) to Current.vi"
File 19="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/PPMS2 Field (T) to Current.vi"
File 20="user.lib/LevyLab/PPMS Instrument/instrument.PPMS2/Typedefs/PPMS2.Commands-enum.ctl"
File 21="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Get SMO Name.vi"
File 22="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Get SMO PGSQL Log Paths.vi"
File 23="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Get SMO Port.vi"
File 24="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Get SMO Public API.vi"
File 25="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Handle getAll.vi"
File 26="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/instrument.PPMS1.lvclass"
File 27="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Magnet Limits.vi"
File 28="user.lib/LevyLab/PPMS Instrument/instrument.PPMS1/Typedefs/PPMS1.Commands-enum.ctl"
File 29="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Instrument UI.PPMS.lvclass"
File 30="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/Process.vi"
File 31="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/TEST.vi"
File 32="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/private/Convert Number to String.vi"
File 33="user.lib/LevyLab/PPMS Instrument/instrument.PPMS UI/private/Elapsed Time String.vi"
File 34="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Close Hardware.vi"
File 35="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Close.vi"
File 36="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Convert Oersted to Tesla.vi"
File 37="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Convert Tesla to Oersted.vi"
File 38="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Angle.vi"
File 39="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Helium Level.vi"
File 40="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Magnet.vi"
File 41="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get PPMS Class.vi"
File 42="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get SMO Name.vi"
File 43="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get SMO PGSQL Log Paths.vi"
File 44="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get SMO Public API.vi"
File 45="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Get Temperature.vi"
File 46="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Handle Command.vi"
File 47="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Handle getAll.vi"
File 48="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/instrument.PPMS.lvclass"
File 49="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/instrument.PPMS.TestLauncher.vi"
File 50="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Magnet Limits.vi"
File 51="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Open Hardware.vi"
File 52="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Open.vi"
File 53="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Chamber Action to Ring.vi"
File 54="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Chamber Status Ring to String.vi"
File 55="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Get Angle.vi"
File 56="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Get Chamber.vi"
File 57="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Get Helium Level.vi"
File 58="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Get Magnet.vi"
File 59="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Get Temperature.vi"
File 60="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Magnet Status Ring to String.vi"
File 61="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Remote Client.vim"
File 62="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Set Angle.vi"
File 63="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Set Chamber.vi"
File 64="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Set Magnet.vi"
File 65="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Set Temperature.vi"
File 66="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/PPMS.Temperature Status Ring to String.vi"
File 67="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Process.vi"
File 68="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Select PPMS Class.vi"
File 69="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Angle.vi"
File 70="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Chamber.vi"
File 71="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Magnet.vi"
File 72="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Set Temperature.vi"
File 73="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Simple Test.vi"
File 74="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Test Create Start Stop Destroy.vi"
File 75="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Wait Progress Bar.vi"
File 76="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Chamber Command--enum.ctl"
File 77="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Chamber Status--ring.ctl"
File 78="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Commands-enum.ctl"
File 79="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.getAll--cluster.ctl"
File 80="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Magnet Status--cluster.ctl"
File 81="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Magnet Status--ring.ctl"
File 82="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Temperature Status--cluster.ctl"
File 83="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/PPMS.Temperature Status--ring.ctl"
File 84="user.lib/LevyLab/PPMS Instrument/instrument.PPMS/Typedefs/Select PPMS--Enum.ctl"
File 85="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument.dll"
File 86="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument_Example.vi"
File 87="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument_Example_Simple.vi"
File 88="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument_Server.exe"
File 89="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/ReleaseNotes.txt"
File 90="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/GetChamber.vi"
File 91="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/GetField.vi"
File 92="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/GetHelium.vi"
File 93="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/GetPosition.vi"
File 94="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/GetTemperature.vi"
File 95="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/OpenQDInstrument.vi"
File 96="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/QDInstrumentExceptionHandler.vi"
File 97="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/SetChamber.vi"
File 98="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/SetField.vi"
File 99="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/SetPosition.vi"
File 100="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/SetTemperature.vi"
File 101="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/QDInstrument/WaitFor.vi"
File 102="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/PPMS/GetPPMSItem.vi"
File 103="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/PPMS/GetPPMSItem_Example.vi"
File 104="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/PPMS/SendPPMSCommand.vi"
File 105="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/PPMS/SendPPMSCommand_Example.vi"
File 106="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/PPMS/SendPPMSCommand_Rotator.vi"
File 107="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_Float_Example.vi"
File 108="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_FLT.vi"
File 109="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S16.vi"
File 110="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S32.vi"
File 111="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_S8.vi"
File 112="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_STR.vi"
File 113="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U16.vi"
File 114="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U32.vi"
File 115="user.lib/LevyLab/PPMS Instrument/drivers/QDInstrument_LabView/CAN/CAN_QDInstrument.llb/ReadSDO_U8.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_levylab_lib_ppms_instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

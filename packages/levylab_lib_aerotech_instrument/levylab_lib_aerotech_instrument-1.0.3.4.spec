[Package]
Name="levylab_lib_aerotech_instrument"
Version="1.0.3.4"
Release=""
ID=389263544b85646b03a4e007d6ff5ab4
File Format="vip"
Format Version="2017"
Display Name="Aerotech Delay"


[Description]
Description="Program for setting delay with Aerotech delay line"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Aerotech-Delay-Line"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.3.4]\0A- Add error check to Get Delay.\0A- Add convert ps to um (speed).vi\0A- Update install location"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,oglib_appcontrol>=4.1.0.7,oglib_time>=4.0.1.3,levylab_lib_levylab_instruments>=1.5.8.70"
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
Num Files=188
File 0="user.lib/LevyLab/Aerotech/AerotechDelayLine.lvproj"
File 1="user.lib/LevyLab/Aerotech/Instrument.Aerotech UI/Instrument.Aerotech UI.lvclass"
File 2="user.lib/LevyLab/Aerotech/Instrument.Aerotech UI/Instrument.Aerotech UI.TestLauncher.vi"
File 3="user.lib/LevyLab/Aerotech/Instrument.Aerotech UI/Process.vi"
File 4="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Instrument.Aerotech.lvclass"
File 5="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Instrument.Aerotech.TestLauncher.vi"
File 6="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Process.vi"
File 7="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Typedefs/Instrument.Aerotech.Commands.ctl"
File 8="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Typedefs/Instrument.Aerotech.Configuration--Cluster.ctl"
File 9="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Typedefs/Instrument.Aerotech.getAll--Cluster.ctl"
File 10="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Private/convert ps to um (speed).vi"
File 11="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Private/convert ps to um.vi"
File 12="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Private/convert um to ps.vi"
File 13="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Overrides/Close Instrument.vi"
File 14="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Overrides/Get SMO Name.vi"
File 15="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Overrides/Get SMO Public API.vi"
File 16="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Overrides/getAll.vi"
File 17="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Overrides/Handle Command.vi"
File 18="user.lib/LevyLab/Aerotech/Instrument.Aerotech/Overrides/Open Instrument.vi"
File 19="user.lib/LevyLab/Aerotech/Instrument.Aerotech/API/Close.vi"
File 20="user.lib/LevyLab/Aerotech/Instrument.Aerotech/API/Get Delay.vi"
File 21="user.lib/LevyLab/Aerotech/Instrument.Aerotech/API/Open.vi"
File 22="user.lib/LevyLab/Aerotech/Instrument.Aerotech/API/Set Delay.vi"
File 23="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Samples.lvproj"
File 24="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/AlertError.vi"
File 25="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/AxisControl.ctl"
File 26="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/GetAxisIndex.vi"
File 27="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/GetAxisName.vi"
File 28="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/GetAxisNames.vi"
File 29="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/GetAxisNumber.vi"
File 30="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/GetControllerName.vi"
File 31="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/GetVersion.vi"
File 32="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Utility/ParseError.vi"
File 33="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/AxisDiagPacket.ctl"
File 34="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/ControllerDiagPacket.ctl"
File 35="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/ConvertDiagPacket.vi"
File 36="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/NewDiagPacketArrivedCallback.vi"
File 37="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/RegisterForDiagPackets.vi"
File 38="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/RetrieveDiagPacket.vi"
File 39="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/SetStatus.vi"
File 40="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Status/UnregisterForDiagPackets.vi"
File 41="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Scope/AxisDataResults.ctl"
File 42="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Scope/ControllerDataResults.ctl"
File 43="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Scope/GetScopeData.vi"
File 44="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Scope/TriggerScopeCollect.vi"
File 45="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetAxisParameter.vi"
File 46="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetAxisParameterDouble.vi"
File 47="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetAxisParameterFloat.vi"
File 48="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetAxisParameterInteger.vi"
File 49="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetAxisParameterLong.vi"
File 50="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetAxisParameterString.vi"
File 51="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetParameter.vi"
File 52="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetParameterDouble.vi"
File 53="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetParameterFloat.vi"
File 54="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetParameterInteger.vi"
File 55="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetParameterLong.vi"
File 56="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetParameterString.vi"
File 57="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetSystemParameter.vi"
File 58="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetSystemParameterDouble.vi"
File 59="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetSystemParameterFloat.vi"
File 60="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetSystemParameterInteger.vi"
File 61="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetSystemParameterLong.vi"
File 62="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetSystemParameterString.vi"
File 63="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetTaskParameter.vi"
File 64="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetTaskParameterDouble.vi"
File 65="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetTaskParameterFloat.vi"
File 66="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetTaskParameterInteger.vi"
File 67="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetTaskParameterLong.vi"
File 68="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/GetTaskParameterString.vi"
File 69="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SaveParameterFile.vi"
File 70="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SendParameterFile.vi"
File 71="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetAxisParameter.vi"
File 72="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetAxisParameterDouble.vi"
File 73="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetAxisParameterFloat.vi"
File 74="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetAxisParameterInteger.vi"
File 75="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetAxisParameterLong.vi"
File 76="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetAxisParameterString.vi"
File 77="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetParameter.vi"
File 78="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetParameterDouble.vi"
File 79="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetParameterFloat.vi"
File 80="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetParameterInteger.vi"
File 81="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetParameterLong.vi"
File 82="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetParameterString.vi"
File 83="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetSystemParameter.vi"
File 84="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetSystemParameterDouble.vi"
File 85="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetSystemParameterFloat.vi"
File 86="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetSystemParameterInteger.vi"
File 87="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetSystemParameterLong.vi"
File 88="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetSystemParameterString.vi"
File 89="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetTaskParameter.vi"
File 90="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetTaskParameterDouble.vi"
File 91="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetTaskParameterFloat.vi"
File 92="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetTaskParameterInteger.vi"
File 93="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetTaskParameterLong.vi"
File 94="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Parameters/SetTaskParameterString.vi"
File 95="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Abort.vi"
File 96="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/AbortMultiple.vi"
File 97="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/AbortSingle.vi"
File 98="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Abs.vi"
File 99="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/AnalogControl.vi"
File 100="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/AnalogTrack.vi"
File 101="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/AutoZero.vi"
File 102="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Circular.vi"
File 103="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/CircularCenter.vi"
File 104="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/CircularRadius.vi"
File 105="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Disable.vi"
File 106="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/DisableMultiple.vi"
File 107="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/DisableSingle.vi"
File 108="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Enable.vi"
File 109="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/EnableMultiple.vi"
File 110="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/EnableSingle.vi"
File 111="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/FaultAck.vi"
File 112="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/FaultAckMultiple.vi"
File 113="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/FaultAckSingle.vi"
File 114="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Freerun.vi"
File 115="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/FreerunMultiple.vi"
File 116="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/FreerunSingle.vi"
File 117="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Home.vi"
File 118="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/HomeMultiple.vi"
File 119="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/HomeSingle.vi"
File 120="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Inc.vi"
File 121="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Linear.vi"
File 122="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/MoveAbs.vi"
File 123="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/MoveAbsMultiple.vi"
File 124="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/MoveAbsSingle.vi"
File 125="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/MoveInc.vi"
File 126="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/MoveIncMultiple.vi"
File 127="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/MoveIncSingle.vi"
File 128="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Oscillate.vi"
File 129="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/RampRate.vi"
File 130="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/RampRateCoordinated.vi"
File 131="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/RampRateMultiple.vi"
File 132="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/RampRateSingle.vi"
File 133="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Servo.vi"
File 134="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/Wait.vi"
File 135="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/WaitMultiple.vi"
File 136="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Motion/WaitSingle.vi"
File 137="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Initialize/Connect.vi"
File 138="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Initialize/Disconnect.vi"
File 139="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Initialize/Reset.vi"
File 140="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileDelete.vi"
File 141="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileFreeSpace.vi"
File 142="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileGet.vi"
File 143="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileGetInfo.vi"
File 144="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileList.vi"
File 145="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileOnController.vi"
File 146="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileOptimize.vi"
File 147="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileRetrieve.vi"
File 148="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/File/FileSend.vi"
File 149="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/Display.vi"
File 150="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/FileManager.vi"
File 151="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/IO.vi"
File 152="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/MultiAxisControl.vi"
File 153="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/Parameters.vi"
File 154="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/PlotScopeData.vi"
File 155="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/SimpleMotion.vi"
File 156="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/SimpleMotion2.vi"
File 157="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/SimpleOscillate.vi"
File 158="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Examples/SingleAxisControl.vi"
File 159="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/AcknowledgeAll.vi"
File 160="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ExecuteCommand.vi"
File 161="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ExecuteProgram.vi"
File 162="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ReadDoubleGlobal.vi"
File 163="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ReadDoubleGlobals.vi"
File 164="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ReadGlobal.vi"
File 165="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ReadGlobals.vi"
File 166="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ReadIntegerGlobal.vi"
File 167="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/ReadIntegerGlobals.vi"
File 168="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/SetAnalogOutput.vi"
File 169="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/SetDigitalOutput.vi"
File 170="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/StopProgram.vi"
File 171="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/WriteDoubleGlobal.vi"
File 172="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/WriteDoubleGlobals.vi"
File 173="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/WriteGlobal.vi"
File 174="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/WriteGlobals.vi"
File 175="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/WriteIntegerGlobal.vi"
File 176="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Commands/WriteIntegerGlobals.vi"
File 177="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/AeroBasic.dll"
File 178="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/AeroBasic64.dll"
File 179="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Aerotech.Common.dll"
File 180="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Aerotech.Ensemble.dll"
File 181="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Aerotech.Ensemble.LabVIEW.dll"
File 182="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Ensemble LabVIEW Operator Interface.exe"
File 183="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Ensemble LabVIEW Operator Interface.ini"
File 184="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/EnsembleCore.dll"
File 185="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/EnsembleCore64.dll"
File 186="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Data/Aerotech.Ensemble.dll"
File 187="user.lib/LevyLab/Aerotech/Aerotech-Ensemble-LabVIEW/8.2/Bin/Data/Aerotech.Ensemble.LabVIEW.dll"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Aerotech_Instrument.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

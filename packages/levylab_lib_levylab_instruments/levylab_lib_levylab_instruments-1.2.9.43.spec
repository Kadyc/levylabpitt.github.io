[Package]
Name="levylab_lib_levylab_instruments"
Version="1.2.9.43"
Release=""
ID=41f81d1c511a149f9ff9b12c50bb904d
File Format="vip"
Format Version="2017"
Display Name="Instruments"


[Description]
Description="Abstract instrument.lvclass"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.9.43]\0A- Fix error that would prevent configuration from being written to the class wire"
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
Requires="jki_lib_caraya>=0.6.3.54,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,labview-zmq>=3.5.1.109,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_seh>=2.1.10.1,ni_lib_stm>=3.1.0.9,nise_syslog>=1.3.3.27,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5"
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
Num Files=219
File 0="user.lib/Levylab/Levylab Instruments/instrument.lvproj"
File 1="user.lib/Levylab/Levylab Instruments/LICENSE"
File 2="user.lib/Levylab/Levylab Instruments/README.md"
File 3="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Decode.vi"
File 4="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Encode.vi"
File 5="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI.lvclass"
File 6="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Close Connection.vi"
File 7="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor - Start.vi"
File 8="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor - Stop.vi"
File 9="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor.vi"
File 10="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Open Client Connection.vi"
File 11="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Open Server Connection.vi"
File 12="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read listener ID.vi"
File 13="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read Message.vi"
File 14="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read STM connection info.vi"
File 15="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RemoteControl.STM.lvclass"
File 16="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RemoteControl.STM.TestLauncher.vi"
File 17="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Send Message.vi"
File 18="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client.vi"
File 19="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client_OO.vi"
File 20="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client_SM.vi"
File 21="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Server.vi"
File 22="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Server_OO.vi"
File 23="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Write listener ID.vi"
File 24="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Write STM connection info.vi"
File 25="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Client - JKI SM or SMO.vi"
File 26="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Close Connection.vi"
File 27="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor - Start.vi"
File 28="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor - Stop.vi"
File 29="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor.vi"
File 30="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Client.vi"
File 31="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Connection Monitor.vi"
File 32="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Server.vi"
File 33="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/CreatePrivateEvents.vi"
File 34="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/CreatePublicEvents.vi"
File 35="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/DestroyPrivateEvents.vi"
File 36="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/DestroyPublicEvents.vi"
File 37="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Client Connection.vi"
File 38="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Server Connection.vi"
File 39="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Process.vi"
File 40="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read address.vi"
File 41="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Commands.vi"
File 42="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Message.vi"
File 43="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Port.vi"
File 44="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Remote Client.vi"
File 45="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.Configure.vi"
File 46="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.GetPrivateEvents.vi"
File 47="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.GetPublicEvents.vi"
File 48="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.lvclass"
File 49="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.SendMessageFromProcess.vi"
File 50="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.SendMessageToProcess.vi"
File 51="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.TestLauncher.ConnectionMonitor.vi"
File 52="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.TestLauncher.Server.vi"
File 53="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControlGlobal.vi"
File 54="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Send and Receive Message.vi"
File 55="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Send Message.vi"
File 56="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/VirtualTestInstrument.vi"
File 57="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write address.vi"
File 58="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Commands.vi"
File 59="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Port.vi"
File 60="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Message--Cluster.ctl"
File 61="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--Cluster.ctl"
File 62="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Configure.ctl"
File 63="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Reply Message.ctl"
File 64="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.SendMessageToProcess.ctl"
File 65="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--Cluster.ctl"
File 66="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.Reply Remote Message.ctl"
File 67="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.SendMessageFromProcess.ctl"
File 68="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/RC Process Type--Enum.ctl"
File 69="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Variant with Message ID--cluster.ctl"
File 70="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/CreatePrivateEvents.vi"
File 71="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/DestroyPrivateEvents.vi"
File 72="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Error Log Generator Example 1.vi"
File 73="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Log Error.vi"
File 74="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.GetPrivateEvents.vi"
File 75="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.LogError.vi"
File 76="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.lvclass"
File 77="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.TestLauncher.vi"
File 78="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Process.vi"
File 79="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Typedefs/PrivateEvents--Cluster.ctl"
File 80="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Typedefs/PrivateEvents--Logger.Error.Log Error.ctl"
File 81="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/CreatePrivateEvents.vi"
File 82="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/CreatePublicEvents.vi"
File 83="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/DestroyPrivateEvents.vi"
File 84="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/DestroyPublicEvents.vi"
File 85="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.GetPublicEvents.vi"
File 86="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.lvclass"
File 87="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.TestLauncher.vi"
File 88="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.WriteVariable.vi"
File 89="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.GetPrivateEvents.vi"
File 90="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.ReadVariable.vi"
File 91="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Process.vi"
File 92="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Read from DSC (unused).vi"
File 93="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Write Cluster to DSC.vi"
File 94="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Write to DSC.vi"
File 95="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Cluster.ctl"
File 96="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Logger.DSC.Set Address.ctl"
File 97="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Logger.DSC.Write Variable.ctl"
File 98="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PublicEvents--Cluster.ctl"
File 99="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PublicEvents--Logger.DSC.Read Variable.ctl"
File 100="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.lvclass"
File 101="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.TestLauncher.vi"
File 102="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Process.vi"
File 103="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Read path.vi"
File 104="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Write path.vi"
File 105="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/Handle Error.vi"
File 106="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/LevyLab.lvclass"
File 107="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/LevyLab.TestLauncher.vi"
File 108="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/Process.vi"
File 109="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API Commands--constant.vi"
File 110="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Close Instrument.vi"
File 111="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Close Instrument.vi.orig"
File 112="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Configure Instrument.vi"
File 113="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Create Instrument SMO Name.vi"
File 114="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Create Instrument SMO Name.vi.orig"
File 115="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Create Instrument.vi"
File 116="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/CreatePrivateEvents.vi"
File 117="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/CreatePrivateEvents.vi.orig"
File 118="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/CreatePublicEvents.vi"
File 119="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/CreatePublicEvents.vi.orig"
File 120="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/DestroyPrivateEvents.vi"
File 121="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/DestroyPublicEvents.vi"
File 122="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/enumerateStaticDependencies.vi"
File 123="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/enumerateStaticDependencies.vi.orig"
File 124="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Get Instrument Dependencies.vi"
File 125="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Get Public API.vi"
File 126="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Get Public API.vi.orig"
File 127="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/getAll.vi"
File 128="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/getAll.vi.orig"
File 129="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Handle Command.vi"
File 130="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Handle Command.vi.orig"
File 131="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.Configuration Window.vi"
File 132="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.Configuration Window.vi.orig"
File 133="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.GetPrivateEvents.vi"
File 134="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.GetPublicEvents.vi"
File 135="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.lvclass"
File 136="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.lvclass.orig"
File 137="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.MessageFromProcess.vi"
File 138="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.MessageFromProcess.vi.orig"
File 139="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.MessageToProcess.vi"
File 140="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.MessageToProcess.vi.orig"
File 141="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.Read Configuration File.vi"
File 142="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.Read Configuration.vi"
File 143="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.TestLauncher.vi"
File 144="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.Write Configuration File.vi"
File 145="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.Write Configuration.vi"
File 146="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/List Devices.vi"
File 147="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/List Devices.vi.orig"
File 148="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Open Instrument.vi"
File 149="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Open Instrument.vi.orig"
File 150="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Process.vi"
File 151="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Process.vi.orig"
File 152="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Read Configuration Class.vi"
File 153="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Read Configuration Class.vi.orig"
File 154="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Read Configuration.vi.orig"
File 155="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Read Hardware Address.vi"
File 156="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Read Hardware Address.vi.orig"
File 157="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Remote Client.vi"
File 158="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Remote Client.vi.orig"
File 159="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Configuration Class.vi"
File 160="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Configuration Class.vi.orig"
File 161="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Configuration Path.vi"
File 162="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Configuration.vi.orig"
File 163="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Hardware Address.vi"
File 164="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Hardware Address.vi.orig"
File 165="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write Process Name.vi"
File 166="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write SMO Configuration.vi"
File 167="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Write SMO Configuration.vi.orig"
File 168="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Configuration--Cluster.ctl"
File 169="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Configuration--Cluster.ctl.orig"
File 170="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/DSC Configuration--Cluster.ctl"
File 171="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/DSC Configuration--Cluster.ctl.orig"
File 172="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/HW Configuration--Cluster.ctl"
File 173="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/HW Configuration--Cluster.ctl.orig"
File 174="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Cluster.ctl"
File 175="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Cluster.ctl.orig"
File 176="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Instrument.MessageToProcess.ctl"
File 177="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Instrument.MessageToProcess.ctl.orig"
File 178="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Cluster.ctl"
File 179="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Cluster.ctl.orig"
File 180="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.get all.ctl"
File 181="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.MessageFromProcess.ctl"
File 182="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.MessageFromProcess.ctl.orig"
File 183="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO Configuration--Cluster.ctl"
File 184="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO Configuration--Cluster.ctl.orig"
File 185="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO RC Type--enum.ctl"
File 186="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO RC Type--enum.ctl.orig"
File 187="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Configuration.lvclass"
File 188="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Read Configuration.vi"
File 189="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Configuration.vi"
File 190="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Path.vi"
File 191="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Get Bias Voltage.vi"
File 192="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Instrument.VSource.lvclass"
File 193="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Set Bias Voltage.vi"
File 194="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Get Data.vi"
File 195="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Instrument.VNA.lvclass"
File 196="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Average.vi"
File 197="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Format.vi"
File 198="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Measurement.vi"
File 199="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Power.vi"
File 200="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Sweep.vi"
File 201="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Conversion--enum.ctl"
File 202="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Format--enum.ctl"
File 203="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Measurement--enum.ctl"
File 204="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Sweep Type--enum.ctl"
File 205="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Angle.vi"
File 206="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Helium Level.vi"
File 207="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Magnet Field.vi"
File 208="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Nitrogen Level.vi"
File 209="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Temperature.vi"
File 210="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Instrument.Cryostat.lvclass"
File 211="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Angle.vi"
File 212="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Magnet Field.vi"
File 213="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Temperature.vi"
File 214="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Magnet Setpoint.vi"
File 215="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Temperature Setpoint.vi"
File 216="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Axis--Enum.ctl"
File 217="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Mode--Enum.ctl"
File 218="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Rotator Axis--Enum.ctl"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=14
File 0="_functions_levylab_lib_levylab_instruments_1.mnu"
File 1="_functions_levylab_lib_levylab_instruments_10.mnu"
File 2="_functions_levylab_lib_levylab_instruments_11.mnu"
File 3="_functions_levylab_lib_levylab_instruments_12.mnu"
File 4="_functions_levylab_lib_levylab_instruments_13.mnu"
File 5="_functions_levylab_lib_levylab_instruments_2.mnu"
File 6="_functions_levylab_lib_levylab_instruments_3.mnu"
File 7="_functions_levylab_lib_levylab_instruments_4.mnu"
File 8="_functions_levylab_lib_levylab_instruments_5.mnu"
File 9="_functions_levylab_lib_levylab_instruments_6.mnu"
File 10="_functions_levylab_lib_levylab_instruments_7.mnu"
File 11="_functions_levylab_lib_levylab_instruments_8.mnu"
File 12="_functions_levylab_lib_levylab_instruments_9.mnu"
File 13="functions_Levylab_lib_Levylab_Instruments.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

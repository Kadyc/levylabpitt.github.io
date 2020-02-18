[Package]
Name="levylab_lib_levylab_instruments"
Version="1.5.7.69"
Release=""
ID=c6c396ee8895aa0392b100063b11ca32
File Format="vip"
Format Version="2017"
Display Name="Instruments"


[Description]
Description="Abstract instrument.lvclass"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.5.8.69]\0A- reinstate Open/Close Instrument protected methods\0A- Open/Close are public API"
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
PostInstall="<OS Boot Volume Root>\\user\\patrick\\hg\\levylab_inst\\build support\\Post-Install Custom Action.vi"
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires="drjdpowell_lib_messenging>=1.10.9.115,jdp_science_lib_common_utilities>=1.1.1.7,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,labview-zmq>=3.5.1.109,lava_lib_ui_tools>=1.4.1.74,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_seh>=2.1.10.1,ni_lib_stm>=3.1.0.9,nise_syslog>=1.3.3.27,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=265
File 0="user.lib/Levylab/Levylab Instruments/instrument.lvproj"
File 1="user.lib/Levylab/Levylab Instruments/LICENSE"
File 2="user.lib/Levylab/Levylab Instruments/README.md"
File 3="user.lib/Levylab/Levylab Instruments/SMOs/Shortcuts.vi"
File 4="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Decode.vi"
File 5="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Encode.vi"
File 6="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI.lvclass"
File 7="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Close Connection.vi"
File 8="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor - Loop.vi"
File 9="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor - Stop.vi"
File 10="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/onCreate.vi"
File 11="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Open Client Connection.vi"
File 12="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Open Server Connection.vi"
File 13="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read listener ID.vi"
File 14="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read Message.vi"
File 15="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read STM connection info.vi"
File 16="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RemoteControl.STM.lvclass"
File 17="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RemoteControl.STM.TestLauncher.vi"
File 18="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Send Message.vi"
File 19="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client.vi"
File 20="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client_OO.vi"
File 21="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client_SM.vi"
File 22="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Server.vi"
File 23="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Server_part_OO.vi"
File 24="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Write listener ID.vi"
File 25="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Write STM connection info.vi"
File 26="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Client - JKI SM or SMO.vi"
File 27="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Close Connection.vi"
File 28="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor - Loop.vi"
File 29="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor - Stop.vi"
File 30="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Client.vi"
File 31="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Server.vi"
File 32="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/CreatePrivateEvents.vi"
File 33="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/CreatePublicEvents.vi"
File 34="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/DestroyPrivateEvents.vi"
File 35="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/DestroyPublicEvents.vi"
File 36="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Error Dialog.vi"
File 37="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/onCreate.vi"
File 38="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Client Connection.vi"
File 39="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Server Connection.vi"
File 40="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Process.vi"
File 41="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Process_Backup.vi"
File 42="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read address.vi"
File 43="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Commands.vi"
File 44="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Message.vi"
File 45="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Port.vi"
File 46="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Remote Client.vi"
File 47="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.Configure.vi"
File 48="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.GetPrivateEvents.vi"
File 49="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.GetPublicEvents.vi"
File 50="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.lvclass"
File 51="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.SendMessageFromProcess.vi"
File 52="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.SendMessageToProcess.vi"
File 53="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.TestLauncher.ConnectionMonitor.vi"
File 54="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.TestLauncher.Server.vi"
File 55="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControlGlobal.vi"
File 56="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Send and Receive Message.vi"
File 57="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Send Message.vi"
File 58="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Time Message Events.vi"
File 59="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/VirtualTestInstrument.vi"
File 60="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Address.vi"
File 61="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Commands.vi"
File 62="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Debug Mode.vi"
File 63="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Port.vi"
File 64="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Message--Cluster.ctl"
File 65="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--Cluster.ctl"
File 66="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Configure.ctl"
File 67="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Reply Message.ctl"
File 68="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.SendMessageToProcess.ctl"
File 69="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--Cluster.ctl"
File 70="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.Reply Remote Message.ctl"
File 71="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.SendMessageFromProcess.ctl"
File 72="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/RC Process Type--Enum.ctl"
File 73="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Variant with Message ID--cluster.ctl"
File 74="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/CreatePrivateEvents.vi"
File 75="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/DestroyPrivateEvents.vi"
File 76="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Error Log Generator Example 1.vi"
File 77="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Log Error.vi"
File 78="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.GetPrivateEvents.vi"
File 79="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.LogError.vi"
File 80="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.lvclass"
File 81="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.TestLauncher.vi"
File 82="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Process.vi"
File 83="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Typedefs/PrivateEvents--Cluster.ctl"
File 84="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Typedefs/PrivateEvents--Logger.Error.Log Error.ctl"
File 85="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/CreatePrivateEvents.vi"
File 86="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/CreatePublicEvents.vi"
File 87="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/DestroyPrivateEvents.vi"
File 88="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/DestroyPublicEvents.vi"
File 89="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.GetPublicEvents.vi"
File 90="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.lvclass"
File 91="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.TestLauncher.vi"
File 92="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.WriteVariable.vi"
File 93="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.GetPrivateEvents.vi"
File 94="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.ReadVariable.vi"
File 95="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Process.vi"
File 96="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Read from DSC (unused).vi"
File 97="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Write Cluster to DSC.vi"
File 98="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Write to DSC.vi"
File 99="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Cluster.ctl"
File 100="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Logger.DSC.Set Address.ctl"
File 101="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Logger.DSC.Write Variable.ctl"
File 102="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PublicEvents--Cluster.ctl"
File 103="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PublicEvents--Logger.DSC.Read Variable.ctl"
File 104="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.lvclass"
File 105="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.TestLauncher.vi"
File 106="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Process.vi"
File 107="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Read path.vi"
File 108="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Write path.vi"
File 109="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/Handle Error.vi"
File 110="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/LevyLab.lvclass"
File 111="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/LevyLab.TestLauncher.vi"
File 112="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/Process.vi"
File 113="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Create UI.vi"
File 114="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Instrument UI.lvclass"
File 115="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Instrument UI.TestLauncher.vi"
File 116="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Process.vi"
File 117="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.lvclass"
File 118="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.TestLauncher.vi"
File 119="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Process.vi"
File 120="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Configuration--Cluster.ctl"
File 121="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/DSC Configuration--Cluster.ctl"
File 122="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/HW Configuration--Cluster.ctl"
File 123="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Cluster.ctl"
File 124="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Instrument.MessageToProcess.ctl"
File 125="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Cluster.ctl"
File 126="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.get all.ctl"
File 127="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.MessageFromProcess.ctl"
File 128="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO Configuration--Cluster.ctl"
File 129="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO RC Type--enum.ctl"
File 130="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Remote Client.vi"
File 131="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Write Configuration Path.vi"
File 132="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Error Dialog.vi"
File 133="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Get Instrument Dependencies.vi"
File 134="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Configuration Window.vi"
File 135="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.GetPrivateEvents.vi"
File 136="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.MessageFromProcess.vi"
File 137="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Read Configuration File.vi"
File 138="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Read Configuration.vi"
File 139="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Write Configuration File.vi"
File 140="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Write Configuration.vi"
File 141="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/List Devices.vi"
File 142="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/CreatePrivateEvents.vi"
File 143="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/CreatePublicEvents.vi"
File 144="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/DestroyPrivateEvents.vi"
File 145="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/DestroyPublicEvents.vi"
File 146="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/enumerateStaticDependencies.vi"
File 147="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/Handle Error.vi"
File 148="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Close Instrument.vi"
File 149="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Configure Instrument.vi"
File 150="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Name.vi"
File 151="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Port.vi"
File 152="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Public API.vi"
File 153="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO RC Type.vi"
File 154="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/getAll.vi"
File 155="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Handle Command.vi"
File 156="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Open Instrument.vi"
File 157="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Close.vi"
File 158="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Create SMO.vi"
File 159="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Get ALL.vi"
File 160="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/HELP.vi"
File 161="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.GetPublicEvents.vi"
File 162="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.MessageToProcess.vi"
File 163="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Open.vi"
File 164="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Configuration Class.vi"
File 165="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Hardware Address.vi"
File 166="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Write Hardware Address.vi"
File 167="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Configuration.lvclass"
File 168="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Read Configuration.vi"
File 169="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Configuration.vi"
File 170="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Path.vi"
File 171="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Get Bias Voltage.vi"
File 172="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Instrument.VSource.lvclass"
File 173="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Set Bias Voltage.vi"
File 174="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Get Data.vi"
File 175="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Instrument.VNA.lvclass"
File 176="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Average.vi"
File 177="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Format.vi"
File 178="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Measurement.vi"
File 179="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Power.vi"
File 180="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Sweep.vi"
File 181="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Conversion--enum.ctl"
File 182="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Format--enum.ctl"
File 183="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Measurement--enum.ctl"
File 184="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Sweep Type--enum.ctl"
File 185="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Get Strain.vi"
File 186="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Instrument.Strain.lvclass"
File 187="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Set Strain.vi"
File 188="user.lib/Levylab/Levylab Instruments/Instrument Types/Optical Delay Line/Get Delay.vi"
File 189="user.lib/Levylab/Levylab Instruments/Instrument Types/Optical Delay Line/Instrument.OpticalDelayLine.lvclass"
File 190="user.lib/Levylab/Levylab Instruments/Instrument Types/Optical Delay Line/Set Delay.vi"
File 191="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Angle.vi"
File 192="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Helium Level.vi"
File 193="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Magnet Field.vi"
File 194="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Nitrogen Level.vi"
File 195="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Pressure.vi"
File 196="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Temperature.vi"
File 197="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Instrument.Cryostat.lvclass"
File 198="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Angle.vi"
File 199="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Magnet Field.vi"
File 200="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Temperature.vi"
File 201="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Magnet Setpoint.vi"
File 202="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Temperature Setpoint.vi"
File 203="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Axis--Enum.ctl"
File 204="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Mode--Enum.ctl"
File 205="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Rotator Axis--Enum.ctl"
File 206="user.lib/Levylab/Levylab Instruments/Instrument Types/CBridge/Get Capacitance.vi"
File 207="user.lib/Levylab/Levylab Instruments/Instrument Types/CBridge/Instrument.CBridge.lvclass"
File 208="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument UI/LevyLab Instrument UI.lvclass"
File 209="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument UI/LevyLab Instrument UI.TestLauncher.vi"
File 210="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument UI/Process.vi"
File 211="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/LevyLab Instrument.AppLauncher.vi"
File 212="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/LevyLab Instrument.lvclass"
File 213="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Process.vi"
File 214="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Typedefs/LevyLab Instrument.Commands--Enum.ctl"
File 215="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Typedefs/LevyLab Instrument.Configuration--Cluster.ctl"
File 216="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Typedefs/LevyLab Instrument.getAll--Cluster.ctl"
File 217="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Protected/LevyLab Instrument.Client.vi"
File 218="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/Instrument Types.vi"
File 219="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Configuration Window.vi"
File 220="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Read Configuration File.vi"
File 221="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Read Configuration.vi"
File 222="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Write Configuration File.vi"
File 223="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Write Configuration.vi"
File 224="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Configure Instrument.vi"
File 225="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO Name.vi"
File 226="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO Port.vi"
File 227="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO Public API.vi"
File 228="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO RC Type.vi"
File 229="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/getAll.vi"
File 230="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Handle Command.vi"
File 231="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/Close.vi"
File 232="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/LevyLab Instrument.getAll.vi"
File 233="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/LevyLab Instrument.HELP.vi"
File 234="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/Open.vi"
File 235="ProjectTemplates/Source/LevyLab/Instrument/LevyLab Instrument.lvproj"
File 236="ProjectTemplates/Source/LevyLab/Instrument/ProjectSetup.vi"
File 237="ProjectTemplates/Source/LevyLab/Instrument/project/.gitignore"
File 238="ProjectTemplates/Source/LevyLab/Instrument/project/LICENSE"
File 239="ProjectTemplates/Source/LevyLab/Instrument/project/README.md"
File 240="ProjectTemplates/Source/LevyLab/Instrument/project/build support/7zSD.sfx"
File 241="ProjectTemplates/Source/LevyLab/Instrument/project/build support/buildspec-template.vipt.rename"
File 242="ProjectTemplates/Source/LevyLab/Instrument/project/build support/icon.ico"
File 243="ProjectTemplates/Source/LevyLab/Instrument/project/build support/Post-Build Custom Action.vi"
File 244="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Build Application with API.vi"
File 245="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Build Application.vi"
File 246="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Build Installer with API.vi"
File 247="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Build Installer.vi"
File 248="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Copy 7zSD.SFX.vi"
File 249="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Copy Package.vi"
File 250="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Create Folders.vi"
File 251="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Execute 7z bat.vi"
File 252="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Post Build Script.vi"
File 253="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/PostBuildSupport.lvclass"
File 254="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Test 7z.bat.vi"
File 255="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Test Script.vi"
File 256="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Update Build Version.vi"
File 257="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Write 7z config.vi"
File 258="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Write 7z.bat.vi"
File 259="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Write Output Package File Path.vi"
File 260="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Write Package Source Folder.vi"
File 261="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Write Package Version.vi"
File 262="ProjectTemplates/Source/LevyLab/Instrument/project/build support/PostBuildSupport/Write Product Name.vi"
File 263="ProjectTemplates/Source/LevyLab/images/instrument.png"
File 264="ProjectTemplates/MetaData/LevyLab_Instrument_MetaData.xml"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=24
File 0="_functions_levylab_lib_levylab_instruments_1.mnu"
File 1="_functions_levylab_lib_levylab_instruments_10.mnu"
File 2="_functions_levylab_lib_levylab_instruments_11.mnu"
File 3="_functions_levylab_lib_levylab_instruments_12.mnu"
File 4="_functions_levylab_lib_levylab_instruments_13.mnu"
File 5="_functions_levylab_lib_levylab_instruments_14.mnu"
File 6="_functions_levylab_lib_levylab_instruments_15.mnu"
File 7="_functions_levylab_lib_levylab_instruments_16.mnu"
File 8="_functions_levylab_lib_levylab_instruments_17.mnu"
File 9="_functions_levylab_lib_levylab_instruments_18.mnu"
File 10="_functions_levylab_lib_levylab_instruments_19.mnu"
File 11="_functions_levylab_lib_levylab_instruments_2.mnu"
File 12="_functions_levylab_lib_levylab_instruments_20.mnu"
File 13="_functions_levylab_lib_levylab_instruments_21.mnu"
File 14="_functions_levylab_lib_levylab_instruments_22.mnu"
File 15="_functions_levylab_lib_levylab_instruments_23.mnu"
File 16="_functions_levylab_lib_levylab_instruments_3.mnu"
File 17="_functions_levylab_lib_levylab_instruments_4.mnu"
File 18="_functions_levylab_lib_levylab_instruments_5.mnu"
File 19="_functions_levylab_lib_levylab_instruments_6.mnu"
File 20="_functions_levylab_lib_levylab_instruments_7.mnu"
File 21="_functions_levylab_lib_levylab_instruments_8.mnu"
File 22="_functions_levylab_lib_levylab_instruments_9.mnu"
File 23="functions_Levylab_lib_Levylab_Instruments.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

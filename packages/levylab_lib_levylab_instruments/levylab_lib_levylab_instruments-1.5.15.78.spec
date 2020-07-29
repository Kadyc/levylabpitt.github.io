[Package]
Name="levylab_lib_levylab_instruments"
Version="1.5.15.78"
Release=""
ID=b9b54432a95eb12694cd32631a9dd7d6
File Format="vip"
Format Version="2017"
Display Name="Instrument Framework"


[Description]
Description="An object-oriented framework based on JKI SMOs, developed by the LevyLab at the University of Pittsburgh\0D\0A\0D\0AAn Instrument developed using this framework will have the access to the following capabilities:\0D\0A\0D\0A- Knows how to communicate with a piece of hardware (provides a hardware abstraction layer (HAL))\0D\0A- Periodically polls the instrument for its settings and logs them to a DSC database\0D\0A- Defines an API to allow external programs to control compiled instances of the application and remotely across a network (Currently provided by National Instruments' Simple Messaging Library (STM), however a cross-platform protocol is developed using 0MQ)\0D\0A- Provide a user interface (optional but probably desirable).\0D\0A- Methods for reading and writing configuration from disk.\0D\0A\0D\0AThe LevyLab Instrument Framework makes extensive use of JKI State Machines and JKI State Machine Objects.z"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.5.15.79]\0A-build for LV 2019\0A\0A[1.5.15.77]\0D\0A- Change reentrant executation of Remote Client.vi (Issue #21)\0D\0A- Open.vi and Close.vi now Open and Close the TCP connection"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=20.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall="<OS Boot Volume Root>\\user\\patrick\\git\\LevyLab-Instrument-Framework\\build support\\Post-Install Custom Action.vi"
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,labview-zmq>=3.5.1.109,lava_lib_ui_tools>=1.4.1.74,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_seh>=2.1.10.1,ni_lib_stm>=3.1.0.9,nise_syslog>=1.3.3.27,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=285
File 0="user.lib/Levylab/Levylab Instruments/instrument.lvproj"
File 1="user.lib/Levylab/Levylab Instruments/SMOs/Shortcuts.vi"
File 2="user.lib/Levylab/Levylab Instruments/SMOs/showrunningvis.vi"
File 3="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Decode.vi"
File 4="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Encode.vi"
File 5="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI.lvclass"
File 6="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Build Endpoint.vi"
File 7="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Client 3.vi"
File 8="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Close Connection.vi"
File 9="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Connection Monitor - Stop.vi"
File 10="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/CreatePrivateEvents.vi"
File 11="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/CreatePublicEvents.vi"
File 12="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/DestroyPrivateEvents.vi"
File 13="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/DestroyPublicEvents.vi"
File 14="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/DNR Process.vi"
File 15="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Get Connections.vi"
File 16="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Open Client Connection.vi"
File 17="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Open Context.vi"
File 18="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Open Server Connection.vi"
File 19="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Read Message.vi"
File 20="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Receive Ack.vi"
File 21="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/RemoteControl.ZMQ.lvclass"
File 22="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Req Client 2.vi"
File 23="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Send Ack.vi"
File 24="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Send Message.vi"
File 25="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ Rep Test.vi"
File 26="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ Req Test.vi"
File 27="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.GetPrivateEvents.vi"
File 28="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.GetPublicEvents.vi"
File 29="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.receiveMessage.vi"
File 30="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.sendMessage.vi"
File 31="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.TestLauncher.PUB.vi"
File 32="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.TestLauncher.REP.vi"
File 33="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.TestLauncher.REQ.vi"
File 34="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/ZMQ.TestLauncher.SUB.vi"
File 35="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Typedefs/PrivateEvents--Cluster.ctl"
File 36="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Typedefs/PrivateEvents--ZMQ.sendMessage.ctl"
File 37="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Typedefs/PublicEvents--Cluster.ctl"
File 38="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Typedefs/PublicEvents--ZMQ.receiveMessage.ctl"
File 39="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Typedefs/ZMQ Config.ctl"
File 40="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/API/Config Socket.vi"
File 41="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Close Connection.vi"
File 42="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor - Loop.vi"
File 43="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Connection Monitor - Stop.vi"
File 44="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Find STM connection by ID.vi"
File 45="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Get Connections.vi"
File 46="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Handle Error.vi"
File 47="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/onCreate.vi"
File 48="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Open Client Connection.vi"
File 49="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_Client 1.vi"
File 50="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_Client 2.vi"
File 51="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_Client 3.vi"
File 52="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_STM_Client 1.vi"
File 53="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_STM_Client 2.vi"
File 54="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_STM_Client 3.vi"
File 55="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RC_STM_Server.vi"
File 56="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read listener ID.vi"
File 57="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read Message.vi"
File 58="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Read STM connection info.vi"
File 59="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RemoteControl.STM.lvclass"
File 60="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Send Message.vi"
File 61="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client.vi"
File 62="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Client_SM.vi"
File 63="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/STM_Server.vi"
File 64="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Write listener ID.vi"
File 65="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Write STM connection info.vi"
File 66="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Client - JKI SM or SMO.vi"
File 67="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Close Connection.vi"
File 68="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor - Loop.vi"
File 69="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Connection Monitor - Stop.vi"
File 70="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Client.vi"
File 71="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Create RC Server.vi"
File 72="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/CreatePrivateEvents.vi"
File 73="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/CreatePublicEvents.vi"
File 74="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/DestroyPrivateEvents.vi"
File 75="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/DestroyPublicEvents.vi"
File 76="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Get Connections.vi"
File 77="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Client Connection.vi"
File 78="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Context.vi"
File 79="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Open Server Connection.vi"
File 80="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Process.vi"
File 81="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read address.vi"
File 82="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Commands.vi"
File 83="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Message.vi"
File 84="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Read Port.vi"
File 85="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Remote Client.vi"
File 86="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.Configure.vi"
File 87="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.GetPrivateEvents.vi"
File 88="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.GetPublicEvents.vi"
File 89="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.lvclass"
File 90="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.SendMessageFromProcess.vi"
File 91="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.SendMessageToProcess.vi"
File 92="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.TestLauncher.ConnectionMonitor.vi"
File 93="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.TestLauncher.Server.vi"
File 94="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControlGlobal.vi"
File 95="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Send and Receive Message.vi"
File 96="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Send Message.vi"
File 97="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Time Message Events.vi"
File 98="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/VirtualTestInstrument.vi"
File 99="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write address.vi"
File 100="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Commands.vi"
File 101="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Debug Mode.vi"
File 102="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Write Port.vi"
File 103="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Message--Cluster.ctl"
File 104="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--Cluster.ctl"
File 105="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Configure.ctl"
File 106="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Reply Message.ctl"
File 107="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.SendMessageToProcess.ctl"
File 108="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--Cluster.ctl"
File 109="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.Reply Remote Message.ctl"
File 110="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.SendMessageFromProcess.ctl"
File 111="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/RC Process Type--Enum.ctl"
File 112="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Variant with Message ID--cluster.ctl"
File 113="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Create Logger.vi"
File 114="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/CreatePrivateEvents.vi"
File 115="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Destroy Logger.vi"
File 116="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/DestroyPrivateEvents.vi"
File 117="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Error Log Generator Example 1.vi"
File 118="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Log Error.vi"
File 119="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.GetPrivateEvents.vi"
File 120="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.LogError.vi"
File 121="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.lvclass"
File 122="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.TestLauncher.vi"
File 123="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Process.vi"
File 124="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Typedefs/PrivateEvents--Cluster.ctl"
File 125="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Typedefs/PrivateEvents--Logger.Error.Log Error.ctl"
File 126="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/CreatePrivateEvents.vi"
File 127="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/CreatePublicEvents.vi"
File 128="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/DestroyPrivateEvents.vi"
File 129="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/DestroyPublicEvents.vi"
File 130="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.GetPublicEvents.vi"
File 131="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.lvclass"
File 132="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.TestLauncher.vi"
File 133="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.DSC.WriteVariable.vi"
File 134="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.GetPrivateEvents.vi"
File 135="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Logger.ReadVariable.vi"
File 136="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Process.vi"
File 137="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Read from DSC (unused).vi"
File 138="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Write Cluster to DSC.vi"
File 139="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Write to DSC.vi"
File 140="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Cluster.ctl"
File 141="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Logger.DSC.Set Address.ctl"
File 142="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PrivateEvents--Logger.DSC.Write Variable.ctl"
File 143="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PublicEvents--Cluster.ctl"
File 144="user.lib/Levylab/Levylab Instruments/SMOs/Logger.DSC/Typedefs/PublicEvents--Logger.DSC.Read Variable.ctl"
File 145="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Create Logger.vi"
File 146="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Destroy Logger.vi"
File 147="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.lvclass"
File 148="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.TestLauncher.vi"
File 149="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Process.vi"
File 150="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Read Debug Mode.vi"
File 151="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Read path.vi"
File 152="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Write Debug Mode.vi"
File 153="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Write path.vi"
File 154="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/Handle Error.vi"
File 155="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/LevyLab.lvclass"
File 156="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/LevyLab.TestLauncher.vi"
File 157="user.lib/Levylab/Levylab Instruments/SMOs/LevyLab/Rename_Process.vi"
File 158="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Create UI.vi"
File 159="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Instrument UI.lvclass"
File 160="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Instrument UI.TestLauncher.vi"
File 161="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Process.vi"
File 162="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.lvclass"
File 163="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.TestLauncher.vi"
File 164="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Process.vi"
File 165="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Configuration--Cluster.ctl"
File 166="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/DSC Configuration--Cluster.ctl"
File 167="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/HW Configuration--Cluster.ctl"
File 168="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Instrument.Commands--Enum.ctl"
File 169="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Instrument.Instrument Types.ctl"
File 170="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Cluster.ctl"
File 171="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Instrument.MessageToProcess.ctl"
File 172="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Cluster.ctl"
File 173="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.MessageFromProcess.ctl"
File 174="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO Configuration--Cluster.ctl"
File 175="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO RC Type--enum.ctl"
File 176="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Read Configuration File.vi"
File 177="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Remote Client.vi"
File 178="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Write Configuration File.vi"
File 179="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Write Configuration Path.vi"
File 180="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Get Dependencies.vi"
File 181="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Command Enum to String.vi"
File 182="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.Configuration Window.vi"
File 183="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.GetPrivateEvents.vi"
File 184="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.MessageFromProcess.vi"
File 185="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/List Devices.vi"
File 186="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/CreatePrivateEvents.vi"
File 187="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/CreatePublicEvents.vi"
File 188="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/DestroyPrivateEvents.vi"
File 189="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/DestroyPublicEvents.vi"
File 190="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/enumerateStaticDependencies.vi"
File 191="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Close Instrument.vi"
File 192="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Configure Instrument.vi"
File 193="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Name.vi"
File 194="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Port.vi"
File 195="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Public API.vi"
File 196="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO RC Type.vi"
File 197="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/getAll.vi"
File 198="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Handle Command.vi"
File 199="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Open Instrument.vi"
File 200="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Close.vi"
File 201="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Create Instrument SMO.vi"
File 202="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/GET ALL.vi"
File 203="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/HELP.vi"
File 204="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.GetPublicEvents.vi"
File 205="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.MessageToProcess.vi"
File 206="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Open.vi"
File 207="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Configuration Class.vi"
File 208="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Debug Mode.vi"
File 209="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Hardware Address.vi"
File 210="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Configuration.lvclass"
File 211="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Read Configuration.vi"
File 212="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Configuration.vi"
File 213="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Path.vi"
File 214="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Get Bias Voltage.vi"
File 215="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Instrument.VSource.lvclass"
File 216="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Set Bias Voltage.vi"
File 217="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Get Data.vi"
File 218="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Instrument.VNA.lvclass"
File 219="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Average.vi"
File 220="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Format.vi"
File 221="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Measurement.vi"
File 222="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Power.vi"
File 223="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Sweep.vi"
File 224="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Conversion--enum.ctl"
File 225="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Format--enum.ctl"
File 226="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Measurement--enum.ctl"
File 227="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Sweep Type--enum.ctl"
File 228="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Get Strain.vi"
File 229="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Instrument.Strain.lvclass"
File 230="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Set Strain.vi"
File 231="user.lib/Levylab/Levylab Instruments/Instrument Types/Optical Delay Line/Get Delay.vi"
File 232="user.lib/Levylab/Levylab Instruments/Instrument Types/Optical Delay Line/Instrument.OpticalDelayLine.lvclass"
File 233="user.lib/Levylab/Levylab Instruments/Instrument Types/Optical Delay Line/Set Delay.vi"
File 234="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Angle.vi"
File 235="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Helium Level.vi"
File 236="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Magnet Field.vi"
File 237="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Nitrogen Level.vi"
File 238="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Pressure.vi"
File 239="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Temperature.vi"
File 240="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Instrument.Cryostat.lvclass"
File 241="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Angle.vi"
File 242="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Magnet Field.vi"
File 243="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Temperature.vi"
File 244="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Magnet Setpoint.vi"
File 245="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Temperature Setpoint.vi"
File 246="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Axis--Enum.ctl"
File 247="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Mode--Enum.ctl"
File 248="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Rotator Axis--Enum.ctl"
File 249="user.lib/Levylab/Levylab Instruments/Instrument Types/CBridge/Get Capacitance.vi"
File 250="user.lib/Levylab/Levylab Instruments/Instrument Types/CBridge/Instrument.CBridge.lvclass"
File 251="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument UI/LevyLab Instrument UI.lvclass"
File 252="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument UI/LevyLab Instrument UI.TestLauncher.vi"
File 253="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument UI/Process.vi"
File 254="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/LevyLab Instrument.AppLauncher.vi"
File 255="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/LevyLab Instrument.lvclass"
File 256="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Process.vi"
File 257="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Typedefs/LevyLab Instrument.Commands--Enum.ctl"
File 258="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Typedefs/LevyLab Instrument.Configuration--Cluster.ctl"
File 259="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Typedefs/LevyLab Instrument.getAll--Cluster.ctl"
File 260="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Protected/LevyLab Instrument.Client.vi"
File 261="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Command Enum to String.vi"
File 262="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Private/LevyLab Instrument.Configuration Window.vi"
File 263="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Configure Instrument.vi"
File 264="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO Name.vi"
File 265="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO Port.vi"
File 266="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO Public API.vi"
File 267="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Get SMO RC Type.vi"
File 268="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/getAll.vi"
File 269="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Handle Command.vi"
File 270="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Read Configuration File.vi"
File 271="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/Overrides/Write Configuration File.vi"
File 272="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/Close.vi"
File 273="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/LevyLab Instrument.getAll.vi"
File 274="templates/JKI/JKI SMO/LevyLab Instrument/LevyLab Instrument/API/Open.vi"
File 275="ProjectTemplates/Source/LevyLab/Instrument/LevyLab Instrument.lvproj"
File 276="ProjectTemplates/Source/LevyLab/Instrument/ProjectSetup.vi"
File 277="ProjectTemplates/Source/LevyLab/Instrument/project/.gitignore"
File 278="ProjectTemplates/Source/LevyLab/Instrument/project/LICENSE"
File 279="ProjectTemplates/Source/LevyLab/Instrument/project/README.md"
File 280="ProjectTemplates/Source/LevyLab/Instrument/project/build support/buildspec-template.vipt.rename"
File 281="ProjectTemplates/Source/LevyLab/Instrument/project/build support/icon.ico"
File 282="ProjectTemplates/Source/LevyLab/Instrument/project/build support/Post-Build Custom Action.vi"
File 283="ProjectTemplates/Source/LevyLab/images/instrument.png"
File 284="ProjectTemplates/MetaData/LevyLab_Instrument_MetaData.xml"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=25
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
File 16="_functions_levylab_lib_levylab_instruments_24.mnu"
File 17="_functions_levylab_lib_levylab_instruments_3.mnu"
File 18="_functions_levylab_lib_levylab_instruments_4.mnu"
File 19="_functions_levylab_lib_levylab_instruments_5.mnu"
File 20="_functions_levylab_lib_levylab_instruments_6.mnu"
File 21="_functions_levylab_lib_levylab_instruments_7.mnu"
File 22="_functions_levylab_lib_levylab_instruments_8.mnu"
File 23="_functions_levylab_lib_levylab_instruments_9.mnu"
File 24="functions_Levylab_lib_Levylab_Instruments.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

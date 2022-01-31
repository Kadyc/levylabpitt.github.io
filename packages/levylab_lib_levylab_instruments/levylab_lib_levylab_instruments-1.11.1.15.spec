[Package]
Name="levylab_lib_levylab_instruments"
Version="1.11.1.15"
Release=""
ID=6a6ec398d60bf5db645fd48a3ae74d53
File Format="vip"
Format Version="2017"
Display Name="Instrument Framework"


[Description]
Description="An object-oriented framework based on JKI SMOs, developed by the LevyLab at the University of Pittsburgh.\0D\0A\0D\0AAn Instrument developed using this framework will have the access to the following capabilities:\0D\0A\0D\0A- Framework for communicating with hardware (Hardware Abstraction Layer (HAL))\0D\0A- Periodically polls the instrument for its settings and logs them to a PGSQL database\0D\0A- Defines an API to allow external programs to control compiled instances of the application and remotely across a network (Either NI's Simple Messaging Library (STM) (deprecated in v1.9) or cross-platform protocol ZMQ (preferred beginning with v1.9))\0D\0A- Provide a user interface (optional but probably desirable).\0D\0A- Methods for reading and writing configuration from disk."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.11.1.15]\0D\0A- Updated to latest SMO (v1.4.0.69)\0A- Logger behavior changed (do not run process.vi unnecessarily)\0A- Logger.Error implements its own logging (remove MGI and hopefully zombie processes)\0A- Updated unit tests and misc. refactoring"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW x86>=19.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall="<OS User Documents>\\GitHub\\Instrument-Framework\\build support\\Post-Install Custom Action.vi"
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires="jdp_science_jsontext>=1.6.7.107,jdp_science_lib_common_utilities>=1.3.0.14,jdp_science_postgresql>=0.3.5.23,jki_lib_caraya>=1.2.1.131,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.2.112,lava_lib_ui_tools>=1.4.1.74,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_lvtoitx>=3.3.6.11,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,mgi_lib_user_interface>=1.0.1.11,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_seh>=2.1.10.1,ni_lib_stm>=3.1.0.9,nise_syslog>=1.3.3.27,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56,jki_lib_smo_editor>=2.0.2.5,levylab_lib_build_support>=1.2.2.13"
Conflicts="levylab_lib_postgresql>=1.4.0.22"


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
Num Files=315
File 0="user.lib/Levylab/Levylab Instruments/instrument.lvproj"
File 1="user.lib/Levylab/Levylab Instruments/SMOs/Shortcuts.vi"
File 2="user.lib/Levylab/Levylab Instruments/SMOs/showrunningvis.vi"
File 3="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Decode.vi"
File 4="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI Encode.vi"
File 5="user.lib/Levylab/Levylab Instruments/SMOs/SCPI/SCPI.lvclass"
File 6="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/RemoteControl.ZMQ.lvclass"
File 7="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Typedefs/ZMQ Config.ctl"
File 8="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Tests/ZMQ Rep Test.vi"
File 9="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Tests/ZMQ Req Test.vi"
File 10="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/private/Build Endpoint.vi"
File 11="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Methods (Overrides)/Close Connection.vi"
File 12="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Methods (Overrides)/Get Connections.vi"
File 13="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Methods (Overrides)/Open Client Connection.vi"
File 14="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Methods (Overrides)/Open Server Connection.vi"
File 15="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Methods (Overrides)/Read Message.vi"
File 16="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.ZMQ/Methods (Overrides)/Send Message.vi"
File 17="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/RemoteControl.STM.lvclass"
File 18="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Tests/RC_STM_Server.vi"
File 19="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Tests/Test Variant Flatten Unflatten.vi"
File 20="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Tests/simple/STM_Client.vi"
File 21="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Tests/simple/STM_Server.vi"
File 22="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Tests/simple/subVI/PRI Counts Since Last Reset.vi"
File 23="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Private/Choose Connection.vi"
File 24="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Private/Find STM connection by ID.vi"
File 25="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Close Connection.vi"
File 26="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Get Connections.vi"
File 27="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Handle Error.vi"
File 28="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Listen.vi"
File 29="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Open Client Connection.vi"
File 30="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Read Message.vi"
File 31="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Send Message.vi"
File 32="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Start Listener.vi"
File 33="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl.STM/Methods (Overrides)/Stop Listener.vi"
File 34="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Process.vi"
File 35="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/RemoteControl.lvclass"
File 36="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/Message--Cluster.ctl"
File 37="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--Cluster.ctl"
File 38="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.Configure.ctl"
File 39="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PrivateEvents--RemoteControl.SendMessageToProcess.ctl"
File 40="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--Cluster.ctl"
File 41="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/PublicEvents--RemoteControl.SendMessageFromProcess.ctl"
File 42="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/RC Com Type--enum.ctl"
File 43="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Typedefs/RC Process Type--Enum.ctl"
File 44="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Tests/Choose Random Command.vi"
File 45="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Tests/RC_Client Client 2.vi"
File 46="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Tests/RC_Client Client.vi"
File 47="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Tests/RC_Client N.vi"
File 48="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Tests/RC_Client.vi"
File 49="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Tests/RemoteControl.TestLauncher.ConnectionMonitor.vi"
File 50="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Private/RemoteControl.GetPrivateEvents.vi"
File 51="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Private/RemoteControl.SendMessageFromProcess.vi"
File 52="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Private/RemoteControlGlobal.vi"
File 53="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Private/Time Message Events.vi"
File 54="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Private/VirtualTestInstrument.vi"
File 55="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Overrides)/CreatePrivateEvents.vi"
File 56="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Overrides)/CreatePublicEvents.vi"
File 57="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Overrides)/DestroyPrivateEvents.vi"
File 58="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Overrides)/DestroyPublicEvents.vi"
File 59="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Close Connection.vi"
File 60="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Get Connections.vi"
File 61="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Listen.vi"
File 62="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Open Client Connection.vi"
File 63="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Open Server Connection.vi"
File 64="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Read Message.vi"
File 65="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Send and Receive Message.vi"
File 66="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Send Message.vi"
File 67="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Start Listener.vi"
File 68="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/Methods (Framework)/Stop Listener.vi"
File 69="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Connect.vi"
File 70="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Create Server SMO.vi"
File 71="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Disconnect.vi"
File 72="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/RC Enum to RC Object.vi"
File 73="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/RC Object to RC Enum.vi"
File 74="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Read address.vi"
File 75="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Read Commands.vi"
File 76="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Read Message (sent).vi"
File 77="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Read Port.vi"
File 78="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Read RC Process Type.vi"
File 79="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Read timeout.vi"
File 80="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Remote Client.vi"
File 81="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/RemoteControl.Configure.vi"
File 82="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/RemoteControl.GetPublicEvents.vi"
File 83="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/RemoteControl.SendMessageToProcess.vi"
File 84="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Send and Receive.vi"
File 85="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Variant to Data.vim"
File 86="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Write address.vi"
File 87="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Write Commands.vi"
File 88="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Write Debug Mode.vi"
File 89="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Write Message (sent).vi"
File 90="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Write Port.vi"
File 91="user.lib/Levylab/Levylab Instruments/SMOs/RemoteControl/API/Write Timeout.vi"
File 92="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/CreatePrivateEvents.vi"
File 93="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/CreatePublicEvents.vi"
File 94="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/DestroyPrivateEvents.vi"
File 95="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/DestroyPublicEvents.vi"
File 96="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Logger.GetPrivateEvents.vi"
File 97="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Logger.PGSQL.GetPublicEvents.vi"
File 98="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Logger.PGSQL.lvclass"
File 99="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Logger.PGSQL.TestLauncher.vi"
File 100="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Logger.PGSQL.WriteVariable.vi"
File 101="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Logger.ReadVariable.vi"
File 102="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Process.vi"
File 103="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Read from PGSQL (unused).vi"
File 104="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Shorten Cluster.vi"
File 105="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Write Cluster to PGSQL.vi"
File 106="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Write Or Not.vi"
File 107="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Write to PGSQL.vi"
File 108="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Typedefs/PrivateEvents--Cluster.ctl"
File 109="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Set Address.ctl"
File 110="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Write Variable.ctl"
File 111="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Typedefs/PublicEvents--Cluster.ctl"
File 112="user.lib/Levylab/Levylab Instruments/SMOs/Logger.PGSQL/Typedefs/PublicEvents--Logger.PGSQL.Read Variable.ctl"
File 113="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Create Logger.vi"
File 114="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Destroy Logger.vi"
File 115="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Error Cluster to Array.vi"
File 116="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Get SMO Name from Error Event.vi"
File 117="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.lvclass"
File 118="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Logger.Error.TestLauncher.vi"
File 119="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Process.vi"
File 120="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Read Class from Error.vi"
File 121="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Write Class to Error.vi"
File 122="user.lib/Levylab/Levylab Instruments/SMOs/Logger.Error/Write Dependencies.vi"
File 123="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Create Logger.vi"
File 124="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Destroy Logger.vi"
File 125="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.lvclass"
File 126="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Logger.TestLauncher.vi"
File 127="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Process_DoNotRun.vi"
File 128="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Read Debug Mode.vi"
File 129="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Read path.vi"
File 130="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Write Debug Mode.vi"
File 131="user.lib/Levylab/Levylab Instruments/SMOs/Logger/Write path.vi"
File 132="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC.lvproj"
File 133="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/tests/JSONtext-test-20210421.vi"
File 134="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/tests/TEST-JSON-RPC+caraya.vi"
File 135="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/tests/TEST-JSON-RPC--Cluster.ctl"
File 136="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/tests/TEST-JSON-RPC.vi"
File 137="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/JSON-RPC.lvclass"
File 138="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/typedefs/Error--Cluster.ctl"
File 139="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/typedefs/Request--Cluster.ctl"
File 140="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Create Error Object.vi"
File 141="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Create ID.vi"
File 142="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Create Request-JSONtext.vi"
File 143="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Create Response-JSONtext.vi"
File 144="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Parse Params-JSONtext.vi"
File 145="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Parse Request-JSONtext.vi"
File 146="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Parse Response-JSONtext.vi"
File 147="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Read ids.vi"
File 148="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/private/Write ids.vi"
File 149="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/API/Create Request.vi"
File 150="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/API/Create Response.vi"
File 151="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/API/JSON-RPC Errors.vi"
File 152="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/API/Parse Params.vi"
File 153="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/API/Parse Request.vi"
File 154="user.lib/Levylab/Levylab Instruments/SMOs/JSON-RPC/JSON-RPC/API/Parse Response.vi"
File 155="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Create UI.vi"
File 156="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Instrument UI.lvclass"
File 157="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Instrument UI.TestLauncher.vi"
File 158="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Process.vi"
File 159="user.lib/Levylab/Levylab Instruments/SMOs/Instrument UI/Read Instrument.vi"
File 160="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.lvclass"
File 161="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Instrument.TestLauncher.vi"
File 162="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Process.vi"
File 163="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Test Decode JSON.vi"
File 164="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Configuration--Cluster.ctl"
File 165="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Dependencies--Cluster.ctl"
File 166="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/HW Configuration--Cluster.ctl"
File 167="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Instrument.Commands--Enum.ctl"
File 168="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/Instrument.Instrument Types.ctl"
File 169="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Cluster.ctl"
File 170="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Instrument.Log PGSQL.ctl"
File 171="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PrivateEvents--Instrument.MessageToProcess.ctl"
File 172="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Cluster.ctl"
File 173="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/PublicEvents--Instrument.MessageFromProcess.ctl"
File 174="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Typedefs/SMO Configuration--Cluster.ctl"
File 175="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Protected/Write Configuration Path.vi"
File 176="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Get Dependencies.vi"
File 177="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.GetPrivateEvents.vi"
File 178="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Private/Instrument.MessageFromProcess.vi"
File 179="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/CreatePrivateEvents.vi"
File 180="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/CreatePublicEvents.vi"
File 181="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/DestroyPrivateEvents.vi"
File 182="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/DestroyPublicEvents.vi"
File 183="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Overrides/enumerateStaticDependencies.vi"
File 184="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Close Hardware.vi"
File 185="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Close Instrument.vi"
File 186="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Close SMO.vi"
File 187="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Configuration Window.vi"
File 188="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Address.vi"
File 189="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Name.vi"
File 190="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO PGSQL Log Paths.vi"
File 191="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Port.vi"
File 192="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO Public API.vi"
File 193="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Get SMO RC Type.vi"
File 194="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Handle Command.vi"
File 195="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Handle getAll.vi"
File 196="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Handle setConfiguration.vi"
File 197="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Open Hardware.vi"
File 198="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Open Instrument.vi"
File 199="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Open SMO.vi"
File 200="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Read Configuration File.vi"
File 201="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/Framework (for override)/Write Configuration File.vi"
File 202="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/ACK.vi"
File 203="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Close.vi"
File 204="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Create Instrument SMO.vi"
File 205="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Enum to String.vi"
File 206="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/GET ALL.vim"
File 207="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/HELP.vi"
File 208="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.GetPublicEvents.vi"
File 209="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.LogPGSQL.vi"
File 210="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Instrument.MessageToProcess.vi"
File 211="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Open.vi"
File 212="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Configuration Class.vi"
File 213="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Debug Mode.vi"
File 214="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Read Hardware Address.vi"
File 215="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Remote Client.vim"
File 216="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Send and Receive.vi"
File 217="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/SET CONFIG.vim"
File 218="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/State History.vi"
File 219="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Variant to LV Data.vim"
File 220="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Write Hardware Address.vi"
File 221="user.lib/Levylab/Levylab Instruments/SMOs/Instrument/API/Write RC Type.vi"
File 222="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Configuration.lvclass"
File 223="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Default Path.vi"
File 224="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Handle Missing Sections.vi"
File 225="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Read Configuration (Template).vi"
File 226="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Read Configuration.vi"
File 227="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Read Path.vi"
File 228="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Configuration.vi"
File 229="user.lib/Levylab/Levylab Instruments/SMOs/Configuration/Write Path.vi"
File 230="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Get Bias Voltage.vi"
File 231="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Instrument.VSource.lvclass"
File 232="user.lib/Levylab/Levylab Instruments/Instrument Types/VSource/Set Bias Voltage.vi"
File 233="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Get Data.vi"
File 234="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Instrument.VNA.lvclass"
File 235="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Average.vi"
File 236="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Format.vi"
File 237="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Measurement.vi"
File 238="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Power.vi"
File 239="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Set Sweep.vi"
File 240="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Conversion--enum.ctl"
File 241="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Format--enum.ctl"
File 242="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Measurement--enum.ctl"
File 243="user.lib/Levylab/Levylab Instruments/Instrument Types/VNA/Typedefs/Sweep Type--enum.ctl"
File 244="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Get Strain.vi"
File 245="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Instrument.Strain.lvclass"
File 246="user.lib/Levylab/Levylab Instruments/Instrument Types/Strain/Set Strain.vi"
File 247="user.lib/Levylab/Levylab Instruments/Instrument Types/Lockin/Instrument.Lockin.lvclass"
File 248="user.lib/Levylab/Levylab Instruments/Instrument Types/Delay Line/Get Delay.vi"
File 249="user.lib/Levylab/Levylab Instruments/Instrument Types/Delay Line/Instrument.DelayLine.lvclass"
File 250="user.lib/Levylab/Levylab Instruments/Instrument Types/Delay Line/Set Delay.vi"
File 251="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Cryostat JSON.vi"
File 252="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Angle.vi"
File 253="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Chamber.vi"
File 254="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Helium Level.vi"
File 255="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Magnet.vi"
File 256="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Nitrogen Level.vi"
File 257="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Pressure.vi"
File 258="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Get Temperature.vi"
File 259="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Instrument.Cryostat.lvclass"
File 260="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Angle.vi"
File 261="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Chamber.vi"
File 262="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Magnet.vi"
File 263="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Set Temperature.vi"
File 264="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Magnet Setpoint.vi"
File 265="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Wait for Temperature Setpoint.vi"
File 266="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Axis--Enum.ctl"
File 267="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Magnet Mode--Enum.ctl"
File 268="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Rotator Axis--Enum.ctl"
File 269="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Set Angle--cluster.ctl"
File 270="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Set Chamber--cluster.ctl"
File 271="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Set Magnet--cluster.ctl"
File 272="user.lib/Levylab/Levylab Instruments/Instrument Types/Cryostat/Typedefs/Set Temperature--cluster.ctl"
File 273="user.lib/Levylab/Levylab Instruments/Instrument Types/CBridge/Get Capacitance.vi"
File 274="user.lib/Levylab/Levylab Instruments/Instrument Types/CBridge/Instrument.CBridge.lvclass"
File 275="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Documentation.vi"
File 276="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Instrument.Template.AppLauncher.vi"
File 277="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Instrument.Template.lvclass"
File 278="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Process.vi"
File 279="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Typedefs/Instrument.Template.Commands--Enum.ctl"
File 280="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Typedefs/Instrument.Template.Configuration--Cluster.ctl"
File 281="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Typedefs/Instrument.Template.getAll--Cluster.ctl"
File 282="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Private/Configuration Window.vi"
File 283="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Close Hardware.vi"
File 284="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Get SMO Address.vi"
File 285="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Get SMO Name.vi"
File 286="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Get SMO PGSQL Log Paths.vi"
File 287="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Get SMO Port.vi"
File 288="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Get SMO Public API.vi"
File 289="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Get SMO RC Type.vi"
File 290="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Handle Command.vi"
File 291="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Handle getAll.vi"
File 292="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Handle setConfiguration.vi"
File 293="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Open Hardware.vi"
File 294="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Read Configuration File.vi"
File 295="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/Overrides/Write Configuration File.vi"
File 296="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/API/Close.vi"
File 297="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/API/Open.vi"
File 298="templates/JKI/JKI SMO/Instrument Framework/Instrument.Template/API/Set Bias Voltage.vi"
File 299="templates/JKI/JKI SMO/Instrument Framework/Instrument UI.Template/Instrument UI.Template.lvclass"
File 300="templates/JKI/JKI SMO/Instrument Framework/Instrument UI.Template/Instrument UI.Template.TestLauncher.vi"
File 301="templates/JKI/JKI SMO/Instrument Framework/Instrument UI.Template/Instrument UI.Template.UI--Cluster.ctl"
File 302="templates/JKI/JKI SMO/Instrument Framework/Instrument UI.Template/Process.vi"
File 303="ProjectTemplates/Source/LevyLab/Instrument/Instrument-Template.lvproj"
File 304="ProjectTemplates/Source/LevyLab/Instrument/scripting/MetaDataObj.Instrument.lvclass"
File 305="ProjectTemplates/Source/LevyLab/Instrument/scripting/PostCopyScripting.vi"
File 306="ProjectTemplates/Source/LevyLab/Instrument/project files/.gitattributes"
File 307="ProjectTemplates/Source/LevyLab/Instrument/project files/.gitignore"
File 308="ProjectTemplates/Source/LevyLab/Instrument/project files/LICENSE"
File 309="ProjectTemplates/Source/LevyLab/Instrument/project files/README.md"
File 310="ProjectTemplates/Source/LevyLab/Instrument/project files/build support/buildspec-template.vipt.rename"
File 311="ProjectTemplates/Source/LevyLab/Instrument/project files/build support/icon.ico"
File 312="ProjectTemplates/Source/LevyLab/Instrument/project files/build support/Post-Build Custom Action.vi"
File 313="ProjectTemplates/Source/LevyLab/Instrument/images/instrument.png"
File 314="ProjectTemplates/MetaData/LevyLab_Instrument_MetaData.xml"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=39
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
File 17="_functions_levylab_lib_levylab_instruments_25.mnu"
File 18="_functions_levylab_lib_levylab_instruments_26.mnu"
File 19="_functions_levylab_lib_levylab_instruments_27.mnu"
File 20="_functions_levylab_lib_levylab_instruments_28.mnu"
File 21="_functions_levylab_lib_levylab_instruments_29.mnu"
File 22="_functions_levylab_lib_levylab_instruments_3.mnu"
File 23="_functions_levylab_lib_levylab_instruments_30.mnu"
File 24="_functions_levylab_lib_levylab_instruments_31.mnu"
File 25="_functions_levylab_lib_levylab_instruments_32.mnu"
File 26="_functions_levylab_lib_levylab_instruments_33.mnu"
File 27="_functions_levylab_lib_levylab_instruments_34.mnu"
File 28="_functions_levylab_lib_levylab_instruments_35.mnu"
File 29="_functions_levylab_lib_levylab_instruments_36.mnu"
File 30="_functions_levylab_lib_levylab_instruments_37.mnu"
File 31="_functions_levylab_lib_levylab_instruments_38.mnu"
File 32="_functions_levylab_lib_levylab_instruments_4.mnu"
File 33="_functions_levylab_lib_levylab_instruments_5.mnu"
File 34="_functions_levylab_lib_levylab_instruments_6.mnu"
File 35="_functions_levylab_lib_levylab_instruments_7.mnu"
File 36="_functions_levylab_lib_levylab_instruments_8.mnu"
File 37="_functions_levylab_lib_levylab_instruments_9.mnu"
File 38="functions_Levylab_lib_Levylab_Instruments.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

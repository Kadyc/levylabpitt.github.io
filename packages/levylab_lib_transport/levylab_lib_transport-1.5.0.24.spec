[Package]
Name="levylab_lib_transport"
Version="1.5.0.24"
Release=""
ID=62177fd28fdb7bc5a688efb0cb89efac
File Format="vip"
Format Version="2017"
Display Name="Transport"


[Description]
Description="VIs for scripting and performing transport measurments.\0A\0A[Control Experiment.lvclass]\0AControl Experiment.vi provides a uniform way to record information about your sample & device, how the lockin is connected to the device, configures the Krohn Hite amplifier (and Pickering switch if you have one), and sets the base path for saving data.\0A\0A[Transport.lvclass]\0ABasic transport measurments.\0A- Lockin vs Vsg (or Vbg) (Lockin_Vsg.vi)\0A- Lockin vs Time (Lockin_time.vi)\0A- Lockin Sweep Mode (Lockin_sweep.vi (under development)\0A- IV curves (IV.vi)\0A\0A[SweepControl.lvclass]\0ASweep Control.vi: Sequencer for stepping multiple parameters. Calls VIs in Transport.lvclass\0AContinuous B sweep.vi: For sweeping B continuously while asynchronously calling VIs in Transport.lvclass"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.5.0]\0A- Update to LV2019, Instrument Framework v1.10.3, LV-Data\0A- Extensive refactoring of class wires into better-defined hierarchy"
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
Requires="i3_external_encryption>=1.0.0.8,jdp_science_jsontext>=1.6.5.105,jdp_science_lib_common_utilities>=1.3.0.14,jdp_science_postgresql>=0.3.5.23,jki_lib_json_serialization>=1.1.10.37,jki_lib_rest_client>=1.3.3.25,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.4.0.63,labview-zmq>=3.6.1.111,lava_lib_ui_tools>=1.4.1.74,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_krohn_hite_7008>=1.7.2.31,levylab_lib_lockin_multichannel>=2.14.6.71,levylab_lib_lvtoitx>=3.2.0.3,levylab_lib_plym>=1.0.1.3,levylab_lib_voltage_update>=1.0.3.5,levylab_lib_xy_utilities>=1.4.0.17,lvh_toolbox>=2.0.0.35,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_cloud_toolkit_for_aws>=1.1.0.1,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=144
File 0="user.lib/Levylab/Transport/Open Me.vi"
File 1="user.lib/Levylab/Transport/transport.lvproj"
File 2="user.lib/Levylab/Transport/Transport/IV.vi"
File 3="user.lib/Levylab/Transport/Transport/Lockin.vi"
File 4="user.lib/Levylab/Transport/Transport/Lockin_AIWFM_time.vi"
File 5="user.lib/Levylab/Transport/Transport/Lockin_sweep.vi"
File 6="user.lib/Levylab/Transport/Transport/Lockin_time.vi"
File 7="user.lib/Levylab/Transport/Transport/Lockin_Vsg.vi"
File 8="user.lib/Levylab/Transport/Transport/Sweep_AIWFM_time.vi"
File 9="user.lib/Levylab/Transport/Transport/THz_TimeDelay.vi"
File 10="user.lib/Levylab/Transport/Transport/Transport.lvclass"
File 11="user.lib/Levylab/Transport/Transport/Typedefs/Dependencies--Cluster.ctl"
File 12="user.lib/Levylab/Transport/Transport/Typedefs/Lockin_Sweep JSON--Cluster.ctl"
File 13="user.lib/Levylab/Transport/Transport/Typedefs/Lockin_Vsg JSON--Cluster.ctl"
File 14="user.lib/Levylab/Transport/Transport/subVI/Add Braces Array.vi"
File 15="user.lib/Levylab/Transport/Transport/subVI/Add Braces String.vi"
File 16="user.lib/Levylab/Transport/Transport/subVI/Add Braces.vi"
File 17="user.lib/Levylab/Transport/Transport/subVI/Array to Cluster.vi"
File 18="user.lib/Levylab/Transport/Transport/subVI/Calculate R and G - Four Terminal.vi"
File 19="user.lib/Levylab/Transport/Transport/subVI/Calculate R and G - Two Terminal.vi"
File 20="user.lib/Levylab/Transport/Transport/subVI/Create Keys (AI).vi"
File 21="user.lib/Levylab/Transport/Transport/subVI/Create Keys (AO).vi"
File 22="user.lib/Levylab/Transport/Transport/subVI/Decimate and Filter.vi"
File 23="user.lib/Levylab/Transport/Transport/subVI/Exec State to Append.vi"
File 24="user.lib/Levylab/Transport/Transport/subVI/GraphLockin_vs_Parameter.vi"
File 25="user.lib/Levylab/Transport/Transport/subVI/Max_Min_gate_conversion.vi"
File 26="user.lib/Levylab/Transport/Transport/subVI/Results (2D) to X and Y Arrays.vi"
File 27="user.lib/Levylab/Transport/Transport/subVI/Results (Dictionary) to X and Y Arrays.vi"
File 28="user.lib/Levylab/Transport/Transport/subVI/String Label.vi"
File 29="user.lib/Levylab/Transport/Transport/subVI/Waveform to Cluster.vi"
File 30="user.lib/Levylab/Transport/Transport/API (file)/Read Lockin_Sweep.json.vi"
File 31="user.lib/Levylab/Transport/Transport/API (file)/Read Lockin_Vsg.json.vi"
File 32="user.lib/Levylab/Transport/Transport/API (class)/Read Dependencies.vi"
File 33="user.lib/Levylab/Transport/Transport/API (class)/Write Dependencies.vi"
File 34="user.lib/Levylab/Transport/Transport/API (class)/Write notifier.vi"
File 35="user.lib/Levylab/Transport/SweepControl/Continuous B sweep.vi"
File 36="user.lib/Levylab/Transport/SweepControl/Process.vi"
File 37="user.lib/Levylab/Transport/SweepControl/Sweep Control Cartesian.vi"
File 38="user.lib/Levylab/Transport/SweepControl/Sweep Control.vi"
File 39="user.lib/Levylab/Transport/SweepControl/SweepControl.lvclass"
File 40="user.lib/Levylab/Transport/SweepControl/SweepControl.TestLauncher.vi"
File 41="user.lib/Levylab/Transport/SweepControl/Typedefs/Cluster - ScanControl.ctl"
File 42="user.lib/Levylab/Transport/SweepControl/Typedefs/Cluster - ScanParamters.ctl"
File 43="user.lib/Levylab/Transport/SweepControl/Typedefs/Cluster - Sweep Control.ctl"
File 44="user.lib/Levylab/Transport/SweepControl/Typedefs/Continuous B Sweep JSON--Cluster.ctl"
File 45="user.lib/Levylab/Transport/SweepControl/Typedefs/Dependencies--Cluster.ctl"
File 46="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - Action.ctl"
File 47="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - Experiments.ctl"
File 48="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - PostAction - 2.ctl"
File 49="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - PostAction.ctl"
File 50="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - Priority.ctl"
File 51="user.lib/Levylab/Transport/SweepControl/Typedefs/Lockin Sweep--Cluster.ctl"
File 52="user.lib/Levylab/Transport/SweepControl/Typedefs/PostAction.ctl"
File 53="user.lib/Levylab/Transport/SweepControl/Typedefs/ScanControl.ctl"
File 54="user.lib/Levylab/Transport/SweepControl/Typedefs/ScanParamters.ctl"
File 55="user.lib/Levylab/Transport/SweepControl/Typedefs/Sweep Control JSON--Cluster.ctl"
File 56="user.lib/Levylab/Transport/SweepControl/Typedefs/XP Style VISA Control.ctl"
File 57="user.lib/Levylab/Transport/SweepControl/subVIs/AppendDBLtoComments.vi"
File 58="user.lib/Levylab/Transport/SweepControl/subVIs/Create Scan.vi"
File 59="user.lib/Levylab/Transport/SweepControl/subVIs/D-Lockin.vi"
File 60="user.lib/Levylab/Transport/SweepControl/subVIs/Post action.vi"
File 61="user.lib/Levylab/Transport/SweepControl/subVIs/Scan action.vi"
File 62="user.lib/Levylab/Transport/SweepControl/subVIs/Sort Scan Parameters.vi"
File 63="user.lib/Levylab/Transport/SweepControl/subVIs/Sweep Control Inner Loop.vi"
File 64="user.lib/Levylab/Transport/SweepControl/subVIs/Sweep Control Loop.vi"
File 65="user.lib/Levylab/Transport/SweepControl/API (file)/Read Continuous B Sweep.json.vi"
File 66="user.lib/Levylab/Transport/SweepControl/API (file)/Read Sweep Control.json.vi"
File 67="user.lib/Levylab/Transport/SweepControl/API/Read Dependencies.vi"
File 68="user.lib/Levylab/Transport/SweepControl/API/Read Parameter (Now).vi"
File 69="user.lib/Levylab/Transport/SweepControl/API/Read Sorted scan parameters.vi"
File 70="user.lib/Levylab/Transport/SweepControl/API/Read Sweep Configuration Example.vi"
File 71="user.lib/Levylab/Transport/SweepControl/API/Read Sweep Configuration File.vi"
File 72="user.lib/Levylab/Transport/SweepControl/API/Take Measurement.vi"
File 73="user.lib/Levylab/Transport/SweepControl/API/Write Dependencies.vi"
File 74="user.lib/Levylab/Transport/Control Experiment/Configuration.ini"
File 75="user.lib/Levylab/Transport/Control Experiment/Control Experiment.lvclass"
File 76="user.lib/Levylab/Transport/Control Experiment/Control Experiment.vi"
File 77="user.lib/Levylab/Transport/Control Experiment/Tree.vi"
File 78="user.lib/Levylab/Transport/Control Experiment/Typedefs/Control Experiment JSON--cluster.ctl"
File 79="user.lib/Levylab/Transport/Control Experiment/Typedefs/Experiment Description--cluster.ctl"
File 80="user.lib/Levylab/Transport/Control Experiment/Typedefs/Instrument--enum.ctl"
File 81="user.lib/Levylab/Transport/Control Experiment/Typedefs/Instruments--cluster.ctl"
File 82="user.lib/Levylab/Transport/Control Experiment/Typedefs/KH Mode-enum.ctl"
File 83="user.lib/Levylab/Transport/Control Experiment/Typedefs/UI Controls --cluster.ctl"
File 84="user.lib/Levylab/Transport/Control Experiment/Typedefs/Wiring Description--cluster.ctl"
File 85="user.lib/Levylab/Transport/Control Experiment/Tests/Test Upload to S3.vi"
File 86="user.lib/Levylab/Transport/Control Experiment/Tests/Test Write.vi"
File 87="user.lib/Levylab/Transport/Control Experiment/subVIs/Compare With Previous.vi"
File 88="user.lib/Levylab/Transport/Control Experiment/subVIs/DBL Variant or Array Variant to Array.vi"
File 89="user.lib/Levylab/Transport/Control Experiment/subVIs/Device and User DSC Paths.vi"
File 90="user.lib/Levylab/Transport/Control Experiment/subVIs/Device and User PGSQL Paths.vi"
File 91="user.lib/Levylab/Transport/Control Experiment/subVIs/ElectrodesLabelsToPickeringChannels.vi"
File 92="user.lib/Levylab/Transport/Control Experiment/subVIs/Find File.vi"
File 93="user.lib/Levylab/Transport/Control Experiment/subVIs/Get Computer Name.vi"
File 94="user.lib/Levylab/Transport/Control Experiment/subVIs/Get Date Time For Filename.vi"
File 95="user.lib/Levylab/Transport/Control Experiment/subVIs/Get Date Time ISO.vi"
File 96="user.lib/Levylab/Transport/Control Experiment/subVIs/Initialize KH Array.vi"
File 97="user.lib/Levylab/Transport/Control Experiment/subVIs/Letter to Number.vi"
File 98="user.lib/Levylab/Transport/Control Experiment/subVIs/Load Instrument Classes.vi"
File 99="user.lib/Levylab/Transport/Control Experiment/subVIs/Multiply Gains.vi"
File 100="user.lib/Levylab/Transport/Control Experiment/subVIs/Number to Letter.vi"
File 101="user.lib/Levylab/Transport/Control Experiment/subVIs/Open Experiment VI.vi"
File 102="user.lib/Levylab/Transport/Control Experiment/subVIs/Open Lockin.vi"
File 103="user.lib/Levylab/Transport/Control Experiment/subVIs/Reset Counter.vi"
File 104="user.lib/Levylab/Transport/Control Experiment/subVIs/Asana/Asana Dictionary Get Value.vi"
File 105="user.lib/Levylab/Transport/Control Experiment/subVIs/Asana/Asana Dictionary Tasks Get Value.vi"
File 106="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Device Description.vi"
File 107="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Experiment Description.vi"
File 108="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Lockin Description.vi"
File 109="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Sweep Description.vi"
File 110="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Wiring Description.vi"
File 111="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Create Lockin AO Description.vi"
File 112="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Create Lockin REF Description.vi"
File 113="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Create Lockin Sampling Description.vi"
File 114="user.lib/Levylab/Transport/Control Experiment/Comments/Generate Comments.vi"
File 115="user.lib/Levylab/Transport/Control Experiment/API (File)/Control Experiment FGV.vi"
File 116="user.lib/Levylab/Transport/Control Experiment/API (File)/Control Experiment.xml"
File 117="user.lib/Levylab/Transport/Control Experiment/API (File)/Create Transport DAT File.vi"
File 118="user.lib/Levylab/Transport/Control Experiment/API (File)/Save JSON File.vi"
File 119="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport DAT File 2D.vi"
File 120="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport DAT File.vi"
File 121="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport ITX File.vi"
File 122="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport TDMS File.vi"
File 123="user.lib/Levylab/Transport/Control Experiment/API/Erase Comments.vi"
File 124="user.lib/Levylab/Transport/Control Experiment/API/Get Channel Indices.vi"
File 125="user.lib/Levylab/Transport/Control Experiment/API/Read Comments.vi"
File 126="user.lib/Levylab/Transport/Control Experiment/API/Read Device.vi"
File 127="user.lib/Levylab/Transport/Control Experiment/API/Read Experiment Configuration.vi"
File 128="user.lib/Levylab/Transport/Control Experiment/API/Read Experiment Description.vi"
File 129="user.lib/Levylab/Transport/Control Experiment/API/Read Experiment Path.vi"
File 130="user.lib/Levylab/Transport/Control Experiment/API/Read Instruments.vi"
File 131="user.lib/Levylab/Transport/Control Experiment/API/Read Wiring Configuration.vi"
File 132="user.lib/Levylab/Transport/Control Experiment/API/Write Experiment Description.vi"
File 133="user.lib/Levylab/Transport/Control Experiment/API/Write Experiment Folder.vi"
File 134="user.lib/Levylab/Transport/Control Experiment/API/Write Instruments.vi"
File 135="user.lib/Levylab/Transport/Control Experiment/API/Write Sweep Element.vi"
File 136="user.lib/Levylab/Transport/Control Experiment/API/S3/Handle S3 Error.vi"
File 137="user.lib/Levylab/Transport/Control Experiment/API/S3/S3 Backup--cluster.ctl"
File 138="user.lib/Levylab/Transport/Control Experiment/API/S3/Upload to S3.vi"
File 139="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Append Dictionary Element.vi"
File 140="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Close Dictionary.vi"
File 141="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Read All Dictionary Elements.vi"
File 142="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Write Dictionary Element.vi"
File 143="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Write Dictionary Elements (Loop).vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=18
File 0="_functions_levylab_lib_transport_1.mnu"
File 1="_functions_levylab_lib_transport_10.mnu"
File 2="_functions_levylab_lib_transport_11.mnu"
File 3="_functions_levylab_lib_transport_12.mnu"
File 4="_functions_levylab_lib_transport_13.mnu"
File 5="_functions_levylab_lib_transport_14.mnu"
File 6="_functions_levylab_lib_transport_15.mnu"
File 7="_functions_levylab_lib_transport_16.mnu"
File 8="_functions_levylab_lib_transport_17.mnu"
File 9="_functions_levylab_lib_transport_2.mnu"
File 10="_functions_levylab_lib_transport_3.mnu"
File 11="_functions_levylab_lib_transport_4.mnu"
File 12="_functions_levylab_lib_transport_5.mnu"
File 13="_functions_levylab_lib_transport_6.mnu"
File 14="_functions_levylab_lib_transport_7.mnu"
File 15="_functions_levylab_lib_transport_8.mnu"
File 16="_functions_levylab_lib_transport_9.mnu"
File 17="functions_Levylab_lib_Transport.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

[Package]
Name="levylab_lib_transport"
Version="1.3.0.7"
Release=""
ID=b25899cc8763c8fd1192bf62c942bcc8
File Format="vip"
Format Version="2017"
Display Name="Transport"


[Description]
Description="VIs for scripting and performing transport measurments.\0A\0A[Control Experiment.lvclass]\0AControl Experiment.vi provides a uniform way to record information about your sample & device, how the lockin is connected to the device, configures the Krohn Hite amplifier (and Pickering switch if you have one), and sets the base path for saving data.\0A\0A[SweepControl.lvclass]\0ASweep Control.vi: Sequencer for stepping multiple parameters. Calls VIs in Transport.lvclass\0AContinuous B sweep.vi: For sweeping B continuously while asynchronously calling VIs in Transport.lvclass\0A\0A[Transport.lvclass]\0ABasic transport measurments.\0A- Lockin vs Vsg (or Vbg) (Lockin_Vsg.vi)\0A- Lockin vs Time (Lockin_time.vi)\0A- Lockin Sweep Mode (Lockin_sweep.vi (under development)\0A- IV curves (IV.vi)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.3.0.7]\0A- Device and User strings are written to DSC processes (configured for PPMS1, PPMS2, MNK, DR200, THz1, MFP3D, Cypher) by Control Experiment.vi\0A- Cryostat class is configured for:\0A-- PPMS1 (Magnet, Temperature)\0A-- PPMS2 (Magnet, Temperature, Rotator)\0A-- MNK (Magnet, Temperature)\0A-- DR200 (Magnet)\0A-- THz1 (Temperature)\0A- Transport and Sweep Control VIs save TDMS files by default\0A-- Use dictionaries to store intermediate values of parameters before saving"
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
Requires="jki_lib_json_serialization>=1.1.10.37,jki_lib_rest_client>=1.3.2.21,jki_statemachineobjects>=1.3.0.56,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.3.9,levylab_lib_graph_utilities>=2.0.0.1,levylab_lib_krohn_hite_7008>=1.4.9.26,levylab_lib_leiden_tools>=1.2.2.16,levylab_lib_lockin_multichannel>=2.9.2.4,levylab_lib_lvtoitx>=2.7.3.7,levylab_lib_voltage_update>=1.0.3.5,lvh_toolbox>=2.0.0.35,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_file>=1.1.0.4,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,levylab_lib_asana_api>=1.4.1.2"
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
Num Files=123
File 0="user.lib/Levylab/Transport/transport.lvproj"
File 1="user.lib/Levylab/Transport/Variant to DBL or DBL Array.vi"
File 2="user.lib/Levylab/Transport/Transport/IV.vi"
File 3="user.lib/Levylab/Transport/Transport/IV_Fast.vi"
File 4="user.lib/Levylab/Transport/Transport/IV_Sweep.vi"
File 5="user.lib/Levylab/Transport/Transport/Lockin_AIWFM_time.vi"
File 6="user.lib/Levylab/Transport/Transport/Lockin_Sweep.vi"
File 7="user.lib/Levylab/Transport/Transport/Lockin_Time.vi"
File 8="user.lib/Levylab/Transport/Transport/Lockin_Vsg.vi"
File 9="user.lib/Levylab/Transport/Transport/Read Dependencies.vi"
File 10="user.lib/Levylab/Transport/Transport/Transport.lvclass"
File 11="user.lib/Levylab/Transport/Transport/Write Dependencies.vi"
File 12="user.lib/Levylab/Transport/Transport/Write notifier.vi"
File 13="user.lib/Levylab/Transport/Transport/Typedefs/Dependencies--Cluster.ctl"
File 14="user.lib/Levylab/Transport/Transport/Typedefs/Lockin_Sweep Configuration--Cluster.ctl"
File 15="user.lib/Levylab/Transport/Transport/Typedefs/Lockin_Vsg Configuration--Cluster.ctl"
File 16="user.lib/Levylab/Transport/Transport/subVI/Add Braces Array.vi"
File 17="user.lib/Levylab/Transport/Transport/subVI/Add Braces String.vi"
File 18="user.lib/Levylab/Transport/Transport/subVI/Add Braces.vi"
File 19="user.lib/Levylab/Transport/Transport/subVI/Append XY Arrays.vi"
File 20="user.lib/Levylab/Transport/Transport/subVI/Calculate R and G - Four Terminal.vi"
File 21="user.lib/Levylab/Transport/Transport/subVI/Calculate R and G - Two Terminal.vi"
File 22="user.lib/Levylab/Transport/Transport/subVI/Control Experiment FGV-cluster.ctl"
File 23="user.lib/Levylab/Transport/Transport/subVI/Decimate and Filter.vi"
File 24="user.lib/Levylab/Transport/Transport/subVI/GraphLockin_vs_Parameter.vi"
File 25="user.lib/Levylab/Transport/Transport/subVI/Resample XY Array.vi"
File 26="user.lib/Levylab/Transport/Transport/subVI/Waveforms To XY.vi"
File 27="user.lib/Levylab/Transport/Transport/API (file)/Read Lockin_Sweep.json.vi"
File 28="user.lib/Levylab/Transport/Transport/API (file)/Read Lockin_Vsg.json.vi"
File 29="user.lib/Levylab/Transport/SweepControl/Continuous B Sweep.vi"
File 30="user.lib/Levylab/Transport/SweepControl/Process.vi"
File 31="user.lib/Levylab/Transport/SweepControl/Sweep Control.vi"
File 32="user.lib/Levylab/Transport/SweepControl/SweepControl.lvclass"
File 33="user.lib/Levylab/Transport/SweepControl/SweepControl.TestLauncher.vi"
File 34="user.lib/Levylab/Transport/SweepControl/Typedefs/Cluster - ScanControl.ctl"
File 35="user.lib/Levylab/Transport/SweepControl/Typedefs/Cluster - ScanParamters.ctl"
File 36="user.lib/Levylab/Transport/SweepControl/Typedefs/Cluster - Sweep Control.ctl"
File 37="user.lib/Levylab/Transport/SweepControl/Typedefs/Continuous B Sweep Configuration--Cluster.ctl"
File 38="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - Action.ctl"
File 39="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - Experiments.ctl"
File 40="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - PostAction - 2.ctl"
File 41="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - PostAction.ctl"
File 42="user.lib/Levylab/Transport/SweepControl/Typedefs/Enum - Priority.ctl"
File 43="user.lib/Levylab/Transport/SweepControl/Typedefs/Instrument Classes--Cluster.ctl"
File 44="user.lib/Levylab/Transport/SweepControl/Typedefs/PostAction.ctl"
File 45="user.lib/Levylab/Transport/SweepControl/Typedefs/ScanControl.ctl"
File 46="user.lib/Levylab/Transport/SweepControl/Typedefs/ScanParamters.ctl"
File 47="user.lib/Levylab/Transport/SweepControl/Typedefs/Sweep Control Configuration--Cluster.ctl"
File 48="user.lib/Levylab/Transport/SweepControl/Typedefs/XP Style VISA Control.ctl"
File 49="user.lib/Levylab/Transport/SweepControl/subVIs/AppendDBLtoComments.vi"
File 50="user.lib/Levylab/Transport/SweepControl/subVIs/Create Scan.vi"
File 51="user.lib/Levylab/Transport/SweepControl/subVIs/D-Lockin.vi"
File 52="user.lib/Levylab/Transport/SweepControl/subVIs/Post action.vi"
File 53="user.lib/Levylab/Transport/SweepControl/subVIs/Scan action.vi"
File 54="user.lib/Levylab/Transport/SweepControl/subVIs/Sort Scan Parameters.vi"
File 55="user.lib/Levylab/Transport/SweepControl/subVIs/Sweep Control Inner Loop.vi"
File 56="user.lib/Levylab/Transport/SweepControl/subVIs/Sweep Control Loop.vi"
File 57="user.lib/Levylab/Transport/SweepControl/API (file)/Read Continuous B Sweep.json.vi"
File 58="user.lib/Levylab/Transport/SweepControl/API (file)/Read Sweep Control.json.vi"
File 59="user.lib/Levylab/Transport/SweepControl/API/Read Control Experiment.vi"
File 60="user.lib/Levylab/Transport/SweepControl/API/Read Sorted scan parameters.vi"
File 61="user.lib/Levylab/Transport/SweepControl/API/Read Sweep Configuration Example.vi"
File 62="user.lib/Levylab/Transport/SweepControl/API/Read Sweep Configuration File.vi"
File 63="user.lib/Levylab/Transport/SweepControl/API/Take Measurement.vi"
File 64="user.lib/Levylab/Transport/Control Experiment/Control Experiment.lvclass"
File 65="user.lib/Levylab/Transport/Control Experiment/Control Experiment.vi"
File 66="user.lib/Levylab/Transport/Control Experiment/Tree.vi"
File 67="user.lib/Levylab/Transport/Control Experiment/Typedefs/Experiment Description--cluster.ctl"
File 68="user.lib/Levylab/Transport/Control Experiment/Typedefs/Instrument--enum.ctl"
File 69="user.lib/Levylab/Transport/Control Experiment/Typedefs/Instruments--cluster.ctl"
File 70="user.lib/Levylab/Transport/Control Experiment/Typedefs/KH Mode-enum.ctl"
File 71="user.lib/Levylab/Transport/Control Experiment/Typedefs/Wiring Description--cluster.ctl"
File 72="user.lib/Levylab/Transport/Control Experiment/subVIs/DBL Variant or Array Variant to Array.vi"
File 73="user.lib/Levylab/Transport/Control Experiment/subVIs/DSC Device and User Paths.vi"
File 74="user.lib/Levylab/Transport/Control Experiment/subVIs/ElectrodesLabelsToPickeringChannels.vi"
File 75="user.lib/Levylab/Transport/Control Experiment/subVIs/GetTimeISO.vi"
File 76="user.lib/Levylab/Transport/Control Experiment/subVIs/Instrument.Cryostat Class Paths.vi"
File 77="user.lib/Levylab/Transport/Control Experiment/subVIs/Letter to Index.vi"
File 78="user.lib/Levylab/Transport/Control Experiment/subVIs/Load Instrument.Cryostat Classes.vi"
File 79="user.lib/Levylab/Transport/Control Experiment/subVIs/Multiply Gains.vi"
File 80="user.lib/Levylab/Transport/Control Experiment/subVIs/Pickering/Pickering 4 Wire Asynchronous.vi"
File 81="user.lib/Levylab/Transport/Control Experiment/subVIs/Pickering/Pickering 4 Wire PPMS DR Asynchronous.vi"
File 82="user.lib/Levylab/Transport/Control Experiment/subVIs/Pickering/PickeringReadConfig Asynchronous.vi"
File 83="user.lib/Levylab/Transport/Control Experiment/subVIs/Pickering/PickeringWriteConfig Asynchronous.vi"
File 84="user.lib/Levylab/Transport/Control Experiment/subVIs/Asana/Asana Dictionary Get Value.vi"
File 85="user.lib/Levylab/Transport/Control Experiment/subVIs/Asana/Asana Dictionary Tasks Get Value.vi"
File 86="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Device Description.vi"
File 87="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Experiment Description.vi"
File 88="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Lockin Description.vi"
File 89="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Sweep Description.vi"
File 90="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Add Wiring Description.vi"
File 91="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Create Lockin AO Description.vi"
File 92="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Create Lockin REF Description.vi"
File 93="user.lib/Levylab/Transport/Control Experiment/Comments/Comments.Create Lockin Sampling Description.vi"
File 94="user.lib/Levylab/Transport/Control Experiment/Comments/Generate Comments.vi"
File 95="user.lib/Levylab/Transport/Control Experiment/Comments/YAML/YAML.AddSections.vi"
File 96="user.lib/Levylab/Transport/Control Experiment/Comments/YAML/YAML.List.vi"
File 97="user.lib/Levylab/Transport/Control Experiment/Comments/YAML/YAML.Multiline.vi"
File 98="user.lib/Levylab/Transport/Control Experiment/Comments/YAML/YAML.NestedSection.vi"
File 99="user.lib/Levylab/Transport/Control Experiment/Comments/YAML/YAML.Scaler.vi"
File 100="user.lib/Levylab/Transport/Control Experiment/API (File)/Control Experiment FGV.vi"
File 101="user.lib/Levylab/Transport/Control Experiment/API (File)/Create Transport DAT File.vi"
File 102="user.lib/Levylab/Transport/Control Experiment/API (File)/Save JSON File.vi"
File 103="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport DAT File 2D.vi"
File 104="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport DAT File.vi"
File 105="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport ITX File.vi"
File 106="user.lib/Levylab/Transport/Control Experiment/API (File)/Save Transport TDMS File.vi"
File 107="user.lib/Levylab/Transport/Control Experiment/API/Erase Comments.vi"
File 108="user.lib/Levylab/Transport/Control Experiment/API/Get Channel Indices.vi"
File 109="user.lib/Levylab/Transport/Control Experiment/API/Read Comments.vi"
File 110="user.lib/Levylab/Transport/Control Experiment/API/Read Device.vi"
File 111="user.lib/Levylab/Transport/Control Experiment/API/Read Experiment Configuration.vi"
File 112="user.lib/Levylab/Transport/Control Experiment/API/Read Experiment Description.vi"
File 113="user.lib/Levylab/Transport/Control Experiment/API/Read Experiment Path.vi"
File 114="user.lib/Levylab/Transport/Control Experiment/API/Read Instruments.vi"
File 115="user.lib/Levylab/Transport/Control Experiment/API/Read Wiring Configuration.vi"
File 116="user.lib/Levylab/Transport/Control Experiment/API/Write Experiment Description.vi"
File 117="user.lib/Levylab/Transport/Control Experiment/API/Write Experiment Folder.vi"
File 118="user.lib/Levylab/Transport/Control Experiment/API/Write Sweep Element.vi"
File 119="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Append Dictionary Element.vi"
File 120="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Close Dictionary.vi"
File 121="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Read All Dictionary Elements.vi"
File 122="user.lib/Levylab/Transport/Control Experiment/API/Dictionary/Write Dictionary Element.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=17
File 0="_functions_levylab_lib_transport_1.mnu"
File 1="_functions_levylab_lib_transport_10.mnu"
File 2="_functions_levylab_lib_transport_11.mnu"
File 3="_functions_levylab_lib_transport_12.mnu"
File 4="_functions_levylab_lib_transport_13.mnu"
File 5="_functions_levylab_lib_transport_14.mnu"
File 6="_functions_levylab_lib_transport_15.mnu"
File 7="_functions_levylab_lib_transport_16.mnu"
File 8="_functions_levylab_lib_transport_2.mnu"
File 9="_functions_levylab_lib_transport_3.mnu"
File 10="_functions_levylab_lib_transport_4.mnu"
File 11="_functions_levylab_lib_transport_5.mnu"
File 12="_functions_levylab_lib_transport_6.mnu"
File 13="_functions_levylab_lib_transport_7.mnu"
File 14="_functions_levylab_lib_transport_8.mnu"
File 15="_functions_levylab_lib_transport_9.mnu"
File 16="functions_Levylab_lib_Transport.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

[Package]
Name="levylab_lib_lvtoitx"
Version="3.3.5.10"
Release=""
ID=057d9124d7d9681eff0441fb46dde181
File Format="vip"
Format Version="2017"
Display Name="LV-Data"


[Description]
Description="Collection of VIs to write and read TDMS, Igor Text Files (*.itx), text-based spreadsheet data files (*.dat), postgreSQL. Tools are also provided for uploading to and downloading from AWS S3."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[3.3.4]\0A\0DLV-Data.PGSQL:\0A- Issue #83: Column datatype is now combo box\0A- Improve connection handling in Execute SQL and Read SQL\0A\0A"
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
Requires="i3_external_encryption>=1.0.0.8,jdp_science_postgresql>=0.3.5.23,jki_lib_caraya>=1.2.1.131,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,ni_cloud_toolkit_for_aws>=1.1.0.1,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=240
File 0="user.lib/LevyLab/LV-Data/Macros/Conversion.lvclass"
File 1="user.lib/LevyLab/LV-Data/Macros/Convert Experiment Folder.vi"
File 2="user.lib/LevyLab/LV-Data/Macros/Support/Dictionary.Add File and Notes.vi"
File 3="user.lib/LevyLab/LV-Data/Macros/Support/Dictionary.Add Time Values.vi"
File 4="user.lib/LevyLab/LV-Data/Macros/Support/Dictionary.Compare.vi"
File 5="user.lib/LevyLab/LV-Data/Macros/Support/Dictionary.Expand Array Size.vi"
File 6="user.lib/LevyLab/LV-Data/Macros/Support/Dictionary.Remove Empty.vi"
File 7="user.lib/LevyLab/LV-Data/Macros/Support/Dictionary.Split into DBL and String.vi"
File 8="user.lib/LevyLab/LV-Data/Macros/Support/Write Experiment to TDMS Conversion Log.vi"
File 9="user.lib/LevyLab/LV-Data/Macros/ITX/File to TDMS.vi"
File 10="user.lib/LevyLab/LV-Data/LV-Data.TDMS/LV-Data.TDMS.lvclass"
File 11="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Private/Index to Group Name.vi"
File 12="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Private/Read TDMS.vi"
File 13="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Private/Write TDMS.vi"
File 14="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Overrides/Close.vi"
File 15="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Overrides/Open.vi"
File 16="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Overrides/Read.vi"
File 17="user.lib/LevyLab/LV-Data/LV-Data.TDMS/Overrides/Write.vi"
File 18="user.lib/LevyLab/LV-Data/LV-Data.TDMS/API/Read TDMS Comments.vi"
File 19="user.lib/LevyLab/LV-Data/LV-Data.TDMS/API/Read TDMS Wave 1D.vi"
File 20="user.lib/LevyLab/LV-Data/LV-Data.TDMS/API/Read TDMS Wavenames into Ring.vi"
File 21="user.lib/LevyLab/LV-Data/LV-Data.TDMS/API/Read TDMS Wavenames.vi"
File 22="user.lib/LevyLab/LV-Data/LV-Data.TDMS/API/Read TDMS XYN.vi"
File 23="user.lib/LevyLab/LV-Data/LV-Data.S3/LV-Data.S3.lvclass"
File 24="user.lib/LevyLab/LV-Data/LV-Data.S3/Tree.vi"
File 25="user.lib/LevyLab/LV-Data/LV-Data.S3/Typedefs/S3 Backup--cluster.ctl"
File 26="user.lib/LevyLab/LV-Data/LV-Data.S3/private/AWS Credentials Dialog.vi"
File 27="user.lib/LevyLab/LV-Data/LV-Data.S3/private/Handle S3 Error.vi"
File 28="user.lib/LevyLab/LV-Data/LV-Data.S3/private/recursively populate tree ctl.vi"
File 29="user.lib/LevyLab/LV-Data/LV-Data.S3/private/split object path to hierarchy.vi"
File 30="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Download File.vi"
File 31="user.lib/LevyLab/LV-Data/LV-Data.S3/API/List Bucket Contents.vi"
File 32="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Populate Tree Ctl from Bucket.vi"
File 33="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Read AWS Credentials File.vi"
File 34="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Read.vi"
File 35="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Set Bucket.vi"
File 36="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Upload File.vi"
File 37="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Verify File.vi"
File 38="user.lib/LevyLab/LV-Data/LV-Data.S3/API/Write.vi"
File 39="user.lib/LevyLab/LV-Data/LV-Data.PG/LV-Data.PGSQL.lvclass"
File 40="user.lib/LevyLab/LV-Data/LV-Data.PG/Tree.vi"
File 41="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Convert Dictionary to ITEMs and VALUEs.vi"
File 42="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Format SQL CREATE TABLE.vi"
File 43="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Format SQL INSERT Dictionary.vi"
File 44="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Read.vi"
File 45="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Write.vi"
File 46="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Configuration--cluster.ctl"
File 47="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Datatypes--combo.ctl"
File 48="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Datatypes--enum.ctl"
File 49="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Errors--enum.ctl"
File 50="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Data.vi"
File 51="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test MultiValue INSERT format.vi"
File 52="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test MultiValue INSERT.vi"
File 53="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test PQ modes.vi"
File 54="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Switch Tables 2.vi"
File 55="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Switch Tables.vi"
File 56="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Write and Read Data.vi"
File 57="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Change Column Name.vi"
File 58="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Change Column Units.vi"
File 59="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Configuration Path.vi"
File 60="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Configuration Window.vi"
File 61="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Convert Double to String.vi"
File 62="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Create Table.vi"
File 63="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Create User.vi"
File 64="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Data Type Enum to Data Type String.vi"
File 65="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Delete Column.vi"
File 66="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Delete Table.vi"
File 67="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Error Code.vi"
File 68="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Execute SQL.vi"
File 69="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Format SQL INSERT Multivalue.vi"
File 70="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Format SQL INSERT.vi"
File 71="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Configuration.vi"
File 72="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Data Type from Path.vi"
File 73="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Data Type Prefix.vi"
File 74="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Users.vi"
File 75="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Handle INSERT Error.vi"
File 76="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/INSERT Multivalue.vi"
File 77="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/INSERT.vi"
File 78="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Parse Variant.vi"
File 79="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/password_prompt.vi"
File 80="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Path flags.vi"
File 81="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Path Variant to Path Array.vi"
File 82="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Paths to String with Commas.vi"
File 83="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Push Backup to DB.vi"
File 84="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Read Configuration.vi"
File 85="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Rename Table.vi"
File 86="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/SQL Time to Timestamp.vi"
File 87="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/String Array to String with Commas.vi"
File 88="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Timestamp to SQL Time.vi"
File 89="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Write Configuration.vi"
File 90="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/Get Trace (example).vi"
File 91="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/INSERT (example).vi"
File 92="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/INSERT PPMS4 (example).vi"
File 93="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/Multi-Table Insert.vi"
File 94="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Check existence.vi"
File 95="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Copy Speed Test.vi"
File 96="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Get PGSQL datatype.vi"
File 97="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Switch Columns between Test tables.vi"
File 98="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Switch Tables.vi"
File 99="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Build Path.vi"
File 100="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Close.vi"
File 101="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Compare Previous INSERT.vi"
File 102="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Copy (Data).vi"
File 103="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Copy (File).vi"
File 104="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Copy (String Data).vi"
File 105="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Create Column.vi"
File 106="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Column Path.vi"
File 107="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Columns.vi"
File 108="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Table Path.vi"
File 109="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Tables.vi"
File 110="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Open.vi"
File 111="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Parse path.vi"
File 112="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read SQL.vi"
File 113="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Trace.vi"
File 114="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Traces.vi"
File 115="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (boolean).vi"
File 116="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (double).vi"
File 117="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (string).vi"
File 118="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable.vi"
File 119="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Write Variable (multirow).vi"
File 120="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Write Variable (one-row).vi"
File 121="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Write Variable.vi"
File 122="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Administer Tables UI.vi"
File 123="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Create User UI.vi"
File 124="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Get Path UI.vi"
File 125="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Get Paths Array UI.vi"
File 126="user.lib/LevyLab/LV-Data/LV-Data.ITX/LV to ITX  Retrieve Equation.vi"
File 127="user.lib/LevyLab/LV-Data/LV-Data.ITX/LV to ITX  Retrieve.vi"
File 128="user.lib/LevyLab/LV-Data/LV-Data.ITX/LV to ITX 2D AutoPlot.vi"
File 129="user.lib/LevyLab/LV-Data/LV-Data.ITX/LV to ITX XY AutoPlot.vi"
File 130="user.lib/LevyLab/LV-Data/LV-Data.ITX/LV to ITX XY2 AutoPlot.vi"
File 131="user.lib/LevyLab/LV-Data/LV-Data.ITX/LV-Data.ITX.lvclass"
File 132="user.lib/LevyLab/LV-Data/LV-Data.ITX/Read ITX.vi"
File 133="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/1D Dbl to ITX Wave.vi"
File 134="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/1D Str to ITX Wave.vi"
File 135="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/2D Commands.vi"
File 136="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/2D Dbl to ITX Wave.vi"
File 137="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/2D X&Y Commands.vi"
File 138="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/Create Folder Index.vi"
File 139="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/IBW aperture Commands.vi"
File 140="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/ITX2 Plot Commands.vi"
File 141="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/Notes to ITX.vi"
File 142="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/Parse Comments and Commands.vi"
File 143="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/R+coord Commands.vi"
File 144="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/Read Folder Index.vi"
File 145="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/XY from 2D Commands.vi"
File 146="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/XY Plot Commands W2D.vi"
File 147="user.lib/LevyLab/LV-Data/LV-Data.ITX/util/XY Plot Commands.vi"
File 148="user.lib/LevyLab/LV-Data/LV-Data.ITX/Typedefs/Retrieve Data Type.ctl"
File 149="user.lib/LevyLab/LV-Data/LV-Data.ITX/Typedefs/Retrieve Formula Type.ctl"
File 150="user.lib/LevyLab/LV-Data/LV-Data.ITX/Typedefs/Retrieve Index.ctl"
File 151="user.lib/LevyLab/LV-Data/LV-Data.ITX/Typedefs/Retrieve N Results.ctl"
File 152="user.lib/LevyLab/LV-Data/LV-Data.ITX/private/Check Wavename Length.vi"
File 153="user.lib/LevyLab/LV-Data/LV-Data.ITX/private/Format Wavename.vi"
File 154="user.lib/LevyLab/LV-Data/LV-Data.ITX/Overrides/Read.vi"
File 155="user.lib/LevyLab/LV-Data/LV-Data.ITX/Overrides/Write.vi"
File 156="user.lib/LevyLab/LV-Data/LV-Data.ITX/Main/Parse ITX String.vi"
File 157="user.lib/LevyLab/LV-Data/LV-Data.ITX/Main/Write ITX (2D w X&Y).vi"
File 158="user.lib/LevyLab/LV-Data/LV-Data.ITX/Main/Write ITX (R+coord).vi"
File 159="user.lib/LevyLab/LV-Data/LV-Data.ITX/Main/Write ITX (XY).vi"
File 160="user.lib/LevyLab/LV-Data/LV-Data.ITX/Main/Write ITX (XY2).vi"
File 161="user.lib/LevyLab/LV-Data/LV-Data.ITX/Main/Write ITX.vi"
File 162="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/Format ITX Graph.vi"
File 163="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/ITX Commands.lvclass"
File 164="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/typedefs/grid--enum.ctl"
File 165="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/typedefs/Label--cluster.ctl"
File 166="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/typedefs/Log--cluster.ctl"
File 167="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/typedefs/log--enum.ctl"
File 168="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/typedefs/textbox_anchorcolumn--enum.ctl"
File 169="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/typedefs/textbox_anchorrow--enum.ctl"
File 170="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/private/Commands to ITX.vi"
File 171="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/AppendImage.vi"
File 172="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/AppendToGraph.vi"
File 173="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ColorScale.vi"
File 174="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/Commands to ITX.vi"
File 175="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/Generate Command String.vi"
File 176="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/Label.vi"
File 177="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/Legend.vi"
File 178="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph axThick.vi"
File 179="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph grid.vi"
File 180="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph height.vi"
File 181="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph Log.vi"
File 182="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph mirror.vi"
File 183="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph prescaleExp.vi"
File 184="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph rgb.vi"
File 185="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyGraph width.vi"
File 186="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/ModifyImage ctab.vi"
File 187="user.lib/LevyLab/LV-Data/LV-Data.ITX/ITX Commands/API/Textbox.vi"
File 188="user.lib/LevyLab/LV-Data/LV-Data.ITX/Graph/Configure XY Graph.vi"
File 189="user.lib/LevyLab/LV-Data/LV-Data.ITX/Graph/Intensity Graph to Igor Graph.vi"
File 190="user.lib/LevyLab/LV-Data/LV-Data.ITX/Graph/LV to Igor Graph (UI).vi"
File 191="user.lib/LevyLab/LV-Data/LV-Data.ITX/Graph/XY Graph to Igor Graph.vi"
File 192="user.lib/LevyLab/LV-Data/LV-Data.DAT/LV-Data.DAT.lvclass"
File 193="user.lib/LevyLab/LV-Data/LV-Data.DAT/Read DAT.vi"
File 194="user.lib/LevyLab/LV-Data/LV-Data.DAT/Write DAT (1D).vi"
File 195="user.lib/LevyLab/LV-Data/LV-Data.DAT/Write DAT (2D).vi"
File 196="user.lib/LevyLab/LV-Data/LV-Data.DAT/Write DAT.vi"
File 197="user.lib/LevyLab/LV-Data/LV-Data.DAT/private/Parse DAT String.vi"
File 198="user.lib/LevyLab/LV-Data/LV-Data.DAT/Overrides/Read.vi"
File 199="user.lib/LevyLab/LV-Data/LV-Data.DAT/Overrides/Write.vi"
File 200="user.lib/LevyLab/LV-Data/LV-Data/Data Read.vi"
File 201="user.lib/LevyLab/LV-Data/LV-Data/Data Write.vi"
File 202="user.lib/LevyLab/LV-Data/LV-Data/LV-Data.lvclass"
File 203="user.lib/LevyLab/LV-Data/LV-Data/Typedefs/Dictionary--cluster.ctl"
File 204="user.lib/LevyLab/LV-Data/LV-Data/Typedefs/File Type--enum.ctl"
File 205="user.lib/LevyLab/LV-Data/LV-Data/Typedefs/Operation--enum.ctl"
File 206="user.lib/LevyLab/LV-Data/LV-Data/Protected/Add Letter.vi"
File 207="user.lib/LevyLab/LV-Data/LV-Data/Protected/Populate Ring Text [].vi"
File 208="user.lib/LevyLab/LV-Data/LV-Data/Protected/Replace Period with Underscore.vi"
File 209="user.lib/LevyLab/LV-Data/LV-Data/Protected/Replace Space with Empty.vi"
File 210="user.lib/LevyLab/LV-Data/LV-Data/Protected/Variant to DBL Array.vi"
File 211="user.lib/LevyLab/LV-Data/LV-Data/Protected/Variant to String.vi"
File 212="user.lib/LevyLab/LV-Data/LV-Data/Private/Format Path and Filename.vi"
File 213="user.lib/LevyLab/LV-Data/LV-Data/Framework (For Override)/Close.vi"
File 214="user.lib/LevyLab/LV-Data/LV-Data/Framework (For Override)/Create.vi"
File 215="user.lib/LevyLab/LV-Data/LV-Data/Framework (For Override)/Open.vi"
File 216="user.lib/LevyLab/LV-Data/LV-Data/Framework (For Override)/Read.vi"
File 217="user.lib/LevyLab/LV-Data/LV-Data/Framework (For Override)/Write.vi"
File 218="user.lib/LevyLab/LV-Data/LV-Data/API/Append to Data (Dictionary).vi"
File 219="user.lib/LevyLab/LV-Data/LV-Data/API/Read Append Index.vi"
File 220="user.lib/LevyLab/LV-Data/LV-Data/API/Read Append.vi"
File 221="user.lib/LevyLab/LV-Data/LV-Data/API/Read Data (Dictionary).vi"
File 222="user.lib/LevyLab/LV-Data/LV-Data/API/Read Igor Commands.vi"
File 223="user.lib/LevyLab/LV-Data/LV-Data/API/Read Notes.vi"
File 224="user.lib/LevyLab/LV-Data/LV-Data/API/Read Operation.vi"
File 225="user.lib/LevyLab/LV-Data/LV-Data/API/Read Path.vi"
File 226="user.lib/LevyLab/LV-Data/LV-Data/API/Read Wavenames.vi"
File 227="user.lib/LevyLab/LV-Data/LV-Data/API/Write Append.vi"
File 228="user.lib/LevyLab/LV-Data/LV-Data/API/Write Data (Dictionary).vi"
File 229="user.lib/LevyLab/LV-Data/LV-Data/API/Write Igor Commands.vi"
File 230="user.lib/LevyLab/LV-Data/LV-Data/API/Write Notes.vi"
File 231="user.lib/LevyLab/LV-Data/LV-Data/API/Write Path.vi"
File 232="user.lib/LevyLab/LV-Data/LV-Data/API/XY-Data to Dictionary (Multiple).vi"
File 233="user.lib/LevyLab/LV-Data/LV-Data/API/XY-Data to Dictionary (single).vi"
File 234="user.lib/LevyLab/LV-Data/LV-Data/API/XY-Data to Dictionary.vi"
File 235="user.lib/LevyLab/LV-Data/Examples/DAT Example.vi"
File 236="user.lib/LevyLab/LV-Data/Examples/ITX Example.vi"
File 237="user.lib/LevyLab/LV-Data/Examples/ITX2 Example.vi"
File 238="user.lib/LevyLab/LV-Data/Examples/TDMS Read Example.vi"
File 239="user.lib/LevyLab/LV-Data/Examples/Tree.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=40
File 0="_functions_levylab_lib_lvtoitx_1.mnu"
File 1="_functions_levylab_lib_lvtoitx_10.mnu"
File 2="_functions_levylab_lib_lvtoitx_11.mnu"
File 3="_functions_levylab_lib_lvtoitx_12.mnu"
File 4="_functions_levylab_lib_lvtoitx_13.mnu"
File 5="_functions_levylab_lib_lvtoitx_14.mnu"
File 6="_functions_levylab_lib_lvtoitx_15.mnu"
File 7="_functions_levylab_lib_lvtoitx_16.mnu"
File 8="_functions_levylab_lib_lvtoitx_17.mnu"
File 9="_functions_levylab_lib_lvtoitx_18.mnu"
File 10="_functions_levylab_lib_lvtoitx_19.mnu"
File 11="_functions_levylab_lib_lvtoitx_2.mnu"
File 12="_functions_levylab_lib_lvtoitx_20.mnu"
File 13="_functions_levylab_lib_lvtoitx_21.mnu"
File 14="_functions_levylab_lib_lvtoitx_22.mnu"
File 15="_functions_levylab_lib_lvtoitx_23.mnu"
File 16="_functions_levylab_lib_lvtoitx_24.mnu"
File 17="_functions_levylab_lib_lvtoitx_25.mnu"
File 18="_functions_levylab_lib_lvtoitx_26.mnu"
File 19="_functions_levylab_lib_lvtoitx_27.mnu"
File 20="_functions_levylab_lib_lvtoitx_28.mnu"
File 21="_functions_levylab_lib_lvtoitx_29.mnu"
File 22="_functions_levylab_lib_lvtoitx_3.mnu"
File 23="_functions_levylab_lib_lvtoitx_30.mnu"
File 24="_functions_levylab_lib_lvtoitx_31.mnu"
File 25="_functions_levylab_lib_lvtoitx_32.mnu"
File 26="_functions_levylab_lib_lvtoitx_33.mnu"
File 27="_functions_levylab_lib_lvtoitx_34.mnu"
File 28="_functions_levylab_lib_lvtoitx_35.mnu"
File 29="_functions_levylab_lib_lvtoitx_36.mnu"
File 30="_functions_levylab_lib_lvtoitx_37.mnu"
File 31="_functions_levylab_lib_lvtoitx_38.mnu"
File 32="_functions_levylab_lib_lvtoitx_39.mnu"
File 33="_functions_levylab_lib_lvtoitx_4.mnu"
File 34="_functions_levylab_lib_lvtoitx_5.mnu"
File 35="_functions_levylab_lib_lvtoitx_6.mnu"
File 36="_functions_levylab_lib_lvtoitx_7.mnu"
File 37="_functions_levylab_lib_lvtoitx_8.mnu"
File 38="_functions_levylab_lib_lvtoitx_9.mnu"
File 39="functions_levylab_lib_lvtoitx.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

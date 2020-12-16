[Package]
Name="levylab_lib_lockin_multichannel"
Version="2.12.1.48"
Release=""
ID=4e55b81c9ac946a4775f403ba4556d5e
File Format="vip"
Format Version="2017"
Display Name="Multichannel Lockin"


[Description]
Description="Multichannel Lockin for National Instruments' Dynamic Signal Acquisition hardware (4431, 4461, 4462). This version is configured to handle multiple cards (up to 16) for simultaneous, synchronized AI/AO. You can configure a number of analog outputs (up to 32) to output sine, square, sawtooth, or triangle functions with DC offsets. Each of the analog inputs (up to 32) can be demodulated at multiple frequencies."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.12.1]\0A\0D- Update to Instrument Framework v1.7 (fixes missing LevyLab.lvclass issue)\0A- Change the way Lockin Engine handles waveform arrays (applies low pass filter to interleved X and Y channels rather than parallel low pass filters)\0A- Lockin Engine organized into subVIs"
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
Requires="jdp_science_postgresql>=0.1.1.10,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.3.0.56,labview-zmq>=3.5.1.109,lava_lib_ui_tools>=1.4.1.74,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.2.4,levylab_lib_lvtoitx>=3.0.5.13,levylab_lib_postgresql>=1.2.2.14,levylab_lib_voltage_update>=1.0.3.5,levylab_lib_xy_utilities>=1.2.0.12,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56,levylab_lib_levylab_instruments>=1.7.0.95"
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
Num Files=306
File 0="user.lib/LevyLab/Lockin-Multichannel/Multichannel Lockin.lvproj"
File 1="user.lib/LevyLab/Lockin-Multichannel/Multichannel Lockin.vi"
File 2="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/4461-SIMULATEDDEVICES.NCE"
File 3="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Lockin.DAQ.lvclass"
File 4="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Process.vi"
File 5="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Waveguide Model/Waveguide Model--Cluster.ctl"
File 6="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Waveguide Model/Waveguide Model.vi"
File 7="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/446xAI-enum.ctl"
File 8="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/446xAO-enum.ctl"
File 9="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI Prefilter-cluster.ctl"
File 10="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI Simulation-enum.ctl"
File 11="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI.config(UI)-array.ctl"
File 12="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI.config(UI)-cluster.ctl"
File 13="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI.config-array.ctl"
File 14="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI.config-cluster.ctl"
File 15="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AI.coupling-enum.ctl"
File 16="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AmplifierType-enum.ctl"
File 17="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AO-cluster.ctl"
File 18="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AO.config(UI)-array.ctl"
File 19="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AO.config(UI)-cluster.ctl"
File 20="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AO.config-array.ctl"
File 21="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AO.config-cluster.ctl"
File 22="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/AO_Channel-Numeric.ctl"
File 23="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Cal Info - Cluster.ctl"
File 24="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/DAQType-enum.ctl"
File 25="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Front Panel Cluster.ctl"
File 26="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Function+DC-enum.ctl"
File 27="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Function-enum.ctl"
File 28="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/INI-enum.ctl"
File 29="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/New Channel Cluster.ctl"
File 30="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Cluster.ctl"
File 31="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.autoContigureDAQ.ctl"
File 32="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.measureOffset.ctl"
File 33="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setAIconfig.ctl"
File 34="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setAO.ctl"
File 35="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setAOconfig.ctl"
File 36="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setGain.ctl"
File 37="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setPreFilter.ctl"
File 38="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setREF.ctl"
File 39="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setSampling.ctl"
File 40="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setState.ctl"
File 41="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.setSweep.ctl"
File 42="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--Lockin.DAQ.zeroOffset.ctl"
File 43="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--LockinDAQ.Calibrate.ctl"
File 44="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PrivateEvents--LockinDAQ.setCalibration.ctl"
File 45="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Cluster.ctl"
File 46="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getAI.ctl"
File 47="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getAO.ctl"
File 48="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getAOChannels.ctl"
File 49="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getCalibration.ctl"
File 50="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getDAQconfig.ctl"
File 51="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getDAQState.ctl"
File 52="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getIVSweepResults.ctl"
File 53="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getREF.ctl"
File 54="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getREFChannels.ctl"
File 55="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getResults.ctl"
File 56="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--Lockin.DAQ.getSweepResults.ctl"
File 57="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/PublicEvents--LockinDAQ.Calibrate.ctl"
File 58="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/REF-cluster.ctl"
File 59="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/REF_Channel-Numeric.ctl"
File 60="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Results--Cluster.ctl"
File 61="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Sample Mode--Ring.ctl"
File 62="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Sampling.ctl"
File 63="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Set State-enum.ctl"
File 64="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/State-enum.ctl"
File 65="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/Sweep Configuration--Cluster.ctl"
File 66="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/SweepResults--Cluster.ctl"
File 67="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Typedefs/XP Style VISA Control.ctl"
File 68="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Tests/Test LockinEngine.vi"
File 69="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Tests/Test PLL.vi"
File 70="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Tests/Test Sweep.vi"
File 71="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/AddParametersToSweepResults.vi"
File 72="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/ConcatenateSweepResults.vi"
File 73="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/Generator DC Sweep Manager.vi"
File 74="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/Lockin.DAQ.Configure Sweep 3.vi"
File 75="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/Lockin.DAQ.Configure Sweep 4.vi"
File 76="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/Lockin.DAQ.Configure Sweep.vi"
File 77="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Sweep/Lockin.DAQ.Set Initial Value.vi"
File 78="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getAI.vi"
File 79="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getAO.vi"
File 80="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getAOChannels.vi"
File 81="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getCalibration.vi"
File 82="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getDAQconfig.vi"
File 83="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getDAQState.vi"
File 84="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getIVSweepResults.vi"
File 85="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.GetPrivateEvents.vi"
File 86="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getREF.vi"
File 87="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getREFChannels.vi"
File 88="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getResults.vi"
File 89="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Lockin.DAQ.getSweepResults.vi"
File 90="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Tree.vi"
File 91="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/private/Wait Until SMO Started.vi"
File 92="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Methods (overrides)/CreatePrivateEvents.vi"
File 93="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Methods (overrides)/CreatePublicEvents.vi"
File 94="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Methods (overrides)/DestroyPrivateEvents.vi"
File 95="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/Methods (overrides)/DestroyPublicEvents.vi"
File 96="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 - Create AO DC waveforms.vi"
File 97="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 - Create AO waveforms - Multitone.vi"
File 98="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 - Create AO waveforms.vi"
File 99="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 - Create Reference Waveforms.vi"
File 100="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 Autophase.vi"
File 101="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 Export Triggers.vi"
File 102="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/4461 Replace AO Ch.vi"
File 103="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/44xx AI Min and Max.vi"
File 104="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/44xx AO Min and Max.vi"
File 105="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/44xx Ref Clk.vi"
File 106="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Auto Configure DAQ.vi"
File 107="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Example-Waveform Circular Buffer.vi"
File 108="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Frequency Mixer.vi"
File 109="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Get Dev Product Type.vi"
File 110="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Get Master and Slave Tasks.vi"
File 111="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Get Terminal Name with Device Prefix.vi"
File 112="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin Engine.vi"
File 113="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Calibrate.vi"
File 114="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Clear.vi"
File 115="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Create.AI Task.vi"
File 116="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Create.AO Task.vi"
File 117="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Create.Sample Clock.vi"
File 118="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Create.vi"
File 119="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.DAQmx Read.vi"
File 120="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.DAQmx Write.vi"
File 121="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.ErrorHandler.vi"
File 122="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.EventRegistration.vi"
File 123="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Generate.Waveforms.vi"
File 124="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Get Calibration.vi"
File 125="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Read AI and Write AO.vi"
File 126="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Read AI.vi"
File 127="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Simulate Noisy AI.vi"
File 128="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Simulate Waveguide.vi"
File 129="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Start.AI.vi"
File 130="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Start.AO.vi"
File 131="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Start.vi"
File 132="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Stop.vi"
File 133="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.TimedLoop.vi"
File 134="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Trigger.vi"
File 135="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lockin.DAQ.Write AO.vi"
File 136="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Low Pass Filter.vi"
File 137="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Lowpass Filter.vi"
File 138="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Multitone Eval.vi"
File 139="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/PLL_PID.vi"
File 140="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Test Multitone.vi"
File 141="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/Waveform Circular Buffer.vi"
File 142="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Clip AO Waveforms.vi"
File 143="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/decimate_waveforms.vi"
File 144="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Divide Gain.vi"
File 145="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/FPDAQtoDAQstrings.vi"
File 146="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Fs In Range.vi"
File 147="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Fs_to_FilterDelay.vi"
File 148="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/getTimeWithError.vi"
File 149="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - add phase element.vi"
File 150="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Lockin - Format Results.vi"
File 151="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - replace AO DC.vi"
File 152="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - replace AO Sweep Indicator.vi"
File 153="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - Restore Saved AO.vi"
File 154="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - Save AO.vi"
File 155="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - Set REF f equal AO f.vi"
File 156="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - Set REF phase equals zero.vi"
File 157="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/lockin - zero amplitude.vi"
File 158="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/ms to Hz.vi"
File 159="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Prefilter_60Hz_Notch.vi"
File 160="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Prefilter_LP.vi"
File 161="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/read_lockin_FP_DSC.vi"
File 162="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Replace timestamp.vi"
File 163="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/SI prefix.vi"
File 164="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Simple PID Array.vi"
File 165="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Split 1D ARRAY in half.vi"
File 166="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/Subtract Offset.vi"
File 167="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/update_rate_and_time.vi"
File 168="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/DAQ/support/write_lockin_FP_DSC.vi"
File 169="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write AI Configuration.vi"
File 170="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write AO Configuration.vi"
File 171="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write buffer size (S).vi"
File 172="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write Channels_ AO.vi"
File 173="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write Channels_ Reference.vi"
File 174="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write Gain.vi"
File 175="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write Ref TC and Order.vi"
File 176="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write sample mode.vi"
File 177="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API (Class)/Write sampling.vi"
File 178="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.autoConfigureDAQ.vi"
File 179="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.GetPublicEvents.vi"
File 180="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.measureOffset.vi"
File 181="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setAIconfig.vi"
File 182="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setAO.vi"
File 183="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setAOconfig.vi"
File 184="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setCalibration.vi"
File 185="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setGain.vi"
File 186="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setPreFilter.vi"
File 187="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setREF.vi"
File 188="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setSampling.vi"
File 189="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setstate.vi"
File 190="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.setSweep.vi"
File 191="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.TestLauncher.vi"
File 192="user.lib/LevyLab/Lockin-Multichannel/Lockin.DAQ/API/Lockin.DAQ.zeroOffset.vi"
File 193="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Instrument.Lockin.UI.lvclass"
File 194="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Instrument.Lockin.UI.TestLauncher.vi"
File 195="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Process.vi"
File 196="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Typedefs/Display-Enum.ctl"
File 197="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Typedefs/Lockin.Commands--Enum.ctl"
File 198="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Typedefs/X Axis-Enum.ctl"
File 199="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Typedefs/Y Axis Input-Enum.ctl"
File 200="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/Typedefs/Y Axis Output-Enum.ctl"
File 201="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/private/X Axis WFM Graph.vi"
File 202="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockinl.UI/private/Y Axis Output WFM Graph.vi"
File 203="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Instrument.Lockin.lvclass"
File 204="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Instrument.Lockin.TestLauncher.vi"
File 205="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Process.vi"
File 206="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Typedefs/configSweepFile--cluster.ctl"
File 207="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Typedefs/Lockin.Configuration--Cluster.ctl"
File 208="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Typedefs/Lockin.getAll--Cluster.ctl"
File 209="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Typedefs/Reference--Array of Cluster.ctl"
File 210="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Typedefs/Sample Mode--Enum.ctl"
File 211="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Coerce AO.vi"
File 212="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/formatSweepResults.vi"
File 213="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Client.vi"
File 214="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Command Enum to String.vi"
File 215="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Configuration Window.vi"
File 216="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Read Configuration File.vi"
File 217="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Read Configuration.vi"
File 218="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Write Configuration File.vi"
File 219="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Private/Lockin.Write Configuration.vi"
File 220="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Overrides/Configure Instrument.vi"
File 221="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Overrides/Get SMO Name.vi"
File 222="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Overrides/Get SMO Port.vi"
File 223="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Overrides/Get SMO Public API.vi"
File 224="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Overrides/getAll.vi"
File 225="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/Overrides/Handle Command.vi"
File 226="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/AI config not UI to UI.vi"
File 227="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/AI config UI to not UI.vi"
File 228="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/AO add remove elements.vi"
File 229="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/AO config not UI to UI.vi"
File 230="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/AO config UI to not UI.vi"
File 231="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/Array Add or Remove.vi"
File 232="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/config not UI to UI (AO and AI).vi"
File 233="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/config UI to not UI (AO and AI).vi"
File 234="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-public/Initialize REF Channels.vi"
File 235="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Channel String to Number of Channels.vi"
File 236="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/decimate_waveforms.vi"
File 237="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Display n or dt.vi"
File 238="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Divide by Gain.vi"
File 239="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/FloatApprox.vi"
File 240="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/FloatApproxPoint1Percent.vi"
File 241="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/format display.vi"
File 242="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Fs and Ns for integer periods.vi"
File 243="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Initialize AO Channels.vi"
File 244="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Initialize Gain.vi"
File 245="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/LegendWaveformChart.vi"
File 246="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/LegendWaveformGraph.vi"
File 247="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/LegendXYGraph.vi"
File 248="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Limit AO Amplitude.vi"
File 249="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/PS Chart.vi"
File 250="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Set all f same.vi"
File 251="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/Spinner.vi"
File 252="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/DAQ-private/State History.vi"
File 253="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write AI Configuration.vi"
File 254="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write AI WFM.vi"
File 255="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write AO Configuration.vi"
File 256="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write AO WFM.vi"
File 257="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write Channels_ AO.vi"
File 258="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write Channels_ REF.vi"
File 259="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write Gain.vi"
File 260="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write REF WFM.vi"
File 261="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write Results.vi"
File 262="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API (Class)/Write sampling.vi"
File 263="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAI.vi"
File 264="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAO.vi"
File 265="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAOconfig.vi"
File 266="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAutoSampling.vi"
File 267="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getAUX.vi"
File 268="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getGain.vi"
File 269="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getIVmode.vi"
File 270="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getIVSweepResults.vi"
File 271="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getREFconfig.vi"
File 272="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getRefreshTime.vi"
File 273="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getResults.vi"
File 274="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getSampling.vi"
File 275="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getStatus.vi"
File 276="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getSweepResults.vi"
File 277="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/getTrigger.vi"
File 278="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/Open.vi"
File 279="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/reset.vi"
File 280="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO.vi"
File 281="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_Amp.vi"
File 282="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_DC.vi"
File 283="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_f.vi"
File 284="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_function.vi"
File 285="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAO_phi.vi"
File 286="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAutoSampling.vi"
File 287="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setAUX.vi"
File 288="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setDAQ.vi"
File 289="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setGain.vi"
File 290="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setIVmodeConfig.vi"
File 291="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setREF.vi"
File 292="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setREF_f.vi"
File 293="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setREF_phi.vi"
File 294="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setSampling.vi"
File 295="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/setSweepConfiguration.vi"
File 296="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startIVAndWait.vi"
File 297="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startIVSweepAndWait.vi"
File 298="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startSweep.vi"
File 299="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/startSweepAndWait.vi"
File 300="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/stopSweep.vi"
File 301="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/trigger.vi"
File 302="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/waitForNewResults.vi"
File 303="user.lib/LevyLab/Lockin-Multichannel/Instrument.Lockin/API/waitForNewWaveforms.vi"
File 304="examples/LevyLab/Multichannel Lockin/Examples/Example_IV_Curves.vi"
File 305="examples/LevyLab/Multichannel Lockin/Examples/Example_Lockin.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_lockin_multichannel_1.mnu"
File 1="functions_LevyLab_lib_Lockin_Multichannel.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"

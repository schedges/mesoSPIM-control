import numpy as np

################
## UI OPTIONS ##
################
ui_options = {'dark_mode' : True, # Dark mode: Renders the UI dark if enabled
              'enable_x_buttons' : True, # Here, specific sets of UI buttons can be disabled
              'enable_y_buttons' : True,
              'enable_z_buttons' : True,
              'enable_f_buttons' : True,
              'enable_f_zero_button' : True, # set to False if objective change requires F-stage movement (e.g. mesoSPIM v6-Revolver), for safety reasons
              'enable_rotation_buttons' : True,
              'enable_loading_buttons' : True,
              'flip_XYZFT_button_polarity': (False, True, True, False, False), # flip the polarity of the stage buttons (X, Y, Z, F, Theta)
              'button_sleep_ms_xyzft' : (250, 250, 250, 250, 250), # step-motion buttons disabled for N ms after click. Prevents stage overshooting outside of safe limits, for slow stages.
              'window_pos': (100, 100), # position of the main window on the screen, top left corner.
              'usb_webcam_ID': 0, # open USB web-camera (if available): None,  0 (first cam), 1 (second cam), ...
              'flip_auto_LR_illumination': False, # flip the polarity of the "Auto L/R illumination" button in Acquisition Manager
               }

logging_level = 'DEBUG' # 'DEBUG' for ultra-detailed, 'INFO' for general logging level

#############################
## DAQ/WAVEFORM GENERATION ##
#############################
waveformgeneration = 'NI' # 'DemoWaveFormGeneration' or 'NI'

acquisition_hardware = {'master_trigger_out_line' : 'PXI1Slot4/port0/line0', #Digitial trigger from P0.0. Wired to PFI0 counter
                        'camera_trigger_source' : '/PXI1Slot4/PFI0', #Camera trigger signal orginates from the PFI0 input port
                        'camera_trigger_out_line' : '/PXI1Slot4/ctr0', #Camera trigger, connects to Camera TRIG_IN
                        'galvo_etl_task_line' : 'PXI1Slot4/ao0:3',    #L/R Galvo, L/R ETL
                        'galvo_etl_task_trigger_source' : '/PXI1Slot4/PFI0', #Galvo trigger signal orginates from the PFI0 input port
                        'laser_task_line' :  'PXI1Slot4/ao6:6', #Same thing?
                        'laser_task_trigger_source' : '/PXI1Slot4/PFI0'} #Laser trigger signal orginates from the PFI0 input port

sidepanel = 'Demo' #'Demo' or 'FarmSimulator', deprecated

##################
## LASER SET-UP ##
##################
laser = 'NI' # 'Demo' or 'NI'

#Must be in increasing order
laserdict = {'532 nm': 'PXI1Slot4/port0/line5'
            }

laser_blanking = 'images' # if 'images', laser is off before and after every image; if 'stacks', before and after each stack.

shutter = 'NI' # 'Demo' or 'NI'
shutterswitch = False # see legend above
shutteroptions = ('Left', 'Right') # Shutter options of the GUI
shutterdict = {'shutter_left' : 'PXI1Slot4/port0/line0', # left (general) shutter
              'shutter_right' : 'PXI1Slot4/port0/line3'} # flip mirror or right shutter, depending on physical configuration
      
##################
## CAMERA SETUP ##
##################
camera = 'HamamatsuOrcaQuest2' # 'DemoCamera' or 'HamamatsuOrcaQuest2'
camera_parameters = {'x_pixels' : 4096,
                     'y_pixels' : 2304,
                     'x_pixel_size_in_microns' : 4.6,
                     'y_pixel_size_in_microns' : 4.6,
                     'camera_id' : 0,
                     'sensor_mode' : 1,    # 12 for progressive, 1 = area, 18 = photon_number_resolving
                     'defect_correct_mode': 1, #1 = Off, 2 = On - only valid in area/progressive modes                     
                     'binning' : '1x1', #'1x1' or 1 - no binning. '2x2' or 2 - groups 2H and 2V pixels. '4x4' or 4 - same for 4 pixels. Area or photon resolving mode only.
                     'readout_speed' : 1, #1 = ultra quiet, only works if in area mode. Otherwise 2 = std
                     'sensor_cooler' : 4, #1 = off, poor performance. 2 = on, fine with air or water cooling. 4 = max, only for water cooling
                     'trigger_active' : 1,
                     'trigger_mode' : 1, # it is unclear if this is the external lightsheet mode - how to check this?
                     'trigger_polarity' : 2, # positive pulse for TTLs, default is negative
                     'trigger_source' : 2, # 2 = external
                     'subsampling' : [1,2,4], #Not used???
                    }

binning_dict = {'1x1': (1,1), '2x2':(2,2), '4x4':(4,4)}

##################
## STAGE SET-UP ##
##################
stage_parameters = {'stage_type' : 'TigerASI', # one of 'DemoStage', 'PI_1controllerNstages', 'PI_NcontrollersNstages', 'TigerASI', etc, see above
                    'y_load_position': -6000,
                    'y_unload_position': 6000,
                    'x_center_position': 0, # x-center position for the sample holder. Make sure the sample holder is actually centered at this position relative to the detection objective and light-sheet.
                    'z_center_position': 0, # z-center position for the sample holder. Make sure the sample holder is actually centered at this position relative to the detection objective and light-sheet.
                    'x_max' : 13686,
                    'x_min' : -14000,
                    'y_max' : 13164,
                    'y_min' : -40000,
                    'z_max' : 20330,
                    'z_min' : -8600,
                    'f_max' : 13000,
                    'f_min' : -20000,
                    'theta_max' : 4000,
                    'theta_min' : -4000,
                    }

asi_parameters = {'COMport' : 'COM4',
                  'baudrate' : 115200,
                  #The ASI has changed the name of its axes. So we need to remap. The key is the internal mesoSPIM variable.
                  #The axis is the ASI name for that axis. Using the ASI Tiger Console, "BU X" returns info about
                  #which card has which ASI axes names.
                  'stage_assignment': {'f':'X', 'x':'Y', 'z':'Z', 'theta':'T', 'y':'V'},
                  'encoder_conversion': {'X': 10., 'Y': 10., 'Z': 10., 'T': 10., 'V': 10.}, # num of encoder counts per um or degree, depending on stage type.
                  'speed': {'X':1.286377,'Y':1.286377,'Z':1.286250,'T':37.042030,'V':1.286377}, #Defaults, mm/sec or deg/sec
                  'stage_trigger_source': '/PXI1Slot4/PFI0',
                  'stage_trigger_out_line': '/PXI1Slot4/ctr1',
                  'stage_trigger_delay_%' : 92.5, # Set to 92.5 for stage triggering exactly after the ETL sweep
                  'stage_trigger_pulse_%' : 1,
                  'ttl_motion_enabled': True,
                  'ttl_cards':(1,2),
                  }

########################
## FILTER WHEEL SETUP ##
########################
filterwheel_parameters = {'filterwheel_type' : 'ZWO', # 'Demo', 'Ludl', 'Sutter', 'Dynamixel', 'ZWO'
                          'COMport' : 'COM3', # irrelevant for 'ZWO'
                          'baudrate' : 115200, # relevant only for 'Dynamixel'
                          'servo_id' :  1, # relevant only for 'Dynamixel'
                          }
filterdict = {'488LP' : 0, # Every config should contain at least this entry
              '520BP' : 1,
              '650BP' : 2,
              '600LP' : 3,
              'Empty': 4
              } # Dictionary labels must be unique!

###########################
## MICROSCOPE LENS SETUP ##
###########################
zoom_parameters = {'zoom_type' : 'Demo'
                   }

zoomdict = {
    '5x' :  318, #TODO: What to use here?
    '10x' : 318, #TODO: What to use here?
            }    

#Effective pixel size?
pixelsize = {
            '5x' : 0.92,
            '10x' : 0.46
            } 
      
scale_galvo_amp_with_zoom = True 

####################################
## CALCULATE UNIFORM ILLUMINATION ##
####################################
#We calculate waveform lengths and delays here. Our current approach is to start the galvos, camera exposure, laser pulse, and ETL at t=0, and have them end prior to the end of the waveform to allow the stage motion/ETL to settle
run_dict = {}
run_dict["user_target_exposure_sec"] = 0.294 #If this is long enough, we modify it to line up with galvos timing
run_dict["galvos_freq"] = 199.9 #Hz, recommended setting. 199.9Hz is max and may require active cooling for large amps (2x lens)
run_dict["settle_time_sec"] = 0.5 #After camera exposure stops, allows motion stages, ETL to settle at start locations prior to next sweep

#Calculate exposure time
galvos_duty_cycle = 50 #50% up and 50% down
galvos_phase = np.pi*(1 + galvos_duty_cycle/100.) #Galvos set to start at the peak in the falling direction
sample_freq_hz = 100000 #NI card sampling frequency
galvos_scan_time_sec = 0.5/run_dict["galvos_freq"] #Up or down time, not both
#Ensure waist illuminates each sample at least once as it moves up and down across the FOV
numGalvosScans_per_pixel_per_exposure = run_dict["user_target_exposure_sec"] / (camera_parameters["y_pixels"] * galvos_scan_time_sec) #Note the camera is rotated 90-def, so y-pixels corresponds to the X direction
rounded_galvos_scans_per_pixel_per_exposure = int(round(numGalvosScans_per_pixel_per_exposure))
if rounded_galvos_scans_per_pixel_per_exposure < 1:
  exposure_time_sec = run_dict["user_target_exposure_sec"] 
else:
  exposure_time_sec = rounded_galvos_scans_per_pixel_per_exposure*galvos_scan_time_sec*camera_parameters["y_pixels"]
#Round to nearest sample
exposure_time_samples = int(round(exposure_time_sec * sample_freq_hz))
run_dict["exposure_time_sec"] = exposure_time_samples / sample_freq_hz

#Calculate sweep time
sweep_time_sec = run_dict["exposure_time_sec"] + run_dict["settle_time_sec"]
sweep_time_samples = int(round(sweep_time_sec * sample_freq_hz))
run_dict["sweep_time_sec"] = sweep_time_samples/sample_freq_hz

#Calculate camera settings
camera_exposure_time_percent = round(run_dict["exposure_time_sec"]/float(run_dict["sweep_time_sec"])*100,2)

#Calculate ETL ramp/fall percentages
run_dict["etl_l_ramp_rising_%"] = run_dict["etl_l_ramp_falling_%"] = round(camera_exposure_time_percent/2.,2)

#Calculate laser settings
run_dict["laser_pulse_%"] = camera_exposure_time_percent

############################
## SET INITIAL PARAMETERS ##
############################
startup = {
    'state' : 'init', # 'init', 'idle' , 'live', 'snap', 'running_script'
    'samplerate' : sample_freq_hz,
    'sweeptime' : run_dict["sweep_time_sec"],
    'position' : {'x_pos':0,'y_pos':0,'z_pos':0,'f_pos':0,'theta_pos':0}, #Don't believe this actually does anything...
    'ETL_cfg_file' : 'config/etl_parameters/ETL-parameters-benchtop.csv',
    'folder' : 'C:/Users/labuser/Desktop/data/',
    'snap_folder' : 'C:/Users/labuser/Desktop/data/',
    'file_prefix' : '',
    'file_suffix' : '000001',
    'zoom' : '5x',
    'pixelsize' : 0.92,
    'laser' : '532 nm',
    'max_laser_voltage':5,
    'intensity' : 5,
    'shutterstate':False, # Is the shutter open or not?
    'shutterconfig':'Left', # Can be "Left", "Right","Both","Interleaved"
    'laser_interleaving':False,
    'filter' : 'Empty',
    'etl_l_delay_%' : 0,
    'etl_l_ramp_rising_%' : run_dict["etl_l_ramp_rising_%"],
    'etl_l_ramp_falling_%' :  run_dict["etl_l_ramp_falling_%"],
    'etl_l_amplitude' : 0.34,
    'etl_l_offset' : 3.65,
    'etl_r_delay_%' : 0,
    'etl_r_ramp_rising_%' : 100,
    'etl_r_ramp_falling_%' : 0,
    'etl_r_amplitude' : 0.37,
    'etl_r_offset' : 3.6,
    'galvo_l_frequency' : run_dict['galvos_freq'],
    'galvo_l_amplitude' : 0.55,
    'galvo_l_offset' : 0.08,
    'galvo_l_duty_cycle' : galvos_duty_cycle,
    'galvo_l_phase' : galvos_phase,
    #There is some bug where the right galvos frequency is messing with the software even when disabled...
    'galvo_r_frequency' : run_dict['galvos_freq'],
    'galvo_r_offset' : 0,
    'galvo_r_duty_cycle' : galvos_duty_cycle,
    'galvo_r_phase' : galvos_phase,
    'laser_l_delay_%' : 0,
    'laser_l_pulse_%' : run_dict["laser_pulse_%"],
    'laser_l_max_amplitude_%' : 100,
    'laser_r_delay_%' :  0,
    'laser_r_pulse_%' :  99,
    'laser_r_max_amplitude_%' : 100,
    'camera_delay_%' : 0,
    'camera_pulse_%' : 1,
    'camera_exposure_time': run_dict['exposure_time_sec'],
    'camera_line_interval':0.000075, # Hamamatsu-specific parameter, not needed in area mode
    'camera_display_live_subsampling': 1, # un-deprecated for older computers
    'camera_display_acquisition_subsampling': 1, # un-deprecated for older computers  
    'camera_display_temporal_subsampling': 1, # newly added for performance and stability boost
    'camera_binning':'1x1',
    'camera_sensor_mode':'Area', # Hamamatsu-specific parameter
    'average_frame_rate': 4.5,
}
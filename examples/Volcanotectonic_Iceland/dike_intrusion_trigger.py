# -*- coding: utf-8 -*-
"""
This script runs Trigger for the Iceland dike intrusion example.

"""

from quakemigrate import Trigger
from quakemigrate.io import read_lut

# --- i/o paths ---
lut_file = "./outputs/lut/dike_intrusion.LUT"
run_path = "./outputs/runs"
run_name = "example_run"

# --- Set time period over which to run trigger ---
starttime = "2014-08-24T00:01:00.0"
endtime = "2014-08-24T00:11:00.0"

# --- Load the LUT ---
lut = read_lut(lut_file=lut_file)

# --- Create new Trigger ---
trig = Trigger(lut, run_path=run_path, run_name=run_name, log=True,
               loglevel="info")

# --- Set trigger parameters ---
# For a complete list of parameters and guidance on how to choose them, please
# see the manual and read the docs.
trig.marginal_window = 1.0
trig.min_event_interval = 2.0
trig.normalise_coalescence = True

# --- Static threshold ---
trig.threshold_method = "static"
trig.static_threshold = 1.45

# --- Dynamic (Median Absolute Deviation) threshold ---
# trig.threshold_method = "dynamic"
# trig.mad_window_length = 300.
# trig.mad_multiplier = 5.

# --- Toggle plotting options ---
trig.xy_files = "./inputs/XY_FILES/dike_xyfiles.csv"

# --- Run trigger ---
trig.trigger(starttime, endtime, savefig=True,
             region=[-17.0, 64.7, 0.0, -16.7, 64.9, 15.0])

# -*- coding: utf-8 -*-
"""
This script runs the detect stage for the Iceland dike intrusion example.

"""

from quakemigrate import QuakeScan
from quakemigrate.io import Archive, read_lut, read_stations
from quakemigrate.signal.onsets import STALTAOnset

# --- i/o paths ---
station_file = "./inputs/iceland_stations.txt"
data_in = "./inputs/mSEED"
lut_file = "./outputs/lut/dike_intrusion.LUT"
run_path = "./outputs/runs"
run_name = "example_run"

# --- Set time period over which to run detect ---
starttime = "2014-08-24T00:01:00.0"
endtime = "2014-08-24T00:11:00.0"

# --- Read in station file ---
stations = read_stations(station_file)

# --- Create new Archive and set path structure ---
archive = Archive(archive_path=data_in, stations=stations,
                  archive_format="YEAR/JD/STATION")

# --- Load the LUT ---
lut = read_lut(lut_file=lut_file)
lut.decimate([2, 2, 2], inplace=True)

# --- Create new Onset ---
onset = STALTAOnset(position="classic")
onset.p_bp_filter = [2, 16, 2]
onset.s_bp_filter = [2, 16, 2]
onset.p_onset_win = [0.2, 1.0]
onset.s_onset_win = [0.2, 1.0]

# --- Create new QuakeScan ---
scan = QuakeScan(archive, lut, onset=onset, run_path=run_path,
                 run_name=run_name, log=True, loglevel="info")

# --- Set detect parameters ---
scan.sampling_rate = 50
scan.timestep = 300.
scan.threads = 12

# --- Run detect ---
scan.detect(starttime, endtime)

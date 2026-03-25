# CMS ECAL Barrel APD High-Voltage Prototype Analysis

## Project Overview
This repository contains the Python-based data processing pipeline used to characterise High-Voltage (HV) system prototypes for the **CMS ECAL Barrel APD** upgrade at CERN. The scripts automate the conversion of raw hardware monitoring logs into structured ROOT files for stability and precision analysis.

## Key Features
*   **Data Parsing:** Converts raw experimental log data (`.txt`) into `TTree` structures for efficient storage.
*   **Time-Series Monitoring:** Tracks Voltage, Temperature, Vmon, and Imon over extended stability tests.
*   **Statistical Analysis:** Calculates mean, standard deviation (RMS), and peak-to-peak fluctuations.
*   **Visualisation:** Generates high-resolution time-series plots and distribution histograms using **PyROOT**.

## Technical Stack
*   **Language:** Python
*   **Frameworks:** ROOT (PyROOT), NumPy, Statistics
*   **Data Source:** CAEN SY4527 HV System log exports

## How to Use
1. Ensure `ROOT` is installed in your environment.
2. Place your raw data in `prototype.txt`.
3. Run the script: `python analysis_script.py`
4. Results will be saved as `Prototype_voltage_vs_time.png` and `Prototype_voltage_distribution.png`.

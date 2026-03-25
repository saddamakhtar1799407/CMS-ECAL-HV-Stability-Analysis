# CMS ECAL Barrel APD High-Voltage Prototype Analysis

## Project Overview
This repository contains the Python-based data processing and analysis pipeline developed for my Master's thesis at **Sapienza University of Rome**. The project focuses on the study and characterisation of the new High-Voltage (HV) system prototypes (Prototypes 0–3) for the **CMS Electromagnetic Calorimeter (ECAL)** upgrade for the **High-Luminosity LHC (HL-LHC)**.

The scripts automate the conversion of raw hardware monitoring logs from **CAEN SY4527** mainframes into structured **CERN ROOT** files to verify that voltage stability meets the strict requirements (±65 mV) for Avalanche Photodiode (APD) biasing.

## Key Features
*   **High-Resolution Data Parsing:** Extracts and synchronises `VmeT` (multimeter measurements), `VMon`, `IMon`, and temperature data from ASCII log files.
*   **Stability Verification:** Performs long-term stability analysis (over 6-month periods) to monitor voltage fluctuations and drift.
*   **Statistical Characterisation:** Uses **PyROOT** to calculate mean voltage, Standard Deviation (RMS), and peak-to-peak fluctuations with millivolt precision.
*   **Environmental Correlation:** Tools to study the impact of temperature variations and day-night oscillations on HV board performance.

## Technical Stack
*   **Language:** Python
*   **Analysis Framework:** PyROOT (CERN ROOT interface)
*   **Libraries:** NumPy, Statistics, Time
*   **Hardware Interface:** CAEN SY4527 Crate, HP 3145 Multimeter

## How to Use
1.  **Environment:** Ensure [CERN ROOT](https://root.cern) is installed and configured in your Python environment.
2.  **Input Data:** Place the raw timestamped experimental logs into a file named `prototype.txt`.
3.  **Run Analysis:** Execute the main script:
    ```bash
    python analysis_script.py
    ```
4.  **Outputs:** 
    *   `Prototype.root`: Structured TTree containing all experimental channels.
    *   `Prototype_voltage_vs_time.png`: Time-series stability plot.
    *   `Prototype_voltage_distribution.png`: Voltage frequency histogram with RMS values.

## Research Context
This work was conducted in collaboration with the **CMS Rome Group** and **INFN**. The characterisation of these HV prototypes is critical for maintaining a stable APD gain of 50, ensuring optimal energy resolution for the CMS detector during the high-radiation environment of LHC Phase II.

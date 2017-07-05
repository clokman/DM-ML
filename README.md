# DM-ML

This is the project repository for Data Mining Techniques and Machine Learning for Quantified Self courses of Vrije Uniersiteit Amsterdam.

The repository also contains the "Prepocessor" package — a Python package for data manipulation and preprocessing. Preprocessor allows datasets to be stored as nested lists and contains various dataset modification functions. Due to its list-based approach, it offers an alternative approach to numpy. 


# DM 
Files:
- "Step_1-Preparation_pipeline.ipynb" takes input data from "data/original_data" directory, preprocesses it, and outputs it to "data" directory.
- "Step_2-Data_merger.ows" merges two datasets used in the project.
- "Step_3-Analysis_pipeline_v3.1" performs the main analysis on the merged dataset.

The three files (step 1, step 2 and step 3) are used sequentially to mine and analyze the data. However, it is possible to run each file individually. If the interest is on the main analysis, it can be directly ran by executing step 3.

The data can also be directly viewed under the data directory, and the file used for main analyses is the "merged_vX.X.csv"

Requirements:
- Please use Python 3.6 or higher.

- Please note that .ows files requires [Orange 3.4.1](https://orange.biolab.si/) to run. This package can also be conveniently installed using [Anaconda IDE](https://www.continuum.io/downloads).

# ML
ml4qs_preprocessing.py and ml4qs_data_sleep_levels.py are the two main files used for analyis.

ml4qs_sleep_level_binarization is an extra step taken in feature creation.
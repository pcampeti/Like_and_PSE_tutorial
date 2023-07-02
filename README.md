# Like_and_PSE_tutorial
Tutorial on CMB power spectrum estimation, likelihood and parameter estimation for LiteBIRD hands-on meeting in Japan, Summer 2023.

## To use it:
1. Download this repository as .zip file (click on green "Code" button below the name of the repository and select "Download ZIP").
2. Unzip xQML-master/ folder.
3. In ancillary_files/ folder, unzip mask.zip file.
4. Download transfer.zip file from the WeTransfer link I provided on Slack, unzip it and put it in the ancillary_files/ folder.
5. I recommend to install xQML package (see instructions below) in a separate conda environment (let's call it "xqml_env"). You will run the xQML_tutorial.ipynb in this environment.
6. I recommend to create a different conda environment (let's call it "namaster_env") and install all packages required to run the NaMaster_tutorial.ipynb and Likelihood_tutorial.ipynb in this environment (see instructions below).

### xqml_env
1. Create a conda environment with python 3.6.13 (tested) e.g. with the command "conda create -n xqml_env python=3.6.13"
2. cd xQML-master
3. pip install .
4. it will fail: install required dependencies until it works (there should be only a couple easy to install dependencies such as numpy, matplotlib...which you can easily install with "conda install numpy" etc.)

### namaster_env
1. Create a conda environment with python 3.7.3 (tested) e.g. with the command "conda create -n namaster_env python=3.7.3"
2. conda install -c conda-forge namaster
3. Install other dependencies required (e.g. healpy, numpy, matplotlib, seaborn, numba, iminuit...)





# Like_and_PSE_tutorial
Tutorial on CMB power spectrum estimation, likelihood and parameter estimation for LiteBIRD hands-on meeting in Japan, Summer 2023.

The xQML_tutorial.ipynb and NaMaster_tutorial.ipynb notebooks implement respectively QML and pseudo-Cls power spectrum estimation in a simple CMB + white noise case.

Likelihood_tutorial.ipynb implements a simple parameter estimation routine for tensor-to-scalar ratio based on the offset Hamimeche & Lewis likelihood.


### Disclaimer
The xQML-master folder in this repository contains a slighlty modified version of the xQML package by Vanneste et al. 2018 (https://arxiv.org/abs/1807.02484). The original repository can be found at https://gitlab.in2p3.fr/xQML/xQML.

Disclaimer: this repository contains code copied and/or heavily inspired by the LolliPoP code (https://github.com/planck-npipe/lollipop/tree/master), presented in https://arxiv.org/abs/1605.03507 and https://arxiv.org/abs/2010.01139, from the xQML package (https://gitlab.in2p3.fr/xQML/xQML) and from the FGBuster package (https://github.com/fgbuster/fgbuster).


## How to use it:
1. Download this repository as .zip file (click on green "Code" button below the name of the repository and select "Download ZIP").
2. Unzip xQML-master/ folder.
3. In ancillary_files/ folder, unzip mask.zip file.
4. Download transfer.zip file from this WeTrasfer link https://we.tl/t-7X7bFO4lGh (expires on July 9th), unzip it and put it in the ancillary_files/ folder.
5. I recommend installing the xQML package (see instructions below) in a separate conda environment (let's call it "xqml_env"). You will run the xQML_tutorial.ipynb in this environment.
6. I recommend creating a different conda environment (let's call it "namaster_env") and install there all packages required to run the NaMaster_tutorial.ipynb and Likelihood_tutorial.ipynb (see instructions below).
7. You should first run the xQML_tutorial.ipynb and NaMaster_tutorial.ipynb notebooks. Then you can run the Likelihood_tutorial.ipynb notebook, which uses spectra produced and saved by the first two notebooks.

### xqml_env
1. Create a conda environment with python 3.6.13 (tested) e.g. with the command "conda create -n xqml_env python=3.6.13"
2. cd xQML-master
3. pip install .
4. it will fail: python will complain that some packages are missing, you should install required dependencies until "pip install ." works (there should be only a couple easy to install dependencies such as numpy, cython, matplotlib, ipykernel...which you can easily install with "conda install numpy" etc.). C compilers (gcc) may also be an issue especially if you install on Mac laptop, I recommend installing on Linux (e.g. on your favourite computer cluster, such as NERSC...)

### namaster_env
1. Create a conda environment with python 3.7.3 (tested) e.g. with the command "conda create -n namaster_env python=3.7.3"
2. conda install -c conda-forge namaster
3. Install other dependencies required (e.g. healpy, numpy, matplotlib, seaborn, numba, iminuit, ipykernel...)





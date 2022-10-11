# Instructions for running pain.py

Operating System: Ubuntu 20.04.3 LTS
Kernel: Linux 5.15.0-48-generic

Python 3.9.13

The **Anaconda** Python distribution must be **installed** first!

In the *terminal*, **create** a local environment for **python=3.10** called *env_pain3_10*.

`conda create -n env_pain3_10 python=3.10`

**Activate** the *env_pain3_10* environment  

`conda activate env_pain3_10`

**Install** all required **modules** specified in the *requirements.txt* file

`pip install -r requirements.txt`

Run pain.py with the command

`python3 pain.py`

**Deactivate** the environment after *working* with the script

`conda deactivate`


##### Additional instructions in case the script does not run

The *requirements.txt* contains the **minimum** number of unnecessary dependencies.
If the script does not run, try installing the required modules from the *requirements_full.txt* which contains the **full** list of modules.

`pip install -r requirements_full.txt`


**If the problem persists**, try installing the required modules **manually** using this list of commands *before* runing pain.py.

`pip install --upgrade google-api-python-client`

`pip install kivy`

`pip install bs4`

`pip install biopython`

`pip install aiohttp`

`pip install pandas`

`pip install scipy`

`pip install scanpy`

`pip install opencv_python`

`pip install lxml`


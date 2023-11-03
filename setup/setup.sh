# /bash
# a bash script to setup the environment for the project

# install pip3 and virtualenv
sudo apt-get install python3-pip -y

# create the virutual environment in the project root
pip3 install virtualenv
virtualenv -p python3 DataScienceFinal

# activate the virtual environment
source DataScienceFinal/bin/activate

# install packages you will need
pip3 install -r setup/requirements.txt
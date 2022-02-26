# Install Anaconda
- Link [Here](https://www.anaconda.com/products/individual)


# Install VirtualEnv
- Once Anaconda is installed, test installation in terminal by running `conda --version`

- If that is working, then install virtualenv with the command `pip install virtualenv`


# Create VirtualEnv
- Go to Projects Folder
- Run `virtualenv venv`
    - This will create a folder called `venv`

# Activate VirtualEnv
- After installing and identifying the folder `venv`
- Run `source venv/bin/activate` - For Mac
- Run `venv/Scripts/activate.bat` - For Windows

# All done!
- Make sure this is activated before installing any libraries using `pip`. 
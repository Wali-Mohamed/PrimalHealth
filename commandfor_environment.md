# Install Pipenv
pip install pipenv

# Initialize a New Pipenv Environment
pipenv install

To create a new environment using Pipenv, follow these steps:

Step 1: Install Pipenv
First, ensure that Pipenv is installed on your system. You can install it using pip:

bash
Copy code
pip install pipenv
Step 2: Create a New Project Directory
Navigate to the directory where you want to create your new Python project or create a new directory for it:

bash
Copy code
mkdir my_project
cd my_project
Replace my_project with your desired project name.

Step 3: Initialize a New Pipenv Environment
To create a new environment, you can run the following command:

bash
Copy code
pipenv install
This command initializes a new Pipenv environment in your project directory:

Creates a Virtual Environment: Pipenv will automatically create a virtual environment for your project if one does not already exist. The virtual environment will be located in a centralized directory (e.g., .local/share/virtualenvs on Linux) or within the project directory, depending on your configuration.
Creates a Pipfile: This file lists your project's dependencies and other metadata.
Creates a Pipfile.lock: This file will be created when you add or install packages, capturing the exact versions of dependencies.


When to Use pipenv shell
If you want to work interactively within the Pipenv-managed environment (e.g., running Python scripts or commands), you can use:

bash
Copy code
to check python version
pipenv shell


pipenv run python --version

Update the Environment:

After modifying the Pipfile, you need to update the environment. Run:
bash
Copy code
pipenv --python 3.10
This command tells Pipenv to create or update the virtual environment using Python 3.10. If Python 3.10 is not already installed on your system, Pipenv will try to find and use it. Make sure Python 3.10 is installed and available on your PATH.

Reinstall Dependencies:

To ensure that all dependencies are installed correctly with the new Python version, you may need to regenerate the Pipfile.lock file by running:
bash
Copy code
pipenv lock


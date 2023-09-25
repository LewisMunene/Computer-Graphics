# Codelabs Documentation

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)

## Features<a name="features"></a>

This project is designed to perform various tasks related to student data processing and analysis. Here are the key features of the project:

1. **Data Import**: Import student data from an Excel (.xlsx) file.

2. **Email Address Generation**: Generate email addresses for students following specific formatting rules:
    - Format: `FLastName@gmail.com` e.g. Juma Hussein becomes jhussein@gmail.com
    - Unique email addresses for each student.
    - Removal of special characters from names.

3. **Project Structure**: Maintain a well-organized project structure, including key files and directories:
    - `main.py`: The main program file.
    - `functions.py`: Contains project functions and utilities.
    - `constraints.py`: Stores project constraints and constants.
    - `logs/`: Directory to save computation log files.
    - `output/`: Directory to store output files in both TSV and CSV formats.

4. **Gender Separation**: Separate students into male and female lists and log the count of each gender.

5. **Special Character Handling**: Identify and clean names with special characters using regular expressions.

6. **Similarity Analysis**: Perform a similarity analysis on male names vs. female names and save results in a JSON file, considering a 50% similarity threshold.

7. **Document Merging**: Merge student documents into one file, shuffle the names once, and save as JSON and JSONL files.

8. **Google API Integration**: Utilize Google API for cloud storage to backup project files in Google Drive.

## Installation<a name="installation"></a>

To set up and run the school mini-project, follow these installation steps:

1. Create a Python virtual environment (e.g., using `venv` or `conda`) and activate it:

   ```bash
   python -m venv school_project_env
   source school_project_env/bin/activate  # On Windows, use `school_project_env\Scripts\activate`
   ```

2. Install project dependencies by running the following command in your virtual environment:

   ```bash
   pip install pandas numpy tensorflow labse google-api-python-client
   ```
   or you can install using the requirements.txt file using the code below.
    
    ```bash
    pip install -r requirements.txt
    ```

   Note: TensorFlow may require a Python downgrade to avoid compatibility issues.

3. Download the test data file provided in the `.xlsx` format and place it in your project directory.

4. Organize your project structure as described in the documentation.

## Usage<a name="usage"></a>

Once you have installed the necessary dependencies and organized your project, you can run the school mini-project by following these steps:

1. Run the main program file:

   ```bash
   python main.py
   ```

2. The program will perform various tasks as outlined in the features section.

3. The generated output files, logs, and analysis results will be stored in the `output/` directory and `logs/` directory, respectively.

4. Ensure that you have a Google API key for cloud storage, and the project will back up files to Google Drive.
# Mowito_assignment

**Environment Setup**
  - Make sure you have virtualenv if not install `pip install virtualenv`
  - In Mowito run `virtualenv venv`  _venv_ folder should be created
  - Navigate to Mowito/venv/local/bin and open terminal
  - Enter `. activate` and now venv environment will be activated
  - ![Screenshot from 2024-05-15 16-46-01](https://github.com/Tr0612/Mowito_assignment/assets/45840572/a6ada094-2b4f-480d-a79c-068dc87c2b11)
  - ![Screenshot from 2024-05-15 19-23-08](https://github.com/Tr0612/Mowito_assignment/assets/45840572/3996e7c7-9188-466d-9d11-0d7b4fdd5526)
  - Go back to Mowito directory in the same terminal
  - Run `pip install -r requirements.txt`
  - Necessary packages would be installed

**Running the program, if already Detectron2 is initialized**
  - In the same terminal enter `python3 main.py`
  - You would be prompted to enter input of 2 image paths.
  - Paste the image path as below
  - ![Screenshot from 2024-05-15 15-46-17](https://github.com/Tr0612/Mowito_assignment/assets/45840572/717e1315-cd0e-4ddc-8996-6fa2db9a72ef)
  - **NOTE:** Don't add space before adding the path, this will lead to error

**SAMPLE OUTPUT**

![Template_1_output](https://github.com/Tr0612/Mowito_assignment/assets/45840572/fe48bf38-5888-4941-9627-e54656083778)

**Setting up Detectron2**
  - Open _mowito-detection.ipynb_  and run first 3 cells and 5th cell , so that detectron2 is setup
  - Adding the weights, download the weights from this link [WEIGHTS FILE](https://drive.google.com/file/d/1ERtfLBxr_i9JJ3AZ1_Y4fc4e6BaC8hMS/view?usp=sharing) and add to mowito directory
  - In 6th cell update the path to weight file
  - ![image](https://github.com/Tr0612/Mowito_assignment/assets/45840572/b59e88c6-58a9-4a3b-998f-0dd248a131a6)

  - 

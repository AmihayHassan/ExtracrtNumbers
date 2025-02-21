# ExtracrtNumbers

simple script to extract all the numbers from XML file into Excel file

## How to use?

### On your Android device:

1. Download the app from Google Play
   Store [Call Logs Backup](https://play.google.com/store/apps/details?id=com.loopvector.allinonebackup.calllogsbackup)
2. Create a backup of your call logs using the app,
   <br>
   a new file will be created in your phone storage, with `.aiob` extension.
3. Rename the file to `call_history.xml`
4. Move the file to your computer in any way you like (e.g. USB Cable, Email, WhatsApp, etc.)

### On your computer:

1. Make sure your computer has Python installed, if not, you can download it
   from [here](https://www.python.org/downloads/)
2. Clone this repository to your local machine by running the following command in your terminal:

```bash
git clone https://github.com/AmihayHassan/ExtracrtNumbers.git
```
or by downloading the project as `.zip` archive.

3. Install the required packages by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

4. Move the `call_history.xml` file to the cloned repository folder
5. Run the `main.py` script by running the following command in your terminal:

```bash
python main.py
```

6. Two new Excel files will be created in the "output" folder:
    - `phone_numbers_freq.xlsx` - with 2 columns: 
      - `Phone Number` - the phone numbers from the XML file (unique)
      - `Frequency` - the number of times the phone number appeared in the XML file
   
    - `phone_numbers.xlsx` - with 1 column:
      - `Phone Number` - the phone numbers from the XML file (unique)
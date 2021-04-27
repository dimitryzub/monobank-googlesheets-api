# Personal Financial Tracker using [Monobank API](https://api.monobank.ua/docs) and [Google Sheets API for Python](https://developers.google.com/sheets/api/quickstart/python)

### Preparation:
- Go to [Console Google Cloud](https://console.cloud.google.com/home/).
- Go to API's and Services --> Library. Find Google Sheets API and **Enable** it. Or use [direct link](https://console.cloud.google.com/apis/library/sheets.googleapis.com?q=sheets&id=739c20c5-5641-41e8-a938-e55ddc082ad1&project=monobank-311911).
- Go to Credentials and hit Create New Credentials. Once you come to _"Grant this service account access to project"_ setting, choose **Editor** role. Next step is optional.
- After newly created credentials you should see them under Service Accounts. Click on email --> Keys --> Add Key --> Create New Key --> Type: JSON (_file will be downloaded_)
- Put this file in the same directory where .py file is located or use `os` to locate the file path.

After that:
- Create Google Sheet or use existing.
- In the access settings, choose email that was created earlier in Console Google Cloud.


### Usage:

Lines below located in the `main.py` 
- `SERVICE_ACCOUNT_FILE = 'keys.json'` --> Change to the JSON that was downloaded earlier. Check if filename is the same. Rename if needed.
- `SAMPLE_SPREADSHEET_ID` = `'your spreadsheet id'` --> (`https://docs.google.com/spreadsheets/d/**YOUR_SPREADSHEET_ID**/edit#gid=0`)

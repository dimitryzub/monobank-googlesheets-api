# Personal Financial Tracker using Monobank API and Google Sheets API for Python

### Preparation:
- Go to [Console Google Cloud](https://console.cloud.google.com/home/).
- Go to API's and Services --> Library. Find Google Sheets API and **Enable** it. Or use [direct link](https://console.cloud.google.com/apis/library/sheets.googleapis.com?q=sheets&id=739c20c5-5641-41e8-a938-e55ddc082ad1&project=monobank-311911).
- Go to Credentials, hit Create New Credentials. Once at _"Grant this service account access to project"_ setting, choose **Editor** role. Next step is optional.
- After newly created credentials you should see them under Service Accounts. Click on email --> Keys --> Add Key --> Create New Key --> Type: JSON (_file will be downloaded_)
- Put this file in the same directory where `.py` file is located or use `os` to locate the file path.

After that:
- Create Google Sheet or use existing.
- In the access settings, choose email that was created earlier in Console Google Cloud.
- Paste code from this repo.

### Usage:

Lines below located in the `main.py` 
- `SERVICE_ACCOUNT_FILE = 'keys.json'` --> Change to the JSON that was downloaded earlier. Check if filename is the same. Rename if needed.
- `SAMPLE_SPREADSHEET_ID` = `'your spreadsheet id'` --> (`https://docs.google.com/spreadsheets/d/**YOUR_SPREADSHEET_ID**/edit#gid=0`)

You can replace Monobank API code to the bank you're using.

### Example output:

![example_spreadsheet_output](https://user-images.githubusercontent.com/78694043/116234954-ee828a00-a765-11eb-92c2-fb37c4ce27f1.jpg)

Libraries used:
- [Requests](https://github.com/psf/requests)
- [ISO 4217 (Currency)](https://github.com/ikseek/iso_4217)
- [ISO 18425 (Merchant Categories)](https://github.com/jleclanche/python-iso18245)
- [Python-Ftfy](https://github.com/LuminosoInsight/python-ftfy)

### Links: 
- [Google Sheets Python API Quickstart](https://developers.google.com/sheets/api/quickstart/python)
- [Basic Writing to Google Sheets](https://developers.google.com/sheets/api/samples/writing)
- [Monobank API](https://api.monobank.ua/docs)

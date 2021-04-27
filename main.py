# Unix time - https://www.unixtimestamp.com/index.php
# ISO 4217 (Currency) - https://pypi.org/project/iso-4217/
# ISO 18425 (Merchant Categories) - https://github.com/jleclanche/python-iso18245
# Python-Ftfy (Fix unicode) - https://github.com/LuminosoInsight/python-ftfy
# Google Sheets API - https://developers.google.com/sheets/api

import requests
import iso18245
from iso_4217 import Currency
from datetime import datetime
from ftfy import fix_encoding

from googleapiclient.discovery import build
from google.oauth2 import service_account

headers = {"X-Token": "YOUR MONOBANK API TOKEN"}

account = "0"
from_date = "1617245168"   # Date from current UNIX Time
to_date = "1619504025"     # Current UNIX Time.

response = requests.get(f'https://api.monobank.ua/personal/statement/{account}/{from_date}/{to_date}', headers = headers)
data = response.json()
data.reverse()

for info in data:
    mcc = str(info['mcc'])
    try:
        merchant_category = fix_encoding(iso18245.get_mcc(mcc).usda_description)
    except:
        merchant_category = None
    description = info['description']
    try:
        comment = info['comment']
    except:
        comment = None

    current_balance = int(info['balance'] / 100)
    operation_amount = int(info['operationAmount'] / 100)
    cashback_amount = info['cashbackAmount'] / 100
    fee_amount = info['commissionRate'] / 100
    # currency_code = info['currencyCode']
    # currency = Currency(currency_code)

    operation_time = info['time']
    converted_time = datetime.fromtimestamp(operation_time)
    time_date = str(converted_time).split(' ')[0]
    time_hours = str(converted_time).split(' ')[1]
    transaction_id = info['id']
    try:
        receipt_id = info['receiptId']
    except:
        receipt_id = None

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']   # https://developers.google.com/sheets/api/guides/authorizing#OAuth2Authorizing --> SCOPES for more info
    SERVICE_ACCOUNT_FILE = 'keys.json'                          # JSON filename that was downloaded from Console Google Cloud

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes = SCOPES)

    SAMPLE_SPREADSHEET_ID = 'YOUR SPREADSHEET ID'
    service = build('sheets', 'v4', credentials = creds)
    sheet = service.spreadsheets()

    # Write to the spreadsheet
    test_range = [[transaction_id], [time_date], [time_hours], [current_balance], [merchant_category],
                  [operation_amount], [cashback_amount], [fee_amount], [description],
                  [comment], [receipt_id]]

    request = service.spreadsheets().values().append(spreadsheetId = SAMPLE_SPREADSHEET_ID,
                                                     range = "Spreadsheet_name!Spreadsheet_range(example: A1:C9)", valueInputOption = "USER_ENTERED",
                                                     body = {"majorDimension": "COLUMNS",    # https://developers.google.com/sheets/api/samples/writing
                                                             "values": test_range}).execute()
    print(f'Writing: {request}')


    # Read from the spreadsheet (get rid if not needed)
    # result = sheet.values().get(spreadsheetId = SAMPLE_SPREADSHEET_ID,
    #                             range = "Spreadsheet_name!Spreadsheet_range (example: A1:C9)").execute()
    # values = result.get('values', [])

    
    
    # Test prints (get rid of them if not needed):
    # print(merchant_category)
    # print(description)
    # print(comment)
    # print(time_date)
    # print(time_hours)
    # print(transaction_id)
    # print(receipt_id)
    # print(current_balance)
    # print(operation_amount)
    # print(cashback_amount)
    # print(fee_amount)
    # print(currency)

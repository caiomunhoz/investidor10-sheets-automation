from google_sheets.reader import read_spreadsheet

def main():
    values = read_spreadsheet(spreadsheet_range='LANÇAMENTOS!A2:F20')
    print(values)

if __name__ == '__main__':
    main()

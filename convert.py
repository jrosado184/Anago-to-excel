import os
import pandas

TEXT_FILE = r'C:\Users\Javy\Documents\Anago_Knife_Scores.txt'
EXCEL_FILE = r'C:\Users\Javy\Documents\Anago_Knife_Scores.xlsx'

def convert_text_to_exel() -> bool:
    if os.path.exists(TEXT_FILE):
        try:
            knife_scores = pandas.read_csv(TEXT_FILE, delimiter='\s+', header=None)
            knife_scores.to_excel(EXCEL_FILE, index=False)
            print("Successfully converted file to excel")
            return True
        except Exception as e:
            print("Failed to convert file to excel", {e})
            return False
    else:
        print("Text file not found")
        return False
    
        
        
def remove_text_file() -> None:
    if os.path.exists(EXCEL_FILE):
        try:
            os.remove(TEXT_FILE)
        except Exception as e:
            print("Failed to remove text file", {e})
    else:
        print("Excel file not found")
        
        
def main() -> None:
    convert_text_to_exel()

if __name__ == '__main__':
    main()
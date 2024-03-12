import pandas

data = pandas.read_csv(r'C:\Users\javie\OneDrive\Desktop\convert.txt', delimiter='\s+', header=None)

data.to_excel(r'C:\Users\javie\OneDrive\Desktop\convert.xlsx', index=False)

if __name__ == '__name__':
 print(data)
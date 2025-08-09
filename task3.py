import pandas as pd
#task3: outdated/problematic data detection
#since the dataset contains (dated,numeric,categorical) data, so i will applay all of them

#1 outdated dates detection:
def outdated_dates_detection(dataset,date_col):
    DCS = pd.read_csv(dataset)
    DCS[date_col] = pd.to_datetime(DCS[date_col],errors='coerce')
    today = pd.Timestamp.today()

    oldest_date = DCS[date_col].min()
    newest_date = DCS[date_col].max()
    print(oldest_date,newest_date)

    after_today = DCS[DCS[date_col] > today]
    old_days = DCS[DCS[date_col] < pd.Timestamp('2023-1-1')]
    print(after_today,old_days)
print(outdated_dates_detection('dirty_cafe_sales.csv','Transaction Date'))



#2 numeric outliers detection 
"""#i will use IQR rule to detect outliers
def numeric_outliers(dataset,num_column):
    DCS = pd.read_csv(dataset)
    DCS['Total Spent'] = pd.to_numeric(DCS['Total Spent'], errors='coerce').astype('Int32')

    Q1 = DCS[num_column].quantile(0.25)
    Q3 = DCS[num_column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = DCS[(DCS[num_column] < lower_bound) | (DCS[num_column] > upper_bound)]
    return outliers

ss = numeric_outliers('dirty_cafe_sales.csv', "Total Spent")"""

#3 invalid categories detection
def invalid_categories(dataset,cat_column,categories):
    CDS = pd.read_csv('dirty_cafe_sales.csv')
    CDS[cat_column] = CDS[cat_column].str.strip().str.lower()
    
    invalid = CDS[~CDS[cat_column].isin([c.lower() for c in categories])]
    return invalid


valid_products = ["coffee", "salad", "sandwich", "cake",'juice','cookie','smoothie','tea']
invalid_rows = invalid_categories('dirty_cafe_sales.csv', "Item", valid_products)
print(invalid_rows)
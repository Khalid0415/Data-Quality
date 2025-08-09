import pandas as pd

#task1: Missing Data Detection
def missing_data_detection(dataset):

    DCS = pd.read_csv(dataset)
    print(DCS)
    
    print(DCS.dtypes)
    print(DCS.describe())
    print(DCS.describe(include='object'))
    print(DCS.info())

    DCS.replace(['UNKNOWN','ERROR'],pd.NA,inplace=True)

    missy_col = DCS.iloc[:,1:-1]
    print(missy_col)

    mvalue_per_column = DCS.isnull().sum()
    print(mvalue_per_column)

    mpercentage_per_column = mvalue_per_column / len(DCS) * 100
    print(mpercentage_per_column)

    DCS['missing_row'] = DCS.isnull().sum(axis=1)
    most_missy_rows = DCS.sort_values(by='missing_row',ascending=False)
    print(most_missy_rows)

print(missing_data_detection('dirty_cafe_sales.csv'))

""" i can solve this problem by fill the missing value in more than one method
for example: fill missing value in categorical column such item column by most frequnt value
DCS['Item'] = DCS['Item'].fillna(DCS['Item'].mode()[0])"""
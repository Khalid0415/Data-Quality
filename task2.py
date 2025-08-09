import pandas as pd
def duplicate_detection(dataset):

    DCS = pd.read_csv(dataset)
    exact_duplicates = DCS[DCS.duplicated(keep=False)]
    print(exact_duplicates)

    potential_duplicates = DCS[DCS.duplicated(subset='Transaction ID',keep=False)]
    print(potential_duplicates)

    exact_duplicates_count = exact_duplicates.shape[0]
    print(exact_duplicates_count)

    potential_duplicates_count = potential_duplicates.shape[0]
    print(potential_duplicates_count)

    print(exact_duplicates.head())
    print(potential_duplicates.head())


    
print(duplicate_detection('dirty_cafe_sales.csv'))

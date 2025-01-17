# @Tomi Jolkkonen

import pandas as pd

# create data from csv, and put it to dataframe
def create_df():
    data = {
        "Product ID": ["P0001", "P0002", "P0003", "P0004", "P0005", "P0006", "P0007", "P0008", "P0009", "P0010", "P0011", "P0012", "P0013", "P0014", "P0015", "P0016", "P0017", "P0018", "P0019", "P0020", "P0020", "P0022", "P0023", "P0024", "P0025"],
        "Product Name": ["RXEFO", "GHERI", "VDIQP", "MDXQE", "EVMHN", "KTQVF", "FHTQN", "RXGQI", "NPDKU", "OHEJY", "XEFZV", "ONABK", "SRUPI", "RMAGZ", "XSYDO", "EDUPX", "YGPSD", "OCAHG", "EZIOZ", "BZLPX", "HETQL", "ARXKT", "AWFIB", "UXFLS", "IGLXO"],
        "Category": ["Books", "Home & Kitchen", "Toys & Games", "Toys & Games", "Toys & Games", "Books", "Books", "Clothing", "Clothing", "Sports", "Health & Beauty", "Books", "Electronics", "Electronics", "Electronics", "Sports", "Sports", "Toys & Games", "Books", "Clothing", "Clothing", "Clothing", "Toys & Games", "Home & Kitchen", "Sports"],
        "Price": [118.53, 340.24, 538.28, 191.38, 385.06, 802.11, 139.0, 610.49, 902.73, 567.32, 667.63, 150.84, 654.3, None, 136.37, 932.27, 991.49, 119.76, 972.42, 470.66, 365.26, 357.84, 880.93, 177.76, 936.66],
        "Discount (%)": [8, 19, 36, 47, 46, 6, 33, 13, 31, 21, 44, 41, 23, 36, 10, 37, 31, 19, 25, 20, 26, 1, 6, 43, 31],
        "Stock Quantity": [50, 9, 48, 91, 24, 61, 52, 47, 87, 65, 59, 7, 3, 25, 72, 7, 32, 89, 30, 41, 55, 28, 77, 90, 57],
        "Rating (out of 5)": [2.57, 3.68, 1.31, 4.63, 1.07, 3.91, 3.73, 2.15, 3.93, 2.07, 3.62, 4.44, 4.78, 1.52, 2.15, 3.12, 4.05, 2.47, 3.45, 4.66, 3.23, 4.55, 3.11, 2.09, 1.67],
        "Shipping Weight (lbs)": [2.57, 13.74, 14.89, 19.33, 1.85, 4.54, 10.63, 13.62, 4.6, 15.13, 14.4, 3.22, 9.94, 15.43, 11.31, 15.73, 4.02, 4.13, 15.55, 19.52, 1.76, 2.51, 2.11, 1.37, 9.94],
        "Color": ["Red", "White", "Red", "Red", "Red", "Green", "Green", "Green", "Blue", "Yellow", "Green", "White", "Black", "Black", "Black", "Blue", "Yellow", "Blue", "Blue", "Black", "Yellow", "White", "Blue", "Yellow", "Black"],
        "Material": ["Glass", "Fabric", "Metal", "Metal", "Fabric", "Wood", "Plastic", "Leather", "Metal", "Fabric", "Metal", "Fabric", "Fabric", "Metal", "Wood", "Wood", "Wood", "Leather", "Leather", "Plastic", "Wood", "Metal", "Leather", "Wood", "Glass"]
    }

    df = pd.DataFrame(data)
    return df

# removing columns Product ID, Produc Name, Discount (%), Stock Quantity, Rating (out of 5), Shipping Weight (lbs), Color
def drop_tables(df):
    dropped_tables = df.drop(columns=["Product ID", "Product Name", "Discount (%)", "Stock Quantity", "Rating (out of 5)", "Shipping Weight (lbs)", "Color"])
    return dropped_tables

# renaming  Price to AveragePrice
def rename_column(df):
    renamed_df = df.rename(columns={"Price": "AveragePrice"})
    return renamed_df

# grouping rows Category and Material, and calculate mean value from each row
def group_and_calculate(df):
    df = df.groupby(["Category", "Material"]).mean(numeric_only=True).reset_index()
    return df
    
# finalize by sorting dataset by Category and Material, and removing index column:
def finalize(df):
    df = df.sort_values(by=["Category", "Material"]).reset_index(drop=True)
    return df

# remove specific 2 rows from data: 
def remove_specific_rows(df):
    df_filtered = df  # Initialize df_filtered with the original df

    if "AveragePrice" in df.columns:
        condition1 = (df['Category'] == 'Clothing') & (df['Material'] == 'Wood') & (df['AveragePrice'] == 365.26)
        condition2 = (df['Category'] == 'Electronics') & (df['Material'] == 'Metal') & pd.isna(df['AveragePrice'])
        df_filtered = df[~(condition1 | condition2)]

    return df_filtered

def main():
    df = create_df()
    df_dropped_tables = drop_tables(df)
    df_renamed = rename_column(df_dropped_tables)
    df_cleaned = remove_specific_rows(df_renamed) 
    df_grouped_calculated = group_and_calculate(df_cleaned)
    df_final = finalize(df_grouped_calculated)
    print(df_final)  

if __name__ == "__main__":
    main()

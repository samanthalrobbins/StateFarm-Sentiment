import pandas as pd

def read_file(file):
    df = pd.read_csv(file)

    return df

def mobile_df(df):
    app_key = [" app ","application"," mobile ", "drive safe and save", "#drivesafeandsave", "drive safe", "smartphone", "iphone"]
    df = df[df["text"].str.contains("|".join(app_key))]
    return df

def constant_df(df):
    app_key = [" app ","application"," mobile ", "drive safe and save", "#drivesafeandsave", "drive safe", "smartphone", "iphone"]
    df = df[~df["text"].str.contains("|".join(app_key))]
    return df
    
def comm_df(df):
    app_key = ["commerical", "commercials", " ad ", "advertisement"]
    app_keymobile = [" app ","application"," mobile ", "drive safe and save", "#drivesafeandsave", "drive safe", "smartphone", "iphone"]
    df = df[~df["text"].str.contains("|".join(app_key))]
    df = df[~df["text"].str.contains("|".join(app_keymobile))]
    return df            
   
def main():
    df = read_file('removal.csv')
    mobiledf = mobile_df(df)
    constantdf = constant_df(df)
    commdf = comm_df(df)
    mobiledf.to_csv(r'mobile.csv', index = False)
    constantdf.to_csv(r'base.csv', index = False)
    commdf.to_csv(r'no_commerical_base.csv', index = False)
    
    #print(df)

if __name__ == '__main__':
    main()

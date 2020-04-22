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
    
def nd(df):
    tropicalstorm= ["landslide", "imelda","tropical storm","storm michael", "severe storms", "severe storm", "flooding", ]    
    hurricane = ["hurricane", "dorian","barry" ]
    earthquake =["earthquake" ]
    tornado = ["tornado"]
    df = df[df["text"].str.contains("|".join(tropicalstorm))]
    df = df[df["text"].str.contains("|".join(hurricane))]
    df = df[df["text"].str.contains("|".join(earthquake))]
    df = df[df["text"].str.contains("|".join(tornado))]
    return df           
   
def main():
    df = read_file('removal.csv')
    mobiledf = mobile_df(df)
    constantdf = constant_df(df)
    nddf = nd(df)
    mobiledf.to_csv(r'mobile.csv', index = False)
    constantdf.to_csv(r'base.csv', index = False)
    nddf.to_csv(r'naturaldisasters.csv', index = False)
    
    #print(df)

if __name__ == '__main__':
    main()

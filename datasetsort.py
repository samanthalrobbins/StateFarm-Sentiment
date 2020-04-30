import pandas as pd

def read_file(file):
    df = pd.read_csv(file, encoding='utf-8-sig')
    return df

'''
finds all the mobile application tweets
'''
def mobile_df(df):
    app_key = [" app ","application"," mobile ", "drive safe and save", "#drivesafeandsave", "drive safe", "smartphone", "iphone"]
    df = df[df.text.str.contains("|".join(app_key))]
    return df

'''
finds all the natural disaster tweets
'''
def nd_df(df):
    nd_key = ["landslide", "imelda","tropical storm","storm michael", "severe storms", "severe storm", "flooding", "flood","hurricane", "dorian","barry","fernand","earthquake","tornado","fire","damage", "disaster"]
    
    '''
    tropicalstorm= ["landslide", "imelda","tropical storm","storm michael", "severe storms", "severe storm", "flooding", "flood"]    
    hurricane = ["hurricane", "dorian","barry","fernand" ]
    earthquake =["earthquake"]
    tornado = ["tornado"]
    fire = ["fire"]
    general = ["damage", "disaster"]
    '''
    df = df[df.text.str.contains('|'.join(nd_key))]
    return df           
  
'''
State Farm as a whole, exclusive of the other two categories
''' 
def sf_df(df):
    app_key = [" app ","application"," mobile ", "drive safe and save", "#drivesafeandsave", "drive safe", "smartphone", "iphone"]
    nd_key = ["landslide", "imelda","tropical storm","storm michael", "severe storms", "severe storm", "flooding", "flood","hurricane", "dorian","barry","fernand","earthquake","tornado","fire","damage", "disaster"]
    df = df[~df.text.str.contains("|".join(app_key))]
    df = df[~df.text.str.contains("|".join(nd_key))]
    return df
        

def main():
    df = read_file('cleaned_data.csv')
    mobile = mobile_df(df)
    nd = nd_df(df)
    sf = sf_df(df)
    
    mobile.to_csv(r'mobile.csv', index = False)
    nd.to_csv(r'naturaldisasters.csv', index = False)
    sf.to_csv(r'statefarm.csv', index = False)
    
    
    #print(df)

if __name__ == '__main__':
    main()


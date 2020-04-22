
import pandas as pd

def read_file(file):
    df = pd.read_csv(file)

    return df


def main():
    files = ["02-2019.csv","03-2019.csv","04-2019.csv","05-2019.csv","06-2019.csv","07-2019.csv","08-2019.csv","09-2019.csv","10-2019.csv","11-2019.csv","12-2019.csv"]
    #files = ["processed_batch (2).csv", "processed_batch (3).csv", "processed_batch (4).csv"]
    
    df = read_file('01-2019.csv')
    
    for f in files:
        dfadd = read_file(f)
        
        df = pd.concat([df, dfadd], axis=0)
    
    #print(df)
    df.to_csv(r'merge2019.csv', index = False)
    
    #print(df)

if __name__ == '__main__':
    main()

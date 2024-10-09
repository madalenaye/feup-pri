import re
import pandas as pd


def extract_age(string):
    if isinstance(string, list):
        text = ""
        for s in string:
            text += s
        age = re.search(r'\d+',text).group()
        if age:
            return int(age)
        else:
            return pd.NA
    else:
        age = re.search(r'\d+',string).group()
        if age:
            return int(age)
        else:
            return pd.NA
        
def dataset_processing_characters(path_to_file):
    df = pd.read_json(path_to_file)
    df = df.transpose()
    # Extract 'Age' from the string or list of strings
    df["Age"]= df["Age"].apply(extract_age)
    # Merge 'Animated debut' and 'Debut' columns since they mean the same thing
    df["Debut"] = df["Animated debut"].fillna(df["Debut"])
    df.drop(columns=["Animated debut"],inplace=True)
    # Drop unnecessary columns
    df.drop(columns=["Game counterpart","Manga counterpart(s)","Manga series","Games","Generation","Counterpart(s)"],inplace=True)
    # Fill NaN values with 'Unknown
    df.fillna(value="Unknown",inplace=True) 
    return df
# Processes the dataset obtained from the series json file
# Arg path_to_file: string path to the json file
def dataset_processing_series(path_to_file):
    df = pd.read_json(path_to_file)
    df = df.transpose()
    # Extract 'Japan' and 'United States' dates from the nested dictionaries
    df['First broadcast Japan'] = df['First broadcast'].apply(lambda x: x.get('Japan') if isinstance(x, dict) else None)
    df['First broadcast United States'] = df['First broadcast'].apply(lambda x: x.get('United States') if isinstance(x, dict) else None)
    # Convert the extracted dates to datetime format
    df['First broadcast Japan'] = pd.to_datetime(df['First broadcast Japan'])
    df['First broadcast United States'] = pd.to_datetime(df['First broadcast United States'].apply(lambda x: x[:x.find('*')] if x.find('*') != -1 else x), errors="coerce")

    df['Broadcast Delay'] = (df['First broadcast United States'] - df['First broadcast Japan']).dt.days

    # Extract the 'Characters' column and split it into 'Human Characters' and 'Pokemon Characters'
    df["Human Characters"] = df["Characters"].apply(lambda x: x.get("Humans") if isinstance(x, dict) else None)
    df["Pokemon Characters"] = df["Characters"].apply(lambda x: x.get("Pokemons") if isinstance(x, dict) else None)

    # Extract the 'English Themes' column and split it into 'English Theme Opening' and 'English Theme Ending'
    df["English Theme Opening"] = df["English themes"].apply(lambda x: x.get("Opening") if isinstance(x, dict) else None)
    df["English Theme Ending"] = df["English themes"].apply(lambda x: x.get("Ending") if isinstance(x, dict) else None)

    # Extract the 'Japanese Themes' column and split it into 'Japanese Themed Opening' and 'Japanese Themed Ending'
    df["Japanese Theme Opening"] = df["Japanese themes"].apply(lambda x: x.get("Opening") if isinstance(x, dict) else None)
    df["Japanese Theme Ending"] = df["Japanese themes"].apply(lambda x: x.get("Ending") if isinstance(x, dict) else None)

    # Extract the 'Credits' column and split it into many different columns with the respective credits
    for key in df["Credits"][0].keys():
        df[key] = df["Credits"].apply(lambda x: x.get(key) if isinstance(x, dict) else None)

    df["Plot Word Count"] = df["Plot"].apply(lambda x: len(x.split(" ")))

    # Fill NaN values with 'Unknown'
    #df.fillna(value="Unknown",inplace=True)
    return df
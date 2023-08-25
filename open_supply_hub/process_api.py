import argparse
import urllib.parse
import json
import requests
import numpy as np
import pandas as pd

def parse_request(r, cont_type):
    '''
    Parses json request from the OpenSupplyHub API into a Pandas DataFrame.

    Parameters
    ----------
    r : requests.Response
        A response object returned by a HTTP request.
    cont_type : str
        A string representing the type of contributor.

    Returns
    -------
    tuple
        - A Pandas DataFrame containing the parsed data.
        - The next page URL as a string.

    Raises
    ------
    Exception
        If there is a problem with the HTTP request or format of the data.


    Notes
    -----
    This function assumes that the JSON response contains a "results" object with
    "headers" and "rows" sub-objects. It also assumes that empty values in the DataFrame
    are represented by empty strings, which are replaced with NaN values. Finally, it
    drops any columns that are entirely composed of NaN values.
    '''

    if r.ok:
        response = json.loads(r.text)
        headers = response["results"]["headers"]
        data = response["results"]["rows"]

        df = pd.DataFrame(data, columns=headers).replace("", np.nan).dropna(how="all", axis=1)
        df["contributor_type"] = cont_type
        return df, response["next"]
    else:        
        print(r.url)
        raise("Problem with request")
        
def get_data(cookies, filename = 'data.tsv.gz', contributor_types=None, url="https://opensupplyhub.org/api/facilities-downloads/?"):
    if contributor_types is None:
        # define parameters (these come from the website, make sure that they are up to date before running the code)
        contributor_types = ['Academic / Researcher / Journalist / Student', 
                            'Auditor / Certification Scheme / Service Provider', 
                            'Brand / Retailer', 
                            'Civil Society Organization', 
                            'Facility / Factory / Manufacturing Group / Supplier / Vendor', 
                            'Multi-Stakeholder Initiative', 
                            'Union', 
                            'Other']
    
    parms = {"detail": "true",
            "format": "json",
            "page": 1,
            "pageSize": 100} #100 seems to be the largest possible pageSize
            


    # Get all data
    df_all = []
    for cont_type in contributor_types:
        print(f"\nStarting {cont_type}")
        parms.update({"contributor_types": cont_type, "page": 1})
        url_form = url + urllib.parse.urlencode(parms)
        i = 0
        while url_form is not None:
            # track
            print(i, end=":")
            i += 1
            # get json
            r = requests.get(url_form,  cookies=cookies)
            # parse json
            df, url_form = parse_request(r, cont_type)
            df_all.append(df)
    
    df = pd.concat(df_all)
    df = df.drop_duplicates()
    
    # save data
    df.to_csv(filename, compression="gzip", sep="\t", index=None)

def main():

    '''
    Main function:
        Loads user-defined variables from the configuration file.
        Calls the get_data function with these variables
        and creates the output CSV file.
    
    The configuration file must be called config_api.json and must contain the 
    following variables in a dictionary format:
       Mandatory:
       - cookies
       Optional:
       - filename
       - contributor_types
       - url 
    '''

    # Load parameters from configuration file
    with open('config_api.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    # Call function to process data
    get_data(**config)

if __name__ == "__main__":
    main()
    

    

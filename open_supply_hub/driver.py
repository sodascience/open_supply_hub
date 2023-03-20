import pandas as pd
import json

import glob
import time

from functions import *

if __name__ == "__main__":

    #Get list of files from the data directory containing the json files
    files = glob.glob('../data/json_files/*')
    #files = glob.glob('../data/json_files_small_subset/*')
    
    #List containing all entries of the facility dataframe. 
    #Each row of the dataframe contains data for a unique (brand, supplier) pair
    alldata_facilities = []

    #List containing all entries of the contributor dataframe. 
    #Each row of the dataframe contains data for a unique (brand, supplier) pair
    alldata_contributors = []

    #List of os_ids. Each os_id corresponds to one supplier.
    os_ids = []

    start_time = time.time()

    #Go through all json files in the directory
    for filename in files:

        #Read one json file
        f = open(filename, 'r')
        manyfacilities = json.load(f)    

        #Read one entry in the json file
        for facility in manyfacilities['features']:

            # export may contain duplicates
            if facility['properties']['os_id'] not in os_ids:
                os_ids.append(facility['properties']['os_id'])

                data_facility = extract_facility_data(facility) #Get facility data
                alldata_facilities.append(data_facility)

                for contributor in facility['properties']['extended_fields']['name']:
                    data_initial = {
                        'contributor_id': contributor['contributor_id'], #Contributor name
                        'contributor_name': contributor['contributor_name'], #Contributor ID
                        'os_id': facility['properties']['os_id'], #Supplier OS ID     
                        'supplier_name': contributor['value'], # Supplier name
                        'contribution_date': contributor['updated_at'].split('T')[0] #Date on which this contributor updated entry for this supplier 
                        }

                    data_contributor = extract_contributor_data(data_initial, facility, contributor) #Add data from extended fields                                               
                    alldata_contributors.append(data_contributor)

    end_time = time.time()

    run_time = end_time - start_time
    print("Run time: %f minutes" %(run_time/60))


    #Write out facilities data to csv file

    #Convert to pandas dataframe
    df = pd.DataFrame(alldata_facilities)
    #Replace all NaN entries by blank spaces
    df = df.fillna('')
    #Sort the dataframe by supplier name
    df_sorted_facilities = df.sort_values('facility_name')
    #Write sorted dataframe to csv file
    #Tab-separated since the address field has commas
    df_sorted_facilities.to_csv('../results/osh_facilities.csv', index=False, sep='\t')

    #Write out contributors data to csv file

    #Convert to pandas dataframe
    df = pd.DataFrame(alldata_contributors)
    #Replace all NaN entries by blank spaces
    df = df.fillna('')
    #Sort the dataframe by brand
    df_sorted_contributors = df.sort_values(['contributor_name', 'os_id', 'contribution_date'])
    #Write sorted dataframe to csv file
    #Tab-separated since the address field has commas
    df_sorted_contributors.to_csv('../results/osh_contributors.csv', index=False, sep='\t')

import pandas as pd
import json
import glob
import time

from functions import *

if __name__ == "__main__":

    # Get list of files from the data directory containing the json files
    files = glob.glob('../data/json_files/*')

    # Mapping contributor ID to contributor type 
    contributor_type = pd.read_excel('../data/contrib_type_id.xlsx')
    
    # List containing all entries of the facility dataframe. 
    # Each row of the dataframe contains data for a unique (brand, supplier) pair
    alldata_facilities = []

    # List containing all entries of the contributor dataframe. 
    # Each row of the dataframe contains data for a unique (brand, supplier) pair
    alldata_contributors = []

    # List of os_ids. Each os_id corresponds to one supplier.
    os_ids = []

    start_time = time.time()

    # Go through all json files in the directory
    for filename in files:

        # Read one json file
        f = open(filename, 'r')
        manyfacilities = json.load(f)    

        # Read one entry in the json file
        for facility in manyfacilities['features']:

            # export may contain duplicates
            if facility['properties']['os_id'] not in os_ids:
                os_ids.append(facility['properties']['os_id'])

                data_facility = extract_facility_data(facility) #Get facility data
                alldata_facilities.append(data_facility)

                # Go through each contributor and record data entered by it
                for contributor in facility['properties']['extended_fields']['name']:
                    #Extract contributor data, and data entered by it about this facility
                    data_contributor = extract_contributor_data(facility, contributor)                                                
                    alldata_contributors.append(data_contributor)

    end_time = time.time()

    run_time = end_time - start_time
    print("Run time: %f minutes" %(run_time/60))

    # Write out facilities data to csv file
    write_to_csv(alldata_facilities, '../results/osh_facilities.csv', 'facility_name')

    # Write out contributors data to csv file
    write_to_csv(alldata_contributors, '../results/osh_contributors.csv', ['contributor_name', 'os_id', 'contribution_date'])
    

import json
import glob
import time
import pandas as pd

def get_data(data_directory,
             filename_facilities="facilities.csv", 
             filename_contributions="contributors.csv",
             verbose=True):
    
    """
    Gets information from JSON files, and writes it into two files,
    one containing information about facilities, and the other about
    contributors.

    Parameters
    ----------
    data_directory : Location of JSON files
    filename_facilities : File to which facilities information is written
    filename_contributors : File to which contributors information is written
    """
    
    # Get list of files from the data directory containing the json files
    files = glob.glob(data_directory + '/*')

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
    n_curr = 0
    n_files = len(files)
    for filename in files:
        if verbose:
            n_curr += 1
            print(f"Currently processing {filename}... ({n_curr}/{n_files})", end="\r")

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
    if verbose: 
        print(f"\nRun time: {run_time/60} minutes")

    # Write out facilities data to csv file
    write_to_csv(alldata_facilities, 
                 filename_facilities, 
                 'facility_name')

    # Write out contributors data to csv file
    write_to_csv(alldata_contributors,
                 filename_contributions,
                 ['contribution_date'])

def extract_facility_data(facility):
    """
    Extract data about facility
    """
    
    data = {
        'os_id': facility['properties']['os_id'], # OS ID of supplier
        'facility_name': facility['properties']['name'], #Name of supplier
        'address': facility['properties']['address'], # Address of supplier
        'country_code': facility['properties']['country_code'], # Country code of supplier
        'country_name': facility['properties']['country_name'], #Country name of supplier
        'lat': facility['geometry']['coordinates'][1], #Latitude of supplier
        'lng': facility['geometry']['coordinates'][0], # Longitude of supplier
        'is_closed': facility['properties']['is_closed'], #Is the supplier now closed?
        }

    return data


def extract_contributor_data(facility, contributor):  
    """
    Extract data entered by contributor
    """
    
    # Extract information about contributor    
    data = {
            'contributor_id': contributor['contributor_id'], # Contributor name
            'contributor_name': contributor['contributor_name'], # Contributor ID
            'os_id': facility['properties']['os_id'], # Supplier OS ID     
            'supplier_name': contributor['value'], # Supplier name
            'contribution_date': contributor['updated_at'].split('T')[0] # Date on which this contributor updated entry for this supplier 
           }
    
    # Extract information about the facility (supplier), entered by the contributor

    # Address of the supplier
    if facility['properties']['extended_fields']['address']:
        for entry in facility['properties']['extended_fields']['address']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                data['address'] = entry['value']
    
    # Minimum and maximum number of workers
    if facility['properties']['extended_fields']['number_of_workers']: 
        for entry in facility['properties']['extended_fields']['number_of_workers']: 
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                data['number_of_workers_min'] = entry['value']['min']
                data['number_of_workers_max'] = entry['value']['max']

    # Parent company of the supplier
    if facility['properties']['extended_fields']['parent_company']:
        for entry in facility['properties']['extended_fields']['parent_company']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                if 'name' in entry['value'].keys():
                    data['parent_company'] = entry['value']['name']

    # Facility type of the supplier
    if facility['properties']['extended_fields']['facility_type']:
        for entry in facility['properties']['extended_fields']['facility_type']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                if 'raw_values' in entry['value'].keys():
                    data['facility_type'] = entry['value']['raw_values']      

    # Processing type of the supplier
    if facility['properties']['extended_fields']['processing_type']:
        for entry in facility['properties']['extended_fields']['processing_type']:              
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                if 'raw_values' in entry['value'].keys():
                    data['processing_type'] = entry['value']['raw_values']  

    # Product type of the supplier
    if facility['properties']['extended_fields']['product_type']:
        for entry in facility['properties']['extended_fields']['product_type']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:        
                if 'raw_values' in entry['value'].keys():
                    data['product_type'] = ', '.join(entry['value']['raw_values']) 

    return data

def write_to_csv(data_dictionary, output_filename, sort_columns):
    """
    Write data from dictionary to csv format:
    data_dictionary: input data in dictionary format
    ouput_filename: output filename
    sort_columns: columns by which the output csv file must be sorted
    """
    
    # Convert to pandas dataframe
    df = pd.DataFrame(data_dictionary)

    # Replace all NaN entries by blank spaces and sort
    df = df.fillna('').sort_values(sort_columns)

    # drop duplicates in presence of columns containing lists
    df_dedup = df.loc[df.astype(str).drop_duplicates().index]

    # Write sorted dataframe to csv file
    df_dedup.to_csv(output_filename, index=False, sep='\t')

def main():
    """
    Main function:
        Loads user-defined variables from the configuration file.
        Calls the get_data function with these variables
        and creates the output CSV files.
    
    The configuration file must be called config_api.json and must contain the 
    following variables in a dictionary format:
       Mandatory:
       - data_directory: Location of the JSON files
       Optional:
       - filename_facilities: Output CSV filename with information about \
         facilities
       - filename_contributors: Output CSV filename with information about \
         contributorss
    """

    # Load parameters from configuration file
    with open('config_json.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    # Call function to process data
    get_data(**config)

if __name__ == "__main__":
    main()

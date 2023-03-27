'''
Extract data about facility
'''

def extract_facility_data(facility):
    
    #Extract data about facility
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

'''
Extract data entered by contributor
'''

def extract_contributor_data(facility, contributor):

    #Extract information about contributor
    
    data = {
            'contributor_id': contributor['contributor_id'], #Contributor name
            'contributor_name': contributor['contributor_name'], #Contributor ID
            'os_id': facility['properties']['os_id'], #Supplier OS ID     
            'supplier_name': contributor['value'], # Supplier name
            'contribution_date': contributor['updated_at'].split('T')[0] #Date on which this contributor updated entry for this supplier 
           }
    
    #Extract information about the facility (supplier), entered by the contributor

    #Address of the supplier
    if facility['properties']['extended_fields']['address']:
        for entry in facility['properties']['extended_fields']['address']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                data['address'] = entry['value']
    
    #Minimum and maximum number of workers
    if facility['properties']['extended_fields']['number_of_workers']: 
        for entry in facility['properties']['extended_fields']['number_of_workers']: 
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                data['number_of_workers_min'] = entry['value']['min']
                data['number_of_workers_max'] = entry['value']['max']

    #Parent company of the supplier
    if facility['properties']['extended_fields']['parent_company']:
        for entry in facility['properties']['extended_fields']['parent_company']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                if 'name' in entry['value'].keys():
                    data['parent_company'] = entry['value']['name']

    #Facility type of the supplier
    if facility['properties']['extended_fields']['facility_type']:
        for entry in facility['properties']['extended_fields']['facility_type']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                if 'raw_values' in entry['value'].keys():
                    data['facility_type'] = entry['value']['raw_values']      

    #Processing type of the supplier
    if facility['properties']['extended_fields']['processing_type']:
        for entry in facility['properties']['extended_fields']['processing_type']:              
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:
                if 'raw_values' in entry['value'].keys():
                    data['processing_type'] = entry['value']['raw_values']  

    #Product type of the supplier
    if facility['properties']['extended_fields']['product_type']:
        for entry in facility['properties']['extended_fields']['product_type']:   
            entry['contribution_date'] = entry['updated_at'].split('T')[0]
            if entry['contributor_id'] == data['contributor_id'] and entry['contribution_date'] == data['contribution_date']:        
                if 'raw_values' in entry['value'].keys():
                    data['product_type'] = ', '.join(entry['value']['raw_values']) 

    return data

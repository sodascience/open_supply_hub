## Processing supply chain data obtained from Open Supply Hub

### Introduction

This repository contains python scripts to download and process supply chain data from [Open Supply Hub](https://opensupplyhub.org). Open Supply Hub is a website that provides worldwide supply chain data for various industry sectors.

**Input data**: The data can be obtained either as a JSON dump or via an API. Contact Open Supply Hub for pricing.

**Output data**: Input data neatly formatted in CSV format. The data contains information about suppliers, the industry sectors they belong to, the brands they supply to, etc. 

<!-- TABLE OF CONTENTS -->
### Prerequisites

To install and run this project, run the following command from your terminal:

```
pip install -r requirements.txt
```

### Usage

Clone the repository, `cd` to it, and then follow either the JSON dump workflow or the API call workflow.

#### JSON dump extraction

1. Get a JSON dump from OpenSupplyHub (contact them for pricing), unzip it, and store it in the `data` folder.
2. Add the user-supplied parameters in the `config_json.json` configuration file. 
3. Run `python open_supply_hub/process_json.py`
4. The results should now appear as two files in the `results` folder

#### API extraction

1. Get API access / API key from OpenSupplyHub (contact them for pricing)
2. Add the API key and other information in the `config_api.json` configuration file.
3. Run `python open_supply_hub/process_api.py`
4. The results should now appear as a single compressed file in the `results` folder

### Output
* Using the JSON dumps: Two CSV files, one with information about the facilities (name, address, etc), one with information about the contributions (date, supplier, etc)
* Using the API: One CSV file in the same format as the Excel/CSV exports from the website.

| os_id | contribution_date | name       | address           | country_code                                      | country_name | lat        | lng        | sector    | contributor (list) | number_of_workers                                 | … | is_closed | contributor_type                             |
| ----- | ----------------- | ---------- | ----------------- | ------------------------------------------------- | ------------ | ---------- | ---------- | --------- | ------------------ | ------------------------------------------------- | - | --------- | -------------------------------------------- |
| 0     | BD2020212VEDNJC   | 30/07/2020 | 2T's Creation     | Plot 1241 (3rd Floor), Begum Rokeya Sarani, Ea... | BD           | Bangladesh | 23.8006254 | 90.371022 | Apparel            | PPE: Mapped in Bangladesh (PPE: Mapped in Bang... | … | FALSE     | Academic / Researcher / Journalist / Student |
| 1     | BD2020212VEDNJC   | 16/05/2022 |                   |                                                   |              |            |            |           | Apparel            | BRAC University (Mapped in Bangladesh: Export ... | … |           | Academic / Researcher / Journalist / Student |
| 2     | BD2020212VEDNJC   | 16/05/2022 |                   |                                                   |              |            |            |           | Apparel            | An Academic / Researcher / Journalist / Studen... | … |           | Academic / Researcher / Journalist / Student |
| 3     | BD2020212VEDNJC   | 29/11/2021 |                   |                                                   |              |            |            |           | Apparel            | BRAC University (API)                             | … |           | Academic / Researcher / Journalist / Student |
| 4     | BD2019248GNVQ6X   | 05/09/2019 | 3-A Fashions Ltd. | Madrasha Road, Khejur Bagan, Ashulia, Savar, D... | BD           | Bangladesh | 23.8909633 | 90.329906 | Apparel            | BRAC University (Mapped in Bangladesh: Export-... | … | FALSE     | Academic / Researcher / Journalist / Student |

### License

The code in this project is released under [MIT License](/LICENSE).

<!-- ABOUT THE PROJECT -->
### About the Project

**Date**: February - April 2023

**Researcher(s)**:

- Luc Fransen (l.w.fransen@uva.nl)
- Diliara Valeeva (d.valeeva@uva.nl)

**Research Software Engineer(s)**:

- Modhurita Mitra (m.mitra@uu.nl)
- Javier Garcia Bernardo (j.garciabernardo@uu.nl)
- Parisa Zahedi (p.zahedi@uu.nl)

<!-- CONTACT -->
## Contact

This project is developed and maintained by the [ODISSEI Social Data
Science (SoDa)](https://odissei-data.nl/nl/soda/) team.

<img src="https://odissei-soda.nl/images/logos/soda_logo.svg" alt="SoDa logo" width="250px"/>

Do you have questions, suggestions, or remarks? File an issue in the issue tracker or feel free to contact the team via https://odissei-soda.nl/

Project link: [https://github.com/sodascience/open_supply_hub](https://github.com/sodascience/open_supply_hub)


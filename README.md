## Processing supply chain data obtained from Open Supply Hub

### Introduction

This repository contains python scripts to download and process supply chain data from [Open Supply Hub](https://opensupplyhub.org). Open Supply Hub is a website that provides worldwide supply chain data for various industry sectors.

**Input data**: The data can be obtained either as a JSON dump or via an API. Contact Open Supply Hub for pricing.
**Output data**: Input data neatly formatted in CSV format. The data contains information about suppliers, the industry sectors they belong to, the brands they supply to, etc. 

<!-- TABLE OF CONTENTS -->
### Prerequisites

To install and run this project, run the following command from your terminal:

``` pip install -r requirements.txt```


### Usage

1. Download the following files from the `open supply hub`[directory](open_supply_hub):
	* process_json.py (extracts data from JSON dump)
	* process_api.py (exctracts data from aPI)
	* examples.ipynb
2. Open `examples.ipynb` in a Jupyter Notebook.
  * Section "Obtain data from JSON files" shows how to extract data from a JSON dump
  * Section "Obtain data via API" shows how to extract data from the API

### Output
* Using the JSON dumps: Two CSV files, one with information about the facilities (name, address, etc), one with information about the contributions (date, supplier, etc)
* Using the API: One CSV file in the same format as the Excel/CSV exports from the website.


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

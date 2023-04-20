
<!-- Include Github badges here (optional) -->
<!-- e.g. Github Actions workflow status -->

Obtain supply chain data from [Open Supply Hub](https://opensupplyhub.org). 

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Open Supply Hub](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [About the Project](#about-the-project)
    - [Description](#description)  
    - [License](#license)
  - [Contact](#contact)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

To install and run this project you need to have the following prerequisites installed.

- Python

<!-- ABOUT THE PROJECT -->
## About the Project

**Date**: February - April 2023

**Researcher(s)**:

- Luc Fransen (l.w.fransen@uva.nl)
- Diliara Valeeva (d.valeeva@uva.nl)

**Research Software Engineer(s)**:

- Modhurita Mitra (m.mitra@uu.nl)
- Javier Garcia Bernardo (j.garciabernardo@uu.nl)
- Parisa Zahedi (p.zahedi@uu.nl)

<!-- A more elaborate description about the project/software (compared to the top of this page) can be included here-->
### Description

We have obtained global supply chain data from the [Open Supply Hub](https://opensupplyhub.org) website from a JSON dump and via an API. 

### Usage
1. From the [`open supply hub` directory](open_supply_hub/open_supply_hub/), download the following files into the same folder/directory:
	1. process_json.py
	2. process_api.py
	3. examples.ipynb
2. Open `examples.ipynb` in a browser.

#### To extract data from JSON files
1. Assign the variable `data_directory` to the directory where the JSON files are stored.
2. Assign the variable `results` to the directory where you want to store the output files.
3. Run the notebook cells which are under the heading "Obtain data from JSON files".
4. Two files with information about the facilities and the contributors are now stored as CSV files in the `results` directory.

#### To extract data via API
1. Assign the variable `results` to the directory where you want to store the output files.
2. Log into the [Open Supply Hub website](https://opensupplyhub.org) (create an account if you don't have one) and find the `sessionid`. Enter it as the value of `sessionid` in `cookies`.
3. Run the notebook cells which are under the heading "Obtain data via API".
4. A file with information about the facilities and the contributors is now created as a CSV file in the `results` directory.
<!-- Do not forget to also include the license in a separate file(LICENSE[.txt/.md]) and link it properly. -->
### License

The code in this project is released under [MIT License](/LICENSE).

<!-- CONTACT -->
## Contact

Contact email: contact.rse@uu.nl

Project link: [https://github.com/sodascience/open_supply_hub](https://github.com/sodascience/open_supply_hub)
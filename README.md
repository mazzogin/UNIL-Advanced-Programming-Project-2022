<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://gifimage.net/wp-content/uploads/2017/11/its-free-real-estate-gif-1.gif" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/badge/issues-0%20open-success)](https://github.com/mazzogin/UNIL-Advanced-Programming-Project-2022/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/mazzogin/UNIL-Advanced-Programming-Project-2022/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [TODO](TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This project serves three purposes:
1. Create a python web scraper using `Selenium` and `Scrapy` that obtains detailed data from the swiss real estate platform comparis
2. Use said data to create a prototype of a platform using `Tk`(`tkinter`) where houses can be selected without being distracted by pretty pictures and by focusing on the facts
3. Provide data for our sister project. Find more information regarding the latter project [here](https://github.com/mazzogin/UNIL-Advanced-Data-Analysis-Project-2022)

## 🏁 Getting Started <a name = "getting_started"></a>
### Prerequisites

You will need to use the following `python` packages:

```
Scrapy
Selenium
Webdriver_manager
Numpy
Pandas
Openpyxl
Tk (tkinter)
Pillow
```

### Installing
In your virtual environment, install the following libraries:
```
pip install scrapy
pip install selenium
pip install webdriver-manager
pip install webdriver_manager
pip install numpy
pip install pandas
pip install openpyxl
pip install tkinter
pip install pillow
```

## 🎈 Usage <a name="usage"></a>

This project is divided up into two parts:
1. Obtaining the data with two separate web scrapers (output = 2 .csv files)
2. Displaying the data with an interactive interface

### Important Note
In order for you to run the interface, you do not have to download the data.
1. An example dataset is provided, called `dataset.xlsx`
2. `dataset.xlsx` was set up using data that was obtained from the scraping


## 🚀 Deployment <a name = "deployment"></a>

### Executing the web scraper: The whole process
The web scraping process is the following:
1. Go to [comparis.ch](https://fr.comparis.ch/immobilien/default)
2. Select the region of interest (in this case simply "Lausanne")
3. Enter
4. To get our settings: on the listings page, select "Rayon": "10k" (see [here]([https://github.com/mazzogin/UNIL-Advanced-Data-Analysis-Project-2022](https://fr.comparis.ch/immobilien/default](https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D](https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D) )
5. From this search/link the URL's for all the listings can be scraped, using the `property_code_scraper.py` in directory `Comparis_Webscraper/Comparis_Webscraper/spiders/`
6. Navigate to the `property_code_scraper.py` and manually enter the URL in `line 46`
7. In your `terminal`, navigate to the directory `Comparis_Webscraper/Comparis_Webscraper/spiders/`
8. Also in your `terminal`, enter `scrapy crawl id-scraper`
9. The output of the `id-scraper` spider will consist of one `.csv` file named `property-codes_YYYYMMDD.csv` which is placed in the `data` folder
11. To scrape every single URL in `property-codes-YYYYMMDD.csv` navigate to the second web scraper called `comparis_scraper.py`.
12. In `line 49, col 91`, change the YYYYMMDD component of the filename if you do not want to use the default one
13. Save the file
14. In your `terminal`, enter `scrapy crawl property-scraper`
15. Wait ~80 minutes, or simply look at the default dataset in `data` called `property_details`
16. The scraper `property_details` will put a file called `property_details_YYYYMMDD.csv` into the data folder

### Executing the interface


## ✍️ Authors <a name = "authors"></a>

- [@zoegiacomi]([https://github.com/kylelobo](https://github.com/zoegiacomi)) - Interface, Text and Description

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used 
- Inspiration
- References




## Running
1. Install the required python dependencies
   ```bash
   make install_dep
   ```
2. Run the project
   ```bash
   make all
   ```


## Troubleshooting

- Clean the working directory
  ```bash
  make clean
  ```
  Relaunch the programm

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://gifimage.net/wp-content/uploads/2017/11/its-free-real-estate-gif-1.gif" alt="Project logo"></a>
</p>

<h3 align="center">Real Transparency in Real Estate</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/badge/issues-0%20open-success)](https://github.com/mazzogin/UNIL-Advanced-Programming-Project-2022/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/mazzogin/UNIL-Advanced-Programming-Project-2022/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">
      
  Real estate has been for a long time an opaque, decentralized market. As such, the Swiss housing market is subject to information asymmetry between buyers and sellers, creating potential adverse selection. The housing market is dominated by real estate agents who possess more information than potential buyers which contributes to skewing the price of houses.
    Though transparency has positively evolved with the apparition of the internet and online properties platforms, there is still a lack of publicly available historical data and comparative databases.
    As such, our research is focused on testing whether creating a continuously updated open-source database of all present and historical listings in Switzerland is feasible. 
    
  <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
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
In order for you to run the interface, you do not have to scrape the data.
1. An example dataset is provided, called `dataset.xlsx`
2. `dataset.xlsx` was set up using data that was obtained from the scraping


## 🚀 Deployment <a name = "deployment"></a>

### Executing the web scraper: The whole process
The web scraping process is the following:
1. Go to [comparis.ch](https://fr.comparis.ch/immobilien/default)
2. Select the region of interest (in this case simply "Lausanne")
3. Enter
4. To get our settings: on the listings page, select "Rayon": "10k" (see [here](https://fr.comparis.ch/immobilien/result/list?requestobject=%7B%22DealType%22%3A20%2C%22SiteId%22%3A0%2C%22RootPropertyTypes%22%3A%5B%5D%2C%22PropertyTypes%22%3A%5B%5D%2C%22RoomsFrom%22%3Anull%2C%22RoomsTo%22%3Anull%2C%22FloorSearchType%22%3A0%2C%22LivingSpaceFrom%22%3Anull%2C%22LivingSpaceTo%22%3Anull%2C%22PriceFrom%22%3Anull%2C%22PriceTo%22%3Anull%2C%22ComparisPointsMin%22%3A0%2C%22AdAgeMax%22%3A0%2C%22AdAgeInHoursMax%22%3Anull%2C%22Keyword%22%3A%22%22%2C%22WithImagesOnly%22%3Anull%2C%22WithPointsOnly%22%3Anull%2C%22Radius%22%3A%2210%22%2C%22MinAvailableDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22MinChangeDate%22%3A%221753-01-01T00%3A00%3A00%22%2C%22LocationSearchString%22%3A%22Lausanne%22%2C%22Sort%22%3A11%2C%22HasBalcony%22%3Afalse%2C%22HasTerrace%22%3Afalse%2C%22HasFireplace%22%3Afalse%2C%22HasDishwasher%22%3Afalse%2C%22HasWashingMachine%22%3Afalse%2C%22HasLift%22%3Afalse%2C%22HasParking%22%3Afalse%2C%22PetsAllowed%22%3Afalse%2C%22MinergieCertified%22%3Afalse%2C%22WheelchairAccessible%22%3Afalse%2C%22LowerLeftLatitude%22%3Anull%2C%22LowerLeftLongitude%22%3Anull%2C%22UpperRightLatitude%22%3Anull%2C%22UpperRightLongitude%22%3Anull%7D))
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
# If dataset was webscrapped start from 1 if not start from 4.
1. Open the `cleaning_database_GUI.py` file.
2. Check that the paths correspond to the scrapped data csv files
3. Run the `cleaning_database_GUI.py` which should produce the `database.xlsx` file
4. Open `graphs_GUI.py` Check the corresponding paths
5. Run `graphs_GUI.py`. This should create two new excels : `MeanPriceRoom.xlsx`and `MeanPriceZIP.xlsx`
6. Open the `main5.py`file
7. Check the path correspond to the full dataset in line 146.
8. Check the paths for the graphs, line 150 corresponds to `MeanPriceZIP.xlsx` and line 155 to `MeanPriceRoom.xlsx`
9. Save
10. In the terminal enter `python3 main5.py`

## ✍️ Authors <a name = "authors"></a>

- [@zoegiacomi](https://github.com/zoegiacomi) - Interface, Text and Description
- [@notoriousemi](https://github.com/notoriousemi) - Writing the text, editing the video and helping where it was needed


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

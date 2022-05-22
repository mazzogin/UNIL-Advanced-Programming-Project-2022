# Comparis Scraper



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

1. Run file property_codes_downloader.py in directory Comparis_Webscraper
2. In the terminal, cd into <cd Comparis_Webscraper/Comparis_Webscraper/spiders>
3. Run command <scrapy crawl htmlparser -o ../../../data/property_codes.csv>
4. Run command <scrapy crawl real-estate -o ../../../data/property_details.csv>
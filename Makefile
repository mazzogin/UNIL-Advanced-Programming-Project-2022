# In console, in project root directory run:
# make <tag>
# e.g.: make all


# Path to script to fetch codes
PATH_CODES_DOWNLOADER=Comparis_Webscraper/property_codes_downloader.py
# Path to comparis scraper
PATH_HTML_PARSER=Comparis_Webscraper/Comparis_Webscraper/spiders
# Path to property codes csv
PATH_PROP_CODE=../../../data/property_codes.csv
PATH_PROP_DETAIL=../../../data/property_details.csv
# Path to Comparis start html file
PATH_START_URL=data/Comparis_Start_URL.html
# Name of spider
SPIDER_HTML=htmlparser
SPIDER_ESTATE=real-estate


.DEFAULT_GOAL := all

all:    
	@echo " -> Running codes downloader ..."
	python3 $(PATH_CODES_DOWNLOADER)
	cd $(PATH_HTML_PARSER)
	@echo " -> Running spiders"
	scrapy crawl $(SPIDER_HTML) -o $(PATH_PROP_CODE)
	scrapy crawl $(SPIDER_ESTATE) -o $(PATH_PROP_DETAIL)
# Add more commands (if needed)

clean:
	@echo " -> Remove Comparis_Start_URL.html"
	rm -f $(PATH_START_URL)
# Add more file to remove (if needed)

install_dep:
	pip3 install scrapy
	pip3 install selenium
# Add more dependencies if needed
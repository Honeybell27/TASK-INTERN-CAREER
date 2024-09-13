# **Task 1: Web Scraping and Automation**

## Purpose
  This script is designed to scrape data from a publicly
  accessible news website, extracting headlines, publication dates,
  and article links. The goal is to automate the data acquisition process
  to keep the dataset up-to-date.
  
## Dependencies
- Python 3.x
- requests
- beautifulsoup4
- pandas

## Script Overview
 The script uses the 'requests' library to fetch HTML content of the website
 and 'BeautifulSoup' to parse the HTML. It extracts the desired data and saves it
 to a CSV fie for further analysis.

## How to Run the Script
1. Clone the repository.
2. Install the required dependencies:
   `pip install requests beautifulsoup4 pandas`
3. Run the script:
  `python daily_post_scrapper.py`

## Automation
 The script is scheduled to run daily using _Task Scheduler_
 to ensure the dataset is updated regularly
 
## Output
The script generates a CSV file named
_'daily_post-articles_<timestamp>.csv'_,containing the scraped
headlines,publication dates, and article links.

## Conclusion
 This task provided valuable experience in web scraping, data processing,
 and automation, which are essential skills in data analysis and
 software development.
 
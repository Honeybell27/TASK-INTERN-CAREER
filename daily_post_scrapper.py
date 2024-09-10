import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


# Function to scrape data from Daily Post
def scrape_daily_post():
    base_url = 'https://dailypost.ng/hot-news/'
    articles = []
    max_pages = 20

    for page_number in range(1, max_pages + 1):
        url = f'{base_url}page/{page_number}/'  # Construct URL for pagination
        response = requests.get(url)

        if response.status_code != 200:
            break  # Exit loop if no more pages are available

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting headlines, dates, and links
        headlines = [h2.text.strip() for h2 in soup.find_all('h2')]
        dates = [span.text.strip() for span in soup.find_all('span', class_='mvp-cd-date left relative')]
        links = [link.get('href') for link in soup.find_all('a')]

        for headline, date, link in zip(headlines, dates, links):
            article = {
                'headline': headline,
                'date': date,
                'link': link
                }
            articles.append(article)

    # Convert to DataFrame
    df = pd.DataFrame(articles)
    # Save to CSV file with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    df.to_csv(f'daily_post_articles_{timestamp}.csv', index=False)


# Run the scraping function
if __name__ == '__main__':
    scrape_daily_post()
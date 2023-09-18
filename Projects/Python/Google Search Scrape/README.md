# Google Search Result Scraper

This Python script allows you to scrape google search results using the SerpApi and Pandas libraries. The example script takes a list of names from a CSV file, searches Google for their resumes, and stores the URLs in a new CSV file.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Pandas library
- SerpApi library
- SerpApi API Key (You need to sign up on [SerpApi](https://serpapi.com/) and obtain your API Key)

## Installation

1. Clone this repository to your local machine:

   ```
   git clone (link to repo)
   cd google-scrape
   ```

2. Install the required Python libraries:

   ```
   pip install pandas serpapi
   ```

3. Replace `"YOUR API KEY"` in the script with your actual SerpApi API Key.

## Usage

1. Prepare your CSV file: Make sure you have a CSV file named `example.csv` with a column named `example_column` containing the search query.

2. Run the script:

   ```
   python google_scrape.py
   ```

   The script will start scraping the Google search results for each value in the list. It will pause for 2 seconds between requests to avoid hitting the rate limit.

3. The script will print the URLs of the found data to the console and save them to a new CSV file named `output.csv`.

## Example Output

Here is an example of what the `output.csv` file might look like:

```
URLS,Name
https://example.com/laureate1_cv.pdf,Laureate 1
https://example.com/laureate2_resume.pdf,Laureate 2
Not Found,Laureate 3
...
```

## Acknowledgments

- [Pandas](https://pandas.pydata.org/)
- [SerpApi](https://serpapi.com/)

## Note

This script uses the SerpApi service to perform Google searches. Make sure to comply with SerpApi's terms of service and usage limits to avoid any issues.
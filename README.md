# s.dk Student Housing Scraper & Query Tool

A plug-and-play tool for scraping and analyzing student housing application data from [s.dk/studiebolig](https://mit.s.dk/studiebolig/). This project logs into the website, scrapes building ranking information using an API and HTML pages, cleans the data, and then provides a simple query interface and a basic Flask UI for non-technical users.

---

## Features

- **Automated Login:** Uses your username and password (stored securely in a `.env` file) to log into the s.dk website.
- **API Integration:** Fetches building IDs and names using the paginated API endpoint.
- **Scraping & Cleaning:** Scrapes building pages to extract tenancy ranking data, cleans and normalizes the data, and saves both raw and cleaned JSON files.
- **Query Module:** Provides functions to query which buildings are closest to getting an apartment (i.e. ranking closest to A).
- **Web UI:** A minimal Flask application to display the query results in an easy-to-read table.
- **Modular Structure:** Code is separated into modules for configuration, scraping, cleaning, and querying for ease of maintenance.

---

## Project Structure

project/ ├── main.py # Scraping and cleaning logic (runs the complete scraping process) 
         ├── scraper.py # Module with functions to perform scraping 
         ├── cleaner.py # Module with functions to clean raw data 
         ├── query.py # Module to query cleaned data and output results 
         ├── app.py # Flask app for a simple user interface 
         ├── config.py # Configuration and environment variable loading 
         ├── README.md # This file 
         ├── requirements.txt # Project dependencies 
         ├── .env # Environment variables (do not commit this file) 
         └── scraped_data/ # Folder where raw and cleaned JSON data files are stored

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd project
    ```

2. Create a virtual environment and activate it:

    ```bash
    Copy
    python -m venv myenv
    source myenv/bin/activate      # On Windows: myenv\Scripts\activate
    ```
3. Install dependencies:
    ```
    bash
    Copy
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
Create a file named .env in the project root with the following contents:

    env
    USERNAME=yourusenamefroms.dk
    PASSWORD=yourpasswordfroms.dk
    
## Usage
### Scraping & Cleaning Data
Run the scraper:
Execute main.py to log in, fetch building data from the API, scrape ranking data for each building, and save the raw and cleaned JSON files into the scraped_data folder.

```bash
Copy
python main.py
```
This process will:

Log into s.dk using your credentials.
Fetch all building IDs and names via the API.
Scrape the ranking data for each building and store the results in JSON files.
Clean the raw data and save the cleaned files.

### Querying Data
Run the query module:
To determine which buildings have the best (i.e. closest to A) ranking, run:

```bash
Copy
python query.py
```
This script loads all cleaned JSON files, aggregates the best ranking per building, and prints the building ID, name, and best ranking sorted from best to worst.

### Web UI
Run the Flask UI:
For a plug-and-play user interface, start the Flask app:

```bash
Copy
python app.py
```
Then, open your browser and navigate to ```http://localhost:5000``` to see the building rankings displayed in a simple table.


## Contributing
Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.
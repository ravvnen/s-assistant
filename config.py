import os
import json
import requests
from bs4 import BeautifulSoup
import logging
from dotenv import load_dotenv


load_dotenv()

# --- Configurations ---
LOGIN_URL = 'https://mit.s.dk/studiebolig/login/'
BUILDING_URL = 'https://mit.s.dk/studiebolig/building/'
API_URL = 'https://mit.s.dk/api/building/?parent=1&has_application_for=369538&exclude_auto=true'
OUTPUT_DIR = "scraped_data"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


# --- Authentication ---
def create_session():
    """Create an authenticated session."""
    session = requests.Session()
    login_page = session.get(LOGIN_URL)
    soup = BeautifulSoup(login_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    payload = {
        'username': USERNAME,
        'password': PASSWORD,
        'csrfmiddlewaretoken': csrf_token
    }
    headers = {'Referer': LOGIN_URL}
    login_response = session.post(LOGIN_URL, data=payload, headers=headers)
    if "Sign out" not in login_response.text:
        raise Exception("Login failed. Check credentials or URL.")
    print("Login succeeded.")
    return session

# --- API Data Fetching ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_all_buildings(session):
    url = 'https://mit.s.dk/api/building/?parent=1&has_application_for=369538&exclude_auto=true'
    pk_to_name = {}
    page = 1
    while url:
        logging.info(f"Fetching page {page}: {url}")
        try:
            response = session.get(url, timeout=10)
        except requests.exceptions.Timeout:
            logging.error(f"Timeout occurred on page {page}: {url}")
            break
        if response.status_code != 200:
            logging.error(f"Error {response.status_code} on page {page}: {url}")
            break
        data = response.json()
        results = data.get("results", [])
        logging.info(f"Fetched {len(results)} buildings on page {page}.")
        for item in results:
            pk_to_name[item["pk"]] = item["name"]
        url = data.get("next")
        page += 1
    logging.info(f"Total buildings fetched: {len(pk_to_name)}")
    return pk_to_name
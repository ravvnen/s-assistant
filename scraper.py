import os
from config import BUILDING_URL, OUTPUT_DIR
from bs4 import BeautifulSoup
import json


# --- Scraping ---
def scrape_building(session, building_id):
    """Scrape raw tenancy data from a building page."""
    url = f"{BUILDING_URL}{building_id}/"
    response = session.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch building {building_id}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    tenancy_rows = soup.select("table.tenancies-table tbody tr")
    tenancies = []
    for row in tenancy_rows:
        # Extract address and tenancy URL
        address_tag = row.find("td", string=lambda x: x is None)
        if address_tag:
            link = address_tag.find("a")
            address = link.get_text(strip=True) if link else ""
            tenancy_url = link['href'] if link and link.has_attr('href') else ""
        else:
            address, tenancy_url = "", ""
        # Extract area (expecting string like "Area:29 m2")
        cells = row.find_all("td")
        area = cells[1].get_text(strip=True) if len(cells) > 1 else ""
        # Extract ranking from the third cell
        ranking_a = row.find("a", class_="waiting-list-category-label")
        ranking_letter = ""
        data_content = ""
        if ranking_a:
            ranking_span = ranking_a.find("span", class_="waiting-list-category")
            if ranking_span:
                ranking_letter = ranking_span.get_text(strip=True)
            data_content = ranking_a.get("data-content", "")
        tenancy = {
            "address": address,
            "tenancy_url": tenancy_url,
            "area": area,
            "ranking": ranking_letter,
            "ranking_info": data_content
        }
        tenancies.append(tenancy)
    return tenancies

# --- Saving Data ---
def save_json(data, filename):
    """Save data as JSON into the output directory."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filepath}")
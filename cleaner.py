from scraper import scrape_building, save_json

# --- Cleaning ---
def clean_tenancies(raw_tenancies, building_name):
    """
    Clean raw tenancy data.
    Expected raw 'area' format: "Area:29 m2"
    Expected ranking_info contains last calculated time in <b> tags.
    """
    cleaned = []
    for tenancy in raw_tenancies:
        area_str = tenancy.get("area", "")
        try:
            area_value = int(area_str.split("Area:")[1].split("m")[0].strip())
        except (IndexError, ValueError):
            area_value = 0
        ranking = tenancy.get("ranking", "").replace("info_outline", "").strip()
        ranking_info = tenancy.get("ranking_info", "")
        last_calculated = ""
        recalculation_interval = ""
        if ranking_info:
            try:
                last_calculated = ranking_info.split("<b>")[1].split("</b>")[0].strip()
            except IndexError:
                pass
            try:
                recalculation_interval = ranking_info.split("<div>Recalculation occurs")[1].split("</div>")[0].strip()
            except IndexError:
                pass
        cleaned_record = {
            "building_name": building_name,
            "ranking": ranking,
            "last_calculated": last_calculated,
        }
        cleaned.append(cleaned_record)
    return cleaned

# --- Processing a Building ---
def process_building(session, building_id, building_name):
    raw_tenancies = scrape_building(session, building_id)
    raw_filename = f"building_{building_id}_data.json"
    save_json(raw_tenancies, raw_filename)
    cleaned = clean_tenancies(raw_tenancies, building_name)
    cleaned_filename = f"building_{building_id}_cleaned_data.json"
    save_json(cleaned, cleaned_filename)
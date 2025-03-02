import os
import json
import re

def query_best_buildings(data_folder="scraped_data"):
    """
    Scans cleaned JSON files in the data_folder (files ending with _cleaned_data.json),
    extracts the building ID from the filename, and determines the best (lowest letter)
    ranking for each building. Returns a sorted list of tuples (building_id, info)
    where info is a dict with building_name and best_ranking.
    """
    building_results = {}
    
    for filename in os.listdir(data_folder):
        if filename.endswith("_cleaned_data.json"):
            m = re.search(r'building_(\d+)_cleaned_data\.json', filename)
            if not m:
                continue
            building_id = m.group(1)
            filepath = os.path.join(data_folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                records = json.load(f)
            if not records:
                continue
            # Assume all records in a file have the same building_name.
            building_name = records[0].get("building_name", "Unknown")
            # Filter out records without a ranking (empty string)
            rankings = [r["ranking"] for r in records if r.get("ranking")]
            if rankings:
                # Lower alphabetical letters are better (e.g. A < B < C ...).
                best_ranking = min(rankings)
            else:
                best_ranking = None
            building_results[building_id] = {"building_name": building_name, "best_ranking": best_ranking}
    
    # Sort by ranking: convert the letter to its ordinal value so that 'A' comes first.
    # Buildings with no ranking are skipped in the sorted result.
    sorted_results = sorted(
        [(bid, info) for bid, info in building_results.items() if info["best_ranking"]],
        key=lambda x: ord(x[1]["best_ranking"])
    )
    return sorted_results

if __name__ == "__main__":
    results = query_best_buildings()
    print("Buildings sorted by best ranking:")
    for bid, info in results:
        print(f"Building ID: {bid}, Name: {info['building_name']}, Ranking: {info['best_ranking']}")

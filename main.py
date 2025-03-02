from config import create_session
from config import fetch_all_buildings
from cleaner import process_building

# --- Main ---
def main():
    session = create_session()  # your login/auth function
    pk_to_name = fetch_all_buildings(session)  # Now uses pagination
    for building_id, building_name in pk_to_name.items():
        print(f"\nProcessing building {building_name} (ID: {building_id})")
        process_building(session, building_id, building_name)

if __name__ == "__main__":
    main()
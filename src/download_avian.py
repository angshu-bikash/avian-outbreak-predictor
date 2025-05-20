import requests
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/AvianDashboard/Overview"

# Check if URL is accessible and print the final URL in case of redirects
response = requests.get(url, allow_redirects=True)
print("Final URL:", response.url)  # This will show the final URL after redirects

if response.status_code == 200:
    try:
        ts = TS()
        ts.loads(url)

        # List worksheets to confirm the one you need
        print("Worksheets available:", ts.getWorksheets())

        # Replace "Overall Findings" with the correct sheet name if different
        ws = ts.getWorksheet("Overall Findings")
        df = ws.data

        df.to_csv("avian_dashboard.csv", index=False)
        print("Saved avian_dashboard.csv with", len(df), "rows.")
    except Exception as e:
        print(f"Error loading Tableau data: {e}")
else:
    print(f"Failed to fetch data, status code: {response.status_code}")

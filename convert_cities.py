import json

with open('data/en/cities.min.json', encoding='utf-8') as f:
    all_cities = json.load(f)

# Keep only English labels
cleaned = {}

for entry in all_cities:
    country = entry['country']
    cities = entry['cities']
    cleaned[country] = [{'label': city['label']} for city in cities]

with open('data/en/cities.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)

print(f'Cleaned {len(cleaned)} countries')

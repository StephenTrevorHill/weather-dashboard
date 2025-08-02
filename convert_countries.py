import json

# Load the original file
with open('data/en/countries.min.json', encoding='utf-8') as f:
    original = json.load(f)

# Keep only the 'label' key
english_only = [{'label': item['label']} for item in original]

# Save the cleaned-up version (overwrite or write to a new file)
with open('data/en/countries.json', 'w', encoding='utf-8') as f:
    json.dump(english_only, f, indent=2, ensure_ascii=False)

print(f'Cleaned {len(english_only)} entries.')

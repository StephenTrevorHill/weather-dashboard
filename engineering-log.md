# Engineering Log – Weather Dashboard

This document tracks key development milestones, decisions, and learnings.

---

## [2024-07-20] Project Kickoff
- Initialized Flask project with weather API
- Created virtual environment, `.gitignore`, and `requirements.txt`
- Built basic Flask route and form to fetch weather data
- Committed initial version and tagged as `v0.1`

---

## [2024-07-21] Added AQI support
- Integrated OpenWeatherMap air pollution API
- Used lat/lon from weather API to fetch AQI
- Added named pollutant mapping using Python dict
- Updated UI to show pollutants in a styled table
- Tagged version as `v0.2`
- Commits:
- 2025-07-21 Add /api/weather endpoint and initial curl test support
- 2025-07-21 initisl commit

---

## [2024-07-22] Testing
- Created `tests/` folder and added `pytest.ini`
- Wrote tests for:
  - `/` GET and POST behavior
  - AQI table row count
  - HTML structure using BeautifulSoup
- Created feature branch `feature/add-tests`
- Merged to `main` via GitHub PR 
- Updated Jira
- Commits:
- Add styled pollutant table with readable labels and AQI
- SMP-10 Add unit tests for basic functionality

---

## [2024-07-23] Deployment

- Cleaned up `requirements.txt` and added `gunicorn`
- Created Procfile to run `gunicorn app:app`
- Connected GitHub repo to Render
- Set `OPENWEATHER_API_KEY` as an environment variable
- Deployed successfully to: https://weather-dashboard-4nqf.onrender.com
- Tagged version as `v0.3`


## [2025-07-30] Tooling and Code Quality

- Installed and configured Ruff for linting and formatting
- Enabled Ruff auto-formatting in VS Code (`.toml` + settings.json)
- Set up `pre-commit` with Ruff hooks to run checks before every commit
- Added manual `ruff format .` and `ruff check .` usage to workflow
- Verified pre-commit behavior with test commits (unused imports, etc.)
- Test badge added to `README.md`

---

## [2025-07-31] GitHub CI + PR Enforcement

- Created `test.yml` GitHub Actions workflow to run tests
- Added `OPENWEATHER_API_KEY` as GitHub secret for CI runs
- Required passing tests before merge (GitHub ruleset)
- Tested failing + fixed commits to validate pipeline behavior
- Signed up for RapidAPI using Github

## [2024-08-01] Country/City Picker + Styling + Tests

- Added JavaScript-based country and city pickers
- Replaced stub API with local JSON data
- Styled the form inputs (font size, spacing)
- Wrote tests for country/city integration
- Updated linter config (Ruff + formatter)
- Tagged version as `v0.5`

## [2024-08-02]
- simplified format of json files - SMP-17 Clean up formatting of JSON files - changed/tested/merged
- removed and then re-added engineering log to tracking


## To-Dos ##
- logging
- better handling of errors
- ?? AI integration ??
- ?? containers? ??


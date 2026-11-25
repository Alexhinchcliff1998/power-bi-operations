# Freight Performance | Power BI Case Study

Reproducible dimensional BI model for 1,000 fictional shipments. Includes data generator, eight DAX measures, reference metrics and an HTML preview. This is not a native Power BI report; follow POWER_BI_BUILD.md to build a PBIX in Power BI Desktop.

```bash
python generate_data.py
python reference_dashboard.py
pip install -r requirements.txt
python -m pytest -q
```
Open preview.html after generation. Independent AI-assisted demonstration using synthetic data.

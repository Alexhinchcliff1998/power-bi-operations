# Rebuild in Power BI Desktop

1. Run python generate_data.py and python reference_dashboard.py. Import the four CSVs in data/ as tables named fact_shipments, dim_date, dim_carrier and dim_region.
2. Set Date and ShipDate to Date; IDs, Miles and delivery days to Whole Number; Cost to Decimal Number.
3. Create single-direction one-to-many relationships from dim_date[Date], dim_carrier[CarrierID] and dim_region[RegionID] to the corresponding fact columns. Mark dim_date as date table and sort Month by MonthNumber.
4. Create the eight measures in measures.dax separately. Format On Time % as percentage and cost measures as USD.
5. Build KPI cards, carrier on-time bar chart, monthly shipment volume and regional table. Add carrier and region slicers.
6. Compare unfiltered totals with reference_metrics.json, test filters and save as FreightPerformance.pbix.

No native PBIX is supplied or claimed verified.

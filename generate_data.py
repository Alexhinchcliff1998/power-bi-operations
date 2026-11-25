import csv, random
from datetime import date,timedelta
from pathlib import Path
BASE=Path(__file__).parent/'data'
def write(name,fields,rows):
    BASE.mkdir(exist_ok=True)
    with (BASE/name).open('w',newline='') as f:
        out=csv.writer(f);out.writerow(fields);out.writerows(rows)
def generate():
    r=random.Random(81);start=date(2025,1,1)
    carriers=[(1,'Atlas Freight'),(2,'Cedar Logistics'),(3,'Harbor Transit'),(4,'Pine Express')];regions=[(1,'East'),(2,'Central'),(3,'West')]
    dates=[(start+timedelta(days=i)).isoformat() for i in range(365)]
    write('dim_date.csv',['Date','Year','MonthNumber','Month'],[(d,2025,int(d[5:7]),date.fromisoformat(d).strftime('%b')) for d in dates]);write('dim_carrier.csv',['CarrierID','Carrier'],carriers);write('dim_region.csv',['RegionID','Region'],regions)
    rows=[]
    for i in range(1000):
        carrier=r.choice(carriers)[0];region=r.choice(regions)[0];miles=r.randint(80,1800);promised=r.randint(2,7);late=r.random()<[.08,.19,.12,.27][carrier-1];actual=promised+r.randint(1,3) if late else max(1,promised-r.randint(0,2));cost=round(110+miles*r.uniform(1.15,1.85),2)
        rows.append((i+1,r.choice(dates),carrier,region,miles,cost,promised,actual))
    write('fact_shipments.csv',['ShipmentID','ShipDate','CarrierID','RegionID','Miles','Cost','PromisedDays','ActualDays'],rows)
if __name__=='__main__':generate()

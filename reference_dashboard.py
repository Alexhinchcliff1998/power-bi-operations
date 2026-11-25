import csv,json,html
from pathlib import Path
from collections import defaultdict
P=Path(__file__).parent
def read(name):
    with (P/'data'/name).open() as f:return list(csv.DictReader(f))
def metrics(rows):
    n=len(rows);cost=sum(float(r['Cost']) for r in rows);miles=sum(int(r['Miles']) for r in rows);on=sum(int(r['ActualDays'])<=int(r['PromisedDays']) for r in rows)
    return {'shipments':n,'on_time':on,'late':n-on,'on_time_pct':round(100*on/n,2) if n else 0,'cost':round(cost,2),'miles':miles,'cost_per_mile':round(cost/miles,4) if miles else 0}
def main():
    rows=read('fact_shipments.csv');carriers={r['CarrierID']:r['Carrier'] for r in read('dim_carrier.csv')};region={r['RegionID']:r['Region'] for r in read('dim_region.csv')};by=defaultdict(list);by_region=defaultdict(list);by_month=defaultdict(list)
    for row in rows:by[carriers[row['CarrierID']]].append(row);by_region[region[row['RegionID']]].append(row);by_month[row['ShipDate'][:7]].append(row)
    m=metrics(rows);(P/'reference_metrics.json').write_text(json.dumps({'overall':m,'carriers':{k:metrics(v) for k,v in sorted(by.items())},'regions':{k:metrics(v) for k,v in sorted(by_region.items())},'months':{k:metrics(v) for k,v in sorted(by_month.items())}},indent=2))
    bars=''.join(f'<p>{html.escape(k)} <meter min="0" max="100" value="{metrics(v)["on_time_pct"]}"></meter> {metrics(v)["on_time_pct"]:.1f}%</p>' for k,v in sorted(by.items()))
    regions=''.join(f'<tr><td>{html.escape(k)}</td><td>{metrics(v)["shipments"]}</td><td>{metrics(v)["on_time_pct"]:.1f}%</td><td>${metrics(v)["cost"]:,.0f}</td></tr>' for k,v in sorted(by_region.items()))
    months=''.join(f'<p>{k} <meter min="0" max="120" value="{len(v)}"></meter> {len(v)}</p>' for k,v in sorted(by_month.items()))
    (P/'preview.html').write_text(f"""<!doctype html><html lang="en"><meta charset="utf-8"><title>Freight Performance</title><style>body{{font:16px system-ui;background:#eff3f7;color:#183047;max-width:1000px;margin:auto;padding:30px}}header{{background:#193751;color:white;padding:25px;border-radius:12px}}section{{background:white;border:1px solid #dce4ee;border-radius:12px;padding:20px;margin:15px 0}}meter{{width:45%;height:20px}}table{{width:100%;text-align:left;border-collapse:collapse}}th,td{{border-bottom:1px solid #dce4ee;padding:12px}}</style><header><h1>Freight performance</h1><p>Reference dashboard · synthetic data</p></header><section><h2>{m['shipments']:,} shipments | {m['on_time_pct']:.1f}% on time</h2><p>Total cost: ${m['cost']:,.2f} · Cost per mile: ${m['cost_per_mile']:.4f}</p></section><section><h2>On-time delivery by carrier</h2>{bars}</section><section><h2>Monthly shipment volume</h2>{months}</section><section><h2>Regional performance</h2><table><tr><th>Region</th><th>Shipments</th><th>On time</th><th>Cost</th></tr>{regions}</table></section></html>""")
if __name__=='__main__':main()

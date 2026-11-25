from reference_dashboard import metrics
from generate_data import generate
from reference_dashboard import read
def test_metrics():
    rows=[{'Cost':'100','Miles':'50','ActualDays':'2','PromisedDays':'2'},{'Cost':'50','Miles':'50','ActualDays':'3','PromisedDays':'2'}]
    result=metrics(rows);assert result['on_time_pct']==50 and result['cost_per_mile']==1.5 and result['late']==1
def test_fixture():
    generate();rows=read('fact_shipments.csv');assert len(rows)==1000 and len({r['ShipmentID'] for r in rows})==1000

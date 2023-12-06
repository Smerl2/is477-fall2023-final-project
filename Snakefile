
rule prepare:
  output:
    "data/online_retail.csv"
  shell:
    "python scipts/prepare_data.py" 

rule profile:
  input: 
    "data/online_retail.csv"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input: 
    "data/online_retail.csv"
  output:
    "results/analysis_results"
  shell:
    "python script/analysis.py"



    







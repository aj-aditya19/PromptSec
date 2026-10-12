import pandas as pd, numpy as np
from scipy.stats import fisher_exact
ai=pd.read_csv('results/per_file.csv'); h=pd.read_csv('results/human.csv')
def rate(df,col):
    s=df[col]; return int((s==True).sum()), len(s)
out=[]
H={c:rate(h,c) for c in ['vulnerable','test_vuln']}
out.append("HUMAN (20 files): combined %d/20, confirmed-by-test %d/20; functional pass %d/%d"%(H['vulnerable'][0],H['test_vuln'][0],(h.func==True).sum(),h.func.notna().sum()))
rows=[]
for col,name in [('vulnerable','combined (test OR Bandit CWE)'),('test_vuln','confirmed by test only')]:
    for scope,df in [('ALL AI (400)',ai)]+[(m+' (80)',ai[ai.model==m]) for m in sorted(ai.model.unique())]:
        a,n=rate(df,col); ha,hn=H[col]
        _,p=fisher_exact([[ha,hn-ha],[a,n-a]])
        rows.append(dict(metric=name,group=scope,ai_vuln=f"{a}/{n}",ai_pct=round(100*a/n,1),human=f"{ha}/{hn}",human_pct=round(100*ha/hn,1),fisher_p=round(p,5)))
out.append("\n## Human vs AI (Fisher exact, treats files as independent; AI files are clustered in chats so p is optimistic)\n"+pd.DataFrame(rows).to_string(index=False))
# per task matrix
m=ai.pivot_table(index='task',columns='model',values='test_vuln',aggfunc=lambda s:int((s==True).sum()))
m['AI_total_of_20']=m.sum(axis=1)
m.insert(0,'human_vuln',h.set_index('task').test_vuln.map(lambda x:int(x==True)))
m.insert(1,'human_func_ok',h.set_index('task').func.map(lambda x:int(x==True)))
out.append("\n## Per task: human (1 file) vs AI vulnerable counts by model (confirmed by test, of 4 variants)\n"+m.to_string())
hv=set(h[h.test_vuln==True].task); aiv=set(ai[ai.test_vuln==True].task)
out.append("\nTasks where human is vulnerable but NO AI file is: %s"%sorted(t for t in hv if (ai[(ai.task==t)].test_vuln==True).sum()==0))
out.append("Tasks where human is vulnerable AND some AI file is: %s"%sorted(t for t in hv if (ai[(ai.task==t)].test_vuln==True).sum()>0))
open('results/human_vs_ai.txt','w').write("\n".join(out)); print("\n".join(out))

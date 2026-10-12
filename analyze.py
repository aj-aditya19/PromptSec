import pandas as pd, numpy as np, json
from scipy.stats import binomtest
d=pd.read_csv('results/per_file.csv')
d['confirmed']=d.test_vuln.astype('boolean'); d['combined']=d.vulnerable.astype('boolean')
d['bandit_only']=(d.combined==True)&(d.confirmed!=True)
V=['original','typo','synonym','paraphrase']
def tab(col):
    return d.pivot_table(index='model',columns='variant',values=col,aggfunc=lambda s:int((s==True).sum()))[V]
out=[]
for col,name in [('combined','COMBINED rule (test OR Bandit CWE hit) - pre-registered'),('confirmed','CONFIRMED by test only (no Bandit-only flags)')]:
    t=tab(col); t['total']=t.sum(axis=1); t.loc['ALL']=t.sum()
    out.append(f"## {name}: vulnerable files per model x variant (of 20 per cell)\n"+t.to_string()+"\n")
def mcnemar(col,v,models=None):
    a=d[(d.variant=='original')]; b=d[(d.variant==v)]
    if models: a=a[a.model.isin(models)]; b=b[b.model.isin(models)]
    m=a.merge(b,on=['model','task'],suffixes=('_o','_v'))
    x=m[f'{col}_o']==True; y=m[f'{col}_v']==True
    n10=int((x&~y).sum()); n01=int((~x&y).sum())
    p=1.0 if n10+n01==0 else binomtest(n01,n10+n01,0.5).pvalue
    return n10,n01,p
def holm(ps):
    o=np.argsort(ps); m=len(ps); adj=np.empty(m); run=0
    for i,k in enumerate(o): run=max(run,(m-i)*ps[k]); adj[k]=min(1,run)
    return adj
for col in ['combined','confirmed']:
    rows=[]
    for scope,ms in [('ALL 5 models',None)]+[(m,[m]) for m in sorted(d.model.unique())]:
        ps=[];tmp=[]
        for v in V[1:]:
            n10,n01,p=mcnemar(col,v,ms); ps.append(p); tmp.append((scope,v,n10,n01,p))
        adj=holm(np.array(ps))
        for (s,v,n10,n01,p),a in zip(tmp,adj): rows.append(dict(scope=s,variant=v,orig_only_vuln=n10,variant_only_vuln=n01,p_exact=round(p,4),p_holm=round(a,4)))
    out.append(f"## McNemar exact, {col}: variant vs original (paired by model+task). orig_only = vulnerable in original but not variant; variant_only = the reverse\n"+pd.DataFrame(rows).to_string(index=False)+"\n")
t=d.groupby('task').agg(combined=('combined',lambda s:int((s==True).sum())),confirmed=('confirmed',lambda s:int((s==True).sum())),bandit_only=('bandit_only','sum'))
out.append("## Per task (of 20 files)\n"+t.to_string()+"\n")
# flag type breakdown
import collections
c=collections.Counter()
for f in d['flags'].dropna(): 
    for k in json.loads(f): c[k]+=1
out.append("## Confirmed flag types (file counts)\n"+"\n".join(f"{k}: {v}" for k,v in c.most_common())+"\n")
out.append("## Bandit-only (not confirmed by test) by task\n"+d[d.bandit_only].groupby('task').size().to_string()+"\n")
func=d.groupby('model').agg(testable=('func',lambda s:int(s.notna().sum())),passed=('func',lambda s:int((s==True).sum())),not_testable=('func',lambda s:int(s.isna().sum())))
out.append("## Functional tests\n"+func.to_string()+"\n")
open('results/summary.txt','w').write("\n".join(out)); print("\n".join(out))

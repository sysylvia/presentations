"""Generate the editable aggregate-only China RCT forest plots for the main summary."""
from pathlib import Path
import json,html
P=Path(__file__).resolve().parent
D=json.loads((P/'evidence.json').read_text())
N='#13294B';B='#4B9CD3';S='#64748B';L='#E8E6E1'
def t(x,y,s,size=33,color=N,anchor='start',weight=400):
 return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(str(s))}</text>'
def ln(x1,y1,x2,y2,color=L,width=2,extra=''):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>'
def ci(v,lo,hi,scale,y):
 x=scale(v);a=scale(lo);b=scale(hi)
 return [ln(a,y,b,y,B,5),ln(a,y-11,a,y+11,B,3),ln(b,y-11,b,y+11,B,3),f'<circle cx="{x}" cy="{y}" r="10" fill="{N}"/>']
e=[t(0,40,'Primary outcomes',38,weight=600),t(875,40,'Selected secondary outcomes',38,weight=600),ln(825,15,825,585,L)]
settings=[('Hemoglobin (g/L)',1,(-2.5,2.5),[-2,0,2]),('Exclusive breastfeeding (pp)',100,(-10,20),[-10,0,10,20]),('Dietary diversity (food groups)',1,(-.1,.5),[0,.2,.4])]
for i,(q,cfg) in enumerate(zip(D['primary'],settings)):
 label,mult,(lo,hi),ticks=cfg;y=110+i*175;scale=lambda v:235+(v-lo)/(hi-lo)*540
 est=q['estimate']*mult
 e += [t(0,y,label,34),t(780,y,f'{est:+.2f}' if mult==1 else f'{est:+.1f}',33,anchor='end'),ln(scale(0),y+15,scale(0),y+65,S,2,'stroke-dasharray="5 6"')]
 e += ci(est,q['lower95']*mult,q['upper95']*mult,scale,y+38)
 for tick in ticks:e += [ln(scale(tick),y+70,scale(tick),y+77,S,1.5),t(scale(tick),y+108,f'{tick:g}',29,S,'middle')]
 e += [ln(235,y+70,775,y+70,S,1.5)]
labels=['Child illness, prior 2 weeks','Caregiver depression symptoms','Caregiver anxiety symptoms','Caregiver stress symptoms']
scale=lambda v:1100+(v+16)/20*475
for i,(q,label) in enumerate(zip(D['selected_secondary'],labels)):
 y=110+i*118
 e += [t(875,y,label,33),t(1638,y,f'{q["estimate"]*100:+.1f}',33,anchor='end')]
 e += ci(q['estimate']*100,q['lower95']*100,q['upper95']*100,scale,y+38)
e += [ln(scale(0),127,scale(0),530,S,2,'stroke-dasharray="5 6"'),ln(1100,535,1575,535,S,1.5)]
for tick in [-16,-12,-8,-4,0,4]:e += [ln(scale(tick),535,scale(tick),542,S,1.5),t(scale(tick),573,tick,29,S,'middle')]
e += [t(1338,615,'Difference (percentage points)',31,S,'middle'),t(0,615,'Dots: ITT estimates   Lines: 95% confidence intervals',31,S)]
svg='<svg xmlns="http://www.w3.org/2000/svg" class="evidence-svg" viewBox="0 0 1650 640" role="img" aria-label="China trial primary and selected secondary forest plots with 95 percent confidence intervals"><style>text{font-family:Times,serif}</style>'+''.join(e)+'</svg>'
(P/'figures/trial-summary.qmd').write_text('```{=html}\n'+svg+'\n```\n')
print('Generated trial summary from evidence.json; no new estimates')

"""Build editable SVG figures from published aggregate estimates and verified architecture.

No participant records are read. Run with Python's standard library only.
"""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "evidence.json").read_text())
NAVY, BLUE, INK, SLATE, STONE = "#13294B", "#4B9CD3", "#334155", "#64748B", "#E8E6E1"


def text(x, y, value, size=36, color=INK, weight=400, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(str(value))}</text>'


def line(x1, y1, x2, y2, color=STONE, width=2, arrows=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {arrows}/>'


def svg(name, height, title, elements):
    head = f'<svg class="evidence-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1650 {height}" role="img" aria-labelledby="{name}-title"><title id="{name}-title">{html.escape(title)}</title>'
    markers = f'<defs><marker id="{name}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{BLUE}"/></marker></defs>'
    body = head + markers + "\n".join(elements) + "</svg>"
    (ROOT / "figures" / f"{name}.qmd").write_text("```{=html}\n" + body + "\n```\n")


def primary():
    elements = []
    spec = [(-2, 2, [-2, -1, 0, 1, 2], "g/L", "−0.382 [−1.964, 1.200]"),
            (-10, 20, [-10, 0, 10, 20], "percentage points", "+5.7 [−6.0, 17.4]"),
            (-.1, .5, [-.1, .1, .3, .5], "food groups", "+0.207 [0.015, 0.399]")]
    for i, (q, (lo, hi, ticks, unit, estimate_text)) in enumerate(zip(DATA["primary"], spec)):
        left = i * 550 + 28
        width = 466
        scale = lambda v: left + (v-lo)/(hi-lo)*width
        factor = 100 if i == 1 else 1
        elements.append(text(left+width/2, 46, q["outcome"], 38, NAVY, 600, "middle"))
        for tick in ticks:
            elements.append(line(scale(tick), 80, scale(tick), 332))
            elements.append(text(scale(tick), 375, f"{tick:g}", 31, SLATE, anchor="middle"))
        elements.append(line(scale(0), 80, scale(0), 332, SLATE, 2))
        elements.append(line(left, 332, left+width, 332, SLATE, 1.5))
        elements.append(line(scale(q["lower95"]*factor), 210, scale(q["upper95"]*factor), 210, BLUE, 5))
        elements.append(f'<circle cx="{scale(q["estimate"]*factor)}" cy="210" r="9" fill="{BLUE}"/>')
        elements.append(text(left+width/2, 428, unit, 33, INK, 600, "middle"))
        elements.append(text(left+width/2, 502, estimate_text, 34, NAVY, 600, "middle"))
        elements.append(text(left+width/2, 562, f'N = {q["n_observed"]}', 31, SLATE, anchor="middle"))
    svg("primary", 600, "Primary ITT estimates with 95 percent confidence intervals, in separate units and scales", elements)


def secondary():
    elements = [text(960, 45, "ITT effects, 95% CI", 38, NAVY, 600, "middle"), text(1460, 45, "ITT [95% CI]", 32, SLATE, 600, "middle")]
    scale = lambda v: 635 + (v+16)/20*650
    for tick in [-16, -12, -8, -4, 0, 4]:
        elements += [line(scale(tick), 88, scale(tick), 474), text(scale(tick), 520, tick, 31, SLATE, anchor="middle")]
    elements += [line(scale(0), 88, scale(0), 474, SLATE), line(635,474,1285,474,SLATE,1.5)]
    labels = ["Child illness, prior 2 weeks", "Caregiver depression symptoms", "Caregiver anxiety symptoms", "Caregiver stress symptoms"]
    labels_ci = ["−8.2 [−14.0, −2.4]", "−6.3 [−10.8, −1.8]", "−4.9 [−8.9, −0.9]", "−4.2 [−8.0, −0.3]"]
    for i, (q, label, value) in enumerate(zip(DATA["selected_secondary"], labels, labels_ci)):
        y = 145 + 92*i
        elements += [text(0,y+12,label,35), line(scale(q["lower95"]*100),y,scale(q["upper95"]*100),y,BLUE,5), f'<circle cx="{scale(q["estimate"]*100)}" cy="{y}" r="9" fill="{BLUE}"/>', text(1460,y+12,value,31,NAVY,anchor="middle")]
    elements.append(text(960,585,"Difference (percentage points)",33,INK,600,"middle"))
    svg("secondary", 610, "Selected secondary ITT estimates with 95 percent confidence intervals, in percentage points", elements)


def node(x, y, w, h, title, body=()):
    elements = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{BLUE}" stroke-width="2.5"/>', text(x+22,y+48,title,37,NAVY,600)]
    elements.extend(text(x+22,y+97+i*43,t,33) for i,t in enumerate(body))
    return elements


def architecture():
    e = node(0,55,450,190,"Curriculum editor",["Lessons, topic modules,", "scripts and media"])
    e += node(600,55,450,190,"Spring Boot API",["Scheduling and", "content delivery"])
    e += node(1200,55,450,190,"CHW Android app",["Render the configured", "visit content"])
    e += node(600,390,450,145,"MySQL",["Curriculum and visit records"])
    tail = 'marker-end="url(#backend-arrow)"'
    both = tail + ' marker-start="url(#backend-arrow)"'
    e += [line(450,150,600,150,BLUE,3,tail),line(1050,150,1200,150,BLUE,3,both),line(825,245,825,390,BLUE,3,both)]
    e += [text(0,414,"Stage, age and prior visits",35),text(0,460,"feed the scheduling rules.",35),text(1200,414,"The app returns visit",35),text(1200,460,"completion and responses.",35)]
    svg("backend",570,"CareLoom curriculum editor, Spring Boot API, MySQL records and CHW Android app",e)


def branching():
    e = node(0,25,450,105,"Lesson / visit session") + node(600,25,450,105,"Topic modules") + node(1200,25,450,105,"Components")
    tail = 'marker-end="url(#branching-arrow)"'
    e += [line(450,78,600,78,BLUE,3,tail),line(1050,78,1200,78,BLUE,3,tail),text(865,190,"Scripts, media and branching questions",33,SLATE),text(0,270,"Illustrative configured question",33,SLATE)]
    e += node(485,310,680,100,"“Revisit this topic?”")
    e += node(0,495,720,100,"Yes: reinforcement content") + node(930,495,720,100,"No: continue the session")
    e += [f'<path d="M 485 360 H 350 V 495" fill="none" stroke="{BLUE}" stroke-width="3" {tail}/>',f'<path d="M 1165 360 H 1290 V 495" fill="none" stroke="{BLUE}" stroke-width="3" {tail}/>']
    svg("branching",620,"Curriculum hierarchy and an illustrative configured yes/no content path",e)


if __name__ == "__main__":
    for build in [primary, secondary, architecture, branching]:
        build()

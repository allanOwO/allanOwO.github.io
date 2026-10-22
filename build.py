"""Regenerates every page from the PROJECTS list. Edit the data, run: python build.py"""
import html
E=html.escape
NAME="Allan Blyth"; EMAIL="allanjwb@gmail.com"; CV="Allan_Blyth_CV.pdf"
ITCH="https://allanowo.itch.io"; LI="https://www.linkedin.com/in/allan-blyth-32977b403/"; GH="https://github.com/allanOwO"
def P(slug,title,kind,meta,summary,cover,group,tags,role,bullets,learned,itch,label,video="",yt=""):
    return dict(slug=slug,title=title,kind=kind,meta=meta,summary=summary,cover=cover,group=group,tags=tags,role=role,bullets=bullets,learned=learned,itch=itch,label=label,video=video,yt=yt)
PROJECTS=[
P("kyomen","Kyomen","Isometric action roguelike","Programmer, Marmot Studios | Global Game Jam 2026, now heading to Steam",
 "Don't let the weight of your past collapse the world. A fast-paced isometric arena combat game built around dynamic mask-based gameplay, started as a Global Game Jam 2026 entry and now in development by Marmot Studios for Steam.",
 "https://img.itch.zone/aW1nLzI1MzU2MTE1LnBuZw==/original/HTEPdh.png","feat",["Unity","C#","State machines","Boss AI"],
 "I work on the combat programming that drives the game's encounters: escalating pressure, how enemies approach the player, and a boss reactive enough that fights feel less predictable. After the jam, the team of five formed Marmot Studios Ltd to take the game to release.",
 ["Designed and built a four-phase boss fight on state machines, with weighted attack selection and coroutine-based timing.","Designed and implemented the enemy wave system to control encounter pacing.","Created enemy movement and attack behaviours, coordinating navigation and combat states.","Implemented boss attack patterns and reactive decision-making that respond to the player's actions.","Iterated from jam prototype to a playable demo."],
 "Designing gameplay systems under a tight deadline, then hardening them for a real release. Balancing reusable enemy logic against the specific needs of a boss encounter.",
 "4250442","https://ath3rox.itch.io/kyomen|Kyomen by Ath3rox, qlxiy, Bishop, KyleMc04, Ryanmcg04, Allan"),
P("ballad-of-auld-dunrod","The Ballad of Auld Dunrod","Third-person stealth exploration","Programming Lead | Client project for a comic book publisher | Browser game",
 "A third-person stealth exploration game based on a Scottish folklore poem, in which the player helps Dunrod escape capture.",
 "https://img.itch.zone/aW1nLzIwNzE2NDY4LnBuZw==/original/e%2BdR4d.png","unity",["Unity","C#","WebGL","Stealth AI"],
 "I led the programming team from development through delivery: coordinating technical work, prioritising features, and making sure the game was stable and complete enough to present as a client project.",
 ["Created guard behaviour to support the stealth loop and give the player readable threats.","Built a dynamic top-down camera system to keep the player oriented.","Optimised for web deployment on mobile browsers and school iPads, where performance and input options were limited."],
 "Leadership, prioritisation, browser optimisation and team delivery against a clear client-facing goal.",
 "3041421","https://gcugames.itch.io/ballad-of-auld-dunrod|Ballad of Auld Dunrod by Glasgow Caledonian University, Patricija Gudynaite, Blitz_Maxis, SkrubJG, Allan, Bishop",yt="uGwDVG2_ZKo"),
P("tower-of-tales","Tower of Tales","Arena shooter","Gameplay Programmer | Team project",
 "A short arena shooter inspired by Arena of the Mad King, The Binding of Isaac and Realm of the Mad God. A cultist enters the arena to defeat the boss and bring back their family.",
 "https://img.itch.zone/aW1nLzI2OTAwMDEyLmpwZw==/original/omEVot.jpg","unity",["Unity","C#","Boss AI","Controller input"],
 "I worked on the player and boss gameplay loop, focusing on responsive movement and an encounter that reacts to the player's position and actions.",
 ["Created boss attack patterns and reactive decision-making to structure the main encounter.","Implemented player movement and tuned its feel for arena combat.","Added controller support so the game plays well across input devices."],
 "Encounter design, input abstraction, and how boss behaviour can communicate patterns while still demanding player adaptation.",
 "2672862","https://qlxiy.itch.io/tower-of-tales|Tower of Tales by qlxiy, Allan, PastorYoda216, Patricija Gudynaite, ashxy, beansTM",yt="i9INBV4BUcI"),
P("bob-steve","Bob n' Steve","Cooperative action","Programmer | Team project",
 "Four soldiers, one string, a field that wants you dead. A cooperative action game with a shared string as its central teamwork mechanic.",
 "https://img.itch.zone/aW1nLzI5OTIwNDEzLnBuZw==/original/qetc6E.png","unity",["Unity","C#","Multiplayer","Voice chat"],
 "I focused on the systems that connect the players and make cooperation meaningful. The string needed gameplay logic that supported a group while staying readable and responsive in combat.",
 ["Designed and implemented the shared-string mechanic linking the soldiers.","Contributed to the in-game voice communication system.","Implemented and integrated multiple weapon systems."],
 "Multiplayer-focused gameplay, explaining technical ideas within a team, and building mechanics that reinforce a game's core identity.",
 "4997416","https://ath3rox.itch.io/bob-steve|Bob n' Steve by Ath3rox, Bishop, KyleMc04, Charlie Turnbull - qlxiy, Allan"),
P("chill-fishing-game","Just a Chill Fishing Game","Relaxed fishing game","Gameplay Programmer | 48-hour jam | Global Game Jam 2025",
 "Explore the deepest depths, discover fish and make Marty proud in this relaxed fishing game.",
 "https://img.itch.zone/aW1nLzE5NTQ2NzQwLmpwZw==/original/ML78Ot.jpg","unity",["Unity","C#","Game jam"],
 "I helped take the game from concept to a complete playable release within 48 hours, focusing on fishing, discovering life underwater and making the environment feel active.",
 ["Designed and implemented the core fishing mechanic, from player interaction to catch feedback.","Implemented fish behaviours that make exploration rewarding.","Created bubble behaviours and environmental feedback for movement and atmosphere."],
 "Scoping features, iterating quickly, and delivering polished gameplay under a strict time limit.",
 "3271726","https://allanowo.itch.io/just-a-chill-fishing-game|Just a Chill Fishing Game by Allan, qlxiy, Ath3rox, Bishop, KyleMc04"),
P("voxel-world","Voxel World Prototype","OpenGL voxel engine","Solo programmer | C++ | OpenGL",
 "A voxel world built from the ground up to explore procedural generation, real-time lighting, world interaction and collision. My first OpenGL project.",
 "https://img.itch.zone/aW1nLzI1MDE3MTYxLnBuZw==/original/%2BL%2BNqm.png","gl",["C++","OpenGL","Procedural generation"],
 "A practical exploration of low-level rendering and engine development. Rather than relying on a pre-built world system, I implemented the core systems needed to create and interact with a large voxel environment.",
 ["Built an infinite procedural world on a chunk-based system.","Implemented real-time directional sunlight with voxel-cast shadows.","Created interactive block modification so players can change the terrain.","Implemented AABB collision for reliable movement through voxel terrain."],
 "C++, OpenGL rendering, procedural systems, spatial organisation and lighting, and the challenges of building engine functionality from scratch.",
 "4197600","https://allanowo.itch.io/voxel-world-prototype|Voxel World Prototype by Allan"),
P("asteroids","Asteroids","Space shooter prototype","Solo programmer | C++ | OpenGL",
 "An arcade-inspired space shooter with procedural asteroid fields and a PS2-inspired low-poly look, built to develop my C++ and OpenGL experience.",
 "https://img.itch.zone/aW1nLzI5OTQ3MTI2LnBuZw==/original/jQ8lWB.png","gl",["C++","OpenGL","Low-poly"],
 "I built it to get more practical C++ and OpenGL experience while recreating the readable loop of a classic asteroid shooter, with a deliberately retro visual direction.",
 ["Developed the rendering and gameplay systems in OpenGL.","Implemented procedural asteroid generation for varied play spaces.","Created an explosion system with visual effects and responsive feedback.","Built a cohesive PS2-inspired low-poly style through rendering and presentation."],
 "Real-time rendering, procedural content, gameplay feedback, and how technical constraints can set a consistent visual identity.",
 "5002358","https://allanowo.itch.io/asteroids|Asteroids by Allan"),
]
def page(title,desc,img,body,path="",cls=""):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{E(img)}"><meta name="theme-color" content="#15111f">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23ff4d5e'/%3E%3Cpath d='M8 24 16 8l8 16' fill='none' stroke='%2315111f' stroke-width='4'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;600;700&display=swap">
<link rel="stylesheet" href="style.css"></head><body>
<div class="hp"><div class="hp-in"><span class="hp-label" aria-hidden="true">Phase 1 of 4</span><div class="hp-bar" aria-hidden="true"><i class="hp-lag"></i><i class="hp-fill"></i></div><nav aria-label="Main"><a href="index.html">Home</a><a href="index.html#work">Work</a><a href="index.html#contact">Contact</a></nav></div></div>
<main>{body}</main>
<footer><div class="wrap">&copy; 2026 {NAME}. Gameplay programmer, Scotland.</div></footer><script src="script.js"></script></body></html>'''
def card(p):
    return f'<a class="card" href="{p["slug"]}.html"><img src="{p["cover"]}" alt="{E(p["title"])} cover image" loading="lazy"><h3>{E(p["title"])}</h3><p>{E(p["kind"])}. {E(p["bullets"][0])}</p></a>'
def tags(p): return '<ul class="tags">'+"".join(f"<li>{E(t)}</li>" for t in p["tags"])+"</ul>"
def index():
    k=PROJECTS[0]; g=lambda n:"".join(card(p) for p in PROJECTS if p["group"]==n)
    b=f'''<div class="wrap"><div class="hero"><h1>Bosses that fight back.</h1>
<p>I'm Allan, a gameplay programmer specialising in enemy AI and multi-phase boss systems in Unity and C#. 2:1 in Games Development from Glasgow Caledonian University, co-founder of Marmot Studios Ltd, and also a C++/OpenGL engine programmer.</p>
<div class="btns"><a class="btn main" href="{CV}">Download CV</a><a class="btn" href="{k["slug"]}.html">See the Kyomen boss</a><a class="btn" href="mailto:{EMAIL}">Email me</a></div></div></div>
<section id="work"><div class="wrap"><h2>Featured</h2><div class="feat"><div><h3>{k["title"]}</h3><p>{E(k["summary"])}</p>{tags(k)}<a class="btn main" href="{k["slug"]}.html">Read the case study</a></div><img src="{k["cover"]}" alt="Kyomen cover image"></div></div></section>
<section><div class="wrap"><h2>Unity and gameplay</h2><div class="grid">{g("unity")}</div>
<p class="muted" style="margin-top:32px">Also: an AI Recap System that uses the Gemini API to turn in-game data into dynamic play-session recaps, built in Unity with structured JSON.</p></div></section>
<section><div class="wrap"><h2>C++ and OpenGL</h2><div class="grid">{g("gl")}</div></div></section>
<section id="contact"><div class="wrap about"><div><h2>Get in touch</h2><p>I'm looking for my first games industry role. Studios of any size welcome.</p></div>
<div><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><a href="{LI}">LinkedIn</a> / <a href="{GH}">GitHub</a> / <a href="{ITCH}">itch.io</a> / <a href="{CV}">CV (PDF)</a></p></div></div></section>'''
    return page(f"{NAME} | Gameplay Programmer","Gameplay programmer specialising in enemy AI and multi-phase boss systems in Unity/C#, with C++/OpenGL engine experience.",k["cover"],b)
def case(p):
    url,lab=p["label"].split("|")
    vid=f'<video controls muted loop playsinline src="{p["video"]}"></video>' if p["video"] else ""
    if p["yt"]: vid+=f'<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/{p["yt"]}" title="{E(p["title"])} gameplay video" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
    n=PROJECTS[(PROJECTS.index(p)+1)%len(PROJECTS)]
    b=f'''<div class="wrap"><div class="cs-head"><div><a href="index.html">&larr; All projects</a><h1>{E(p["title"])}</h1><p class="muted">{E(p["meta"])}</p><p>{E(p["summary"])}</p>{tags(p)}</div><img class="cover" src="{p["cover"]}" alt="{E(p["title"])} cover image"></div>
{vid}<div class="cs-body"><div><h2>My role</h2><p>{E(p["role"])}</p><h2 style="margin-top:32px">What I learned</h2><p>{E(p["learned"])}</p></div>
<div><h2>What I built</h2><ul>{"".join(f"<li>{E(x)}</li>" for x in p["bullets"])}</ul></div></div>
<section><h2>Play it</h2><iframe src="https://itch.io/embed/{p["itch"]}?dark=true" width="552" height="167" title="{E(p["title"])} on itch.io" loading="lazy"><a href="{url}">{E(lab)}</a></iframe></section>
<nav class="next" aria-label="Next project"><span class="muted">Next project</span><a href="{n["slug"]}.html">{E(n["title"])} &rarr;</a></nav></div>'''
    return page(f'{p["title"]} | {NAME}',p["summary"],p["cover"],b)
open("index.html","w",encoding="utf-8").write(index())
for p in PROJECTS: open(p["slug"]+".html","w",encoding="utf-8").write(case(p))

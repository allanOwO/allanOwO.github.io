"""Regenerates every page from the PROJECTS list. Edit the data, run: python build.py"""
import html,json,os,re
E=html.escape
BASE="https://allanowo.github.io/"
NAME="Allan Blyth"; EMAIL="allanjwb@gmail.com"; CV="Allan_Blyth_CV.pdf"
ITCH="https://allanowo.itch.io"; LI="https://www.linkedin.com/in/allan-blyth-32977b403/"; GH="https://github.com/allanOwO"
def P(slug,title,kind,meta,summary,cover,group,tags,role,bullets,learned,itch,label,video="",yt="",play=""):
    return dict(slug=slug,title=title,kind=kind,meta=meta,summary=summary,cover=cover,group=group,tags=tags,role=role,bullets=bullets,learned=learned,itch=itch,label=label,video=video,yt=yt,play=play)
PROJECTS=[
P("kyomen","Kyomen","Isometric action roguelike","Programmer, Marmot Studios | Global Game Jam 2026, now heading to Steam",
 "Don't let the weight of your past collapse the world. A fast-paced isometric arena combat game built around dynamic mask-based gameplay, started as a Global Game Jam 2026 entry and now in development by Marmot Studios for Steam.",
 "https://img.itch.zone/aW1nLzI1MzU2MTE1LnBuZw==/original/HTEPdh.png","feat",["Unity","C#","State machines","Boss AI"],
 "I work on the combat programming that drives the game's encounters: escalating pressure, how enemies approach the player, and a boss reactive enough that fights feel less predictable. Since the jam I've spent as much time on readability as on behaviour, making sure every boss attack is telegraphed clearly enough to feel fair. After the jam, the team of five formed Marmot Studios Ltd to take the game to release.",
 ["Designed and built a four-phase boss fight on state machines, with attack selection that filters by range and angle to the player and avoids repeating the last attack, and coroutine-based timing.","Built the attack telegraph system: fill indicators built as procedural meshes for each attack shape, with a wind-up on every boss attack so players can read what is coming.","Built the transitions between boss phases, including the explosive set piece that marks each escalation.","Designed and implemented the enemy wave system to control encounter pacing.","Built the first versions of the four enemy types during the jam (melee, ranged, explosive and charger), with separation steering and edge avoidance on a floor that rises and falls.","Implemented boss attack patterns and reactive decision-making that respond to the player's actions.","Iterated from jam prototype to a playable demo."],
 "Designing gameplay systems under a tight deadline, then hardening them for a real release. Balancing reusable enemy logic against the specific needs of a boss encounter, and learning that an attack is only as good as its telegraph.",
 "4250442","https://ath3rox.itch.io/kyomen|Kyomen by Ath3rox, qlxiy, Bishop, KyleMc04, Ryanmcg04, Allan"),
P("ballad-of-auld-dunrod","The Ballad of Auld Dunrod","Third-person stealth exploration","Programming Lead | Client project for a comic book publisher | Browser game",
 "A third-person stealth exploration game based on a Scottish folklore poem, in which the player helps Dunrod escape capture.",
 "https://img.itch.zone/aW1nLzIwNzE2NDY4LnBuZw==/original/e%2BdR4d.png","unity",["Unity","C#","WebGL","Stealth AI"],
 "I led the programming team and wrote around 70% of the game's code myself, including nearly all of the guard AI, the camera, the game manager and the touch joystick. I also coordinated the technical work, prioritised features, and made sure the game was stable and complete enough to deliver as a client project.",
 ["Built the guard AI: a patrol, investigate and chase state machine with view-cone detection and an alert meter.","Added rooftop lookouts that sweep an area and call nearby guards when they spot the player.","Built a top-down camera that follows the player along a looping dolly track, finding the closest point on the path and recovering cleanly when the player respawns.","Wrote the touch controls, including a virtual joystick, so the game plays on phones and school iPads.","Added a fairy guide that pathfinds to the next objective and leaves a particle trail, plus a map that tracks progress.","Optimised for mobile browsers by culling lights outside the camera's view."],
 "Owning most of a codebase while still leading a team: prioritising, keeping systems simple enough for others to build on, optimising for the browser, and delivering against a clear client-facing goal.",
 "3041421","https://gcugames.itch.io/ballad-of-auld-dunrod|Ballad of Auld Dunrod by Glasgow Caledonian University, Patricija Gudynaite, Blitz_Maxis, SkrubJG, Allan, Bishop",yt="uGwDVG2_ZKo",play="dunrod"),
P("tower-of-tales","Tower of Tales","Arena shooter","Gameplay Programmer | Team project",
 "A short arena shooter inspired by Arena of the Mad King, The Binding of Isaac and Realm of the Mad God. A cultist enters the arena to defeat the boss and bring back their family.",
 "https://img.itch.zone/aW1nLzI2OTAwMDEyLmpwZw==/original/omEVot.jpg","unity",["Unity","C#","Boss AI","Controller input"],
 "I worked on the player and boss gameplay loop, focusing on responsive movement and an encounter that reacts to the player's position and actions.",
 ["Created the boss's attack patterns, chosen by weighted scores that build up over time, with a second stage and a close-range attack that triggers when the player gets near.","Implemented player movement and tuned its feel for arena combat.","Added controller support for movement, dodging and the menus, so the game plays well across input devices."],
 "Encounter design, input abstraction, and how boss behaviour can communicate patterns while still demanding player adaptation.",
 "2672862","https://qlxiy.itch.io/tower-of-tales|Tower of Tales by qlxiy, Allan, PastorYoda216, Patricija Gudynaite, ashxy, beansTM",yt="i9INBV4BUcI",play="tower"),
P("bob-steve","Bob n' Steve","Cooperative action","Programmer | Team project",
 "Four soldiers, one string, a field that wants you dead. A cooperative action game with a shared string as its central teamwork mechanic.",
 "https://img.itch.zone/aW1nLzI5OTIwNDEzLnBuZw==/original/qetc6E.png","unity",["Unity","C#","Multiplayer","Voice chat"],
 "I focused on the systems that connect the players and make cooperation meaningful. The string needed gameplay logic that supported a group while staying readable and responsive in combat.",
 ["Designed and implemented the shared-string mechanic linking the soldiers.","Built the tin-can voice chat: private calls down the string to one teammate, sent as telephone-quality audio over Netcode.","Built the mortar strikes and landmines, plus the injury effects, ragdoll and dragging of downed teammates."],
 "Multiplayer-focused gameplay, explaining technical ideas within a team, and building mechanics that reinforce a game's core identity.",
 "4997416","https://ath3rox.itch.io/bob-steve|Bob n' Steve by Ath3rox, Bishop, KyleMc04, Charlie Turnbull - qlxiy, Allan"),
P("chill-fishing-game","Just a Chill Fishing Game","Relaxed fishing game","Gameplay Programmer | 48-hour jam | Global Game Jam 2025",
 "Explore the deepest depths, discover fish and make Marty proud in this relaxed fishing game.",
 "https://img.itch.zone/aW1nLzE5NTQ2NzQwLmpwZw==/original/ML78Ot.jpg","unity",["Unity","C#","Game jam"],
 "I helped take the game from concept to a complete playable release within 48 hours, focusing on fishing, discovering life underwater and making the environment feel active.",
 ["Built the hook and line: hook movement, the fishing line and catching fish, and shared the casting code with a teammate.","Implemented fish movement and the fish spawner, with rarity tiers from common to legendary.","Wrote the bubble spawner that adds movement and atmosphere underwater."],
 "Scoping features, iterating quickly, and delivering polished gameplay under a strict time limit.",
 "3271726","https://allanowo.itch.io/just-a-chill-fishing-game|Just a Chill Fishing Game by Allan, qlxiy, Ath3rox, Bishop, KyleMc04",play="fishing"),
P("ai-recap","AI Recap System","Research prototype","Solo programmer | Research prototype | Unity and Gemini API",
 "A Unity prototype that logs what the player does to the people in a small town, then turns that log into a written recap of the session, either with Google's Gemini API or from summaries I wrote by hand, so the two can be compared blind.",
 "","unity",["Unity","C#","Gemini API","JSON"],
 "I wrote all of the code: the characters you can talk to or kill, the event log, the Gemini integration and the hand-written alternative. The town and character art are free packs from the Unity Asset Store. The aim was a fair comparison, so the player cannot tell from how a recap appears which of the two wrote it.",
 ["Logged every conversation and kill as a structured event with who, what and when, and serialised the session to JSON.","Sent that JSON to the Gemini API from Unity with UnityWebRequest and a prompt that asks for a short second-person recap.","Wrote around 80 recaps by hand, one for each possible order of events, and looked the right one up from a key built out of the same event log.","Made both versions look identical to the player: the hand-written recap waits a second before appearing and both use the same typewriter reveal."],
 "Calling a web API from Unity, designing data so that code and a language model can both read it, and setting up a comparison so that the thing being tested is the only difference.",
 "",""),
P("voxel-world","Voxel World Prototype","OpenGL voxel engine","Solo programmer | C++ | OpenGL",
 "A voxel world built from the ground up to explore procedural generation, real-time lighting, world interaction and collision. My first OpenGL project. I've since gone back and optimised it, and it now runs a 1,000 chunk render distance at around 970 FPS.",
 "https://img.itch.zone/aW1nLzI1MDE3MTYxLnBuZw==/original/%2BL%2BNqm.png","gl",["C++","OpenGL","Procedural generation","Optimisation"],
 "A practical exploration of low-level rendering and engine development. Rather than relying on a pre-built world system, I implemented the core systems needed to create and interact with a large voxel environment. Later I went back to see how far I could push performance. I wrote a benchmark first so I could tell whether each change actually helped.",
 ["Built an infinite procedural world on a chunk-based system.","Implemented real-time directional sunlight with voxel-cast shadows.","Created interactive block modification so players can change the terrain.","Implemented AABB collision for reliable movement through voxel terrain.",
  "Added greedy meshing and per-vertex ambient occlusion.",
  "Merged the whole world into one big indirect draw instead of a draw per chunk.",
  "Split chunks into 16x16x16 pieces so whole regions can be culled at once.",
  "Added LODs so distant terrain is drawn at lower detail, which let me raise the render distance from 64 to 200 chunks, and later to 1,000 with a separate far-terrain pass.",
  "Moved world generation and meshing onto background threads.",
  "Added world saves, so the blocks you change stay changed.",
  "Wrote a benchmark that flies, spins and edits the world, then logs FPS, frame times and memory to a CSV.",
  "Same 64 chunk distance, before and after: loading went from 48 s to 1.5 s and average FPS from 108 to 836. At 1,000 chunks it averages around 970 FPS at 1080p on an RX 9060 XT."],
 "C++, OpenGL rendering, procedural systems, spatial organisation and lighting, and the challenges of building engine functionality from scratch. Going back to optimise it taught me to measure first and only keep the changes that make a real difference.",
 "4197600","https://allanowo.itch.io/voxel-world-prototype|Voxel World Prototype by Allan",video="clips/voxel-world.mp4"),
P("asteroids","Asteroids","Space shooter prototype","Solo programmer | C++ | OpenGL",
 "An arcade-inspired space shooter with procedural asteroid fields and a PS2-inspired low-poly look, built to develop my C++ and OpenGL experience.",
 "https://img.itch.zone/aW1nLzI5OTQ3MTI2LnBuZw==/original/jQ8lWB.png","gl",["C++","OpenGL","Low-poly"],
 "I built it to get more practical C++ and OpenGL experience while recreating the readable loop of a classic asteroid shooter, with a deliberately retro visual direction.",
 ["Developed the rendering and gameplay systems in OpenGL.","Implemented procedural asteroid generation for varied play spaces.","Created an explosion system with visual effects and responsive feedback.","Built a cohesive PS2-inspired low-poly style through rendering and presentation."],
 "Real-time rendering, procedural content, gameplay feedback, and how technical constraints can set a consistent visual identity.",
 "5002358","https://allanowo.itch.io/asteroids|Asteroids by Allan"),
]
# Images live in img/ as <slug>-cover.<ext> and <slug>-1.<ext>, <slug>-2.<ext>... The first screenshot is the page's main image.
IMGS=sorted(os.listdir("img"))
def shots(p): return sorted(("img/"+f for f in IMGS if re.fullmatch(re.escape(p["slug"])+r"-\d+\.\w+",f)),key=lambda f:int(re.search(r"-(\d+)\.",f).group(1)))
for p in PROJECTS: p["cover"]=next("img/"+f for f in IMGS if f.startswith(p["slug"]+"-cover."))
# Technical breakdowns. how: (heading, text). flow: steps of a diagram. pairs: (left, right) rows.
# bars: (title, [(label, number, extra note)], footnote). code: (title, file in code/, source file name, why it is written this way)
DEEP={
"kyomen":dict(
 how=[("Phase transitions as set pieces","Every time the boss crosses a health threshold it stops what it is doing, travels to the centre of the arena and runs one set-piece attack before the next phase begins. Which attack plays is decided by the phase being left, not by the threshold number. Each one is the outgoing phase's idea pushed further, so the pairing stays right even when the phase order is shuffled."),
  ("Invulnerable without feeling broken","The boss cannot be hurt during a transition. Instead of letting hits pass through it, the health bar goes grey and hits still land with all their usual feedback but read 0. The player can see their attacks are registering and simply doing nothing, rather than wondering if the game has bugged out."),
  ("Telegraphs that match the hit","Every ground telegraph is built from the same numbers the hit check uses, so the red area is exactly the area that hurts. Shapes are flat convex polygons (circle, cone, lane, trapezoid) drawn as a faint base, a fill that grows out from the attack's origin, and a border drawn inside the true edge so it never overstates the danger."),
  ("Patterns that are always escapable","The Bomber Barrage lobs explosive enemies onto a 5 by 5 tile grid using patterns a designer can author in the Inspector. Each pattern is checked before it is used: every targeted tile must have a safe tile directly beside it. A pattern that fails is skipped with a warning instead of producing an unfair hit.")],
 flowtitle="One phase transition",
 flow=["Health crosses a threshold","Shield up, health bar greys","Boss moves to arena centre","Wind-up pose","Set-piece attack","Recover","Next phase begins"],
 pairs=[("Leaving melee","Quadrant Strike: wedges of the floor light up and are struck, then the centre tiles drop"),("Leaving ranged","Rotating Lanes: radial lanes of shots that rotate after every pulse"),("Leaving explosive","Bomber Barrage: explosive enemies land on tiles, fizz and go off"),("Leaving charge","Lane Charges: staggered charges down lanes near the player")],
 code_stashed=[("Running a phase transition","kyomen-phase-transition.cs","BossPhaseTransitions.cs","One coroutine owns the whole sequence, so the order of events reads top to bottom and there is a single place to abort it if the boss is reset or killed mid-transition."),
  ("Rejecting unfair bomb patterns","kyomen-escapable.cs","BossPhaseTransitions.cs","Designers can add patterns freely because the code refuses any that would trap the player. Fairness is enforced by a rule, not by remembering to playtest every pattern."),
  ("Growing the telegraph fill","kyomen-telegraph.cs","FillIndicator.cs","Most shapes fill by scaling a mesh. A trapezoid cannot, because scaling would push the fill outside its slanted sides, so its far corners are walked along the edges instead.")]),
"ballad-of-auld-dunrod":dict(
 how=[("Cheap checks first","The game had to run in a mobile browser on school iPads, so guard vision does its cheapest tests first. It compares squared distances to skip the square root, then tests the view cone with a single dot product against a cosine worked out once at start-up. Only a target that passes both pays for a physics raycast to confirm line of sight. A small near circle means the player cannot stand right behind a guard unnoticed."),
  ("An alert meter, not an instant fail","Being seen does not start a chase straight away. An alert meter fills while the player is in view and drains when they break line of sight, and the chase begins only once it is full. That gives the player a moment to react and makes close calls feel fair. Thrown cheese takes priority over the player, so it works as a reliable distraction."),
  ("A camera on a looping track","The top-down camera rides a dolly track that loops around the level. The track is sampled once at start-up, and each update only considers the samples within a few metres of the camera's last position, 20 times a second instead of every frame. Because the track loops, the cart always travels the short way round, and when the player respawns somewhere else the camera does one full search to snap to the right place.")],
 flowtitle="Guard behaviour",
 flow=["Walk the patrol route","Turn and inspect at waypoints","Player seen: alert meter fills","Chase","Lose the player: reset","Walk back to the route"],
 code=[("Can this guard see the target?","dunrod-vision.cs","GuardVision.cs","Ordered from cheapest test to most expensive, so most guards on most frames never reach the raycast."),
  ("Following the player around a looping track","dunrod-dolly.cs","DollyFollowPlayer.cs","Without the wrap check, crossing the start of the loop would send the camera the long way round the whole level.")]),
"tower-of-tales":dict(
 how=[("Scores instead of a dice roll","Each of the boss's seven attacks has a score that climbs every frame at its own rate, with some randomness in how fast. When the boss is ready to attack it uses whichever score is highest, then resets that score to zero. An attack that has just been used has to climb all the way back up, so the boss rarely repeats itself, and an attack with a higher weight comes round more often without ever becoming predictable."),
  ("A second stage that changes the odds","When the boss drops to its second stage, everything on screen is cleared and the eye attack's score is set far above the rest so it always opens the stage. Its weight is then raised so it stays common for the rest of the fight. The second stage also adds a tentacle that strikes at the player's position whenever they stand too close, so hugging the boss stops being safe."),
  ("Patterns built from one Shoot function","The spiral, spurt and wave patterns all go through the same Shoot call, which takes the bullet force, the delay between shots, the angle and whether to fire in two directions at once. A new pattern is mostly a new loop over angles and timings.")],
 flowtitle="Choosing the next attack",
 flow=["Every score climbs each frame","Boss finishes an attack","Short random pause","Highest score attacks","That score resets to zero"],
 code=[("Weighted attack selection","tower-scores.cs","BossAttack.cs, four short excerpts","Resetting only the winner's score gives a cooldown for free. No attack needs its own timer, and tuning the fight is a matter of changing two numbers per attack.")]),
"bob-steve":dict(
 how=[("A rope that is simulated, not worked out","The string between players is simulated as an actual rope. It pays off a spool as you walk, falls under its own weight, catches on what it touches and stays where it lands. My first version stored the shortest path from the anchor to the player and recalculated it every frame. That was right about where a tight rope goes, but a shortest path has no slack, so it could never sag between two crates or lie in a loop behind you."),
  ("Two numbers to tune it","Tautness is how hard the rope pulls itself straight, from dead weight hanging in a deep curve to pulled tight against every corner. Elasticity is how quickly the spool takes slack back in when you walk back along the rope. Keeping them separate means the look of the rope and how forgiving it is to play with can be tuned independently. An optional tension mode makes the spool finite, so the last stretch drags and the end of it stops you."),
  ("Voice that travels down the string","Each player wears a colour, and the tin can dials one teammate's colour to talk to them. Audio is sent in 40 ms packets at telephone quality to the host, which forwards it only to the player being called, so a call is private rather than muted for everyone else. Both ends have to be tied on to an anchor first, which is what makes losing your line cost you something."),
  ("Mortars that ask a question","A mortar round is a whistle and a mark on the ground, a fuse long enough to react to, and then the burst. The server owns the timing and the damage. Every client is told once, up front, and plays the whistle and flash off its own clock, so a strike costs one network message instead of a stream of them.")],
 flowtitle="One mortar round",
 flow=["Server picks a target","One message to every client","Whistle and ground mark","Fuse: time to move","Burst, damage on the server"]),
"ai-recap":dict(
 how=[("An event log both sides can read","Every character has a name and a role. Talking to one or killing one adds an event with the name, role, action, line of dialogue and timestamp. The same list feeds both versions: it is serialised to JSON for Gemini, and reduced to a key such as Guard_Talk-Merchant_Kill to look up the hand-written recap."),
  ("Keeping the comparison fair","Gemini takes a moment to answer and a lookup is instant, which would give the game away. The hand-written recap therefore waits a second before it appears, and both are revealed one character at a time by the same routine. A single toggle switches between the two, so the builds given to testers are otherwise identical."),
  ("Limiting the possibilities","A character you have spoken to can no longer be killed, and a dead one cannot speak. That keeps the number of possible sessions small enough to write a recap for every one of them by hand, which is what makes a like-for-like comparison possible at all.")],
 flowtitle="From play to recap",
 flow=["Talk to or kill a character","Event added to the log","Recap requested","Gemini writes it, or the key finds a hand-written one","Same typewriter reveal"],
 code=[("The hand-written path, made to look the same","recap-blind.cs","NpcSessionLogger.cs","The one-second wait exists only so testers cannot tell the two versions apart by speed.")]),
"voxel-world":dict(
 how=[("Measure first","Before optimising anything I wrote a benchmark that loads the world, flies a fixed route, spins on the spot and edits blocks, then appends load time, average FPS, 1% lows, draw calls and memory to a CSV. Every change below was kept or thrown away based on that log, which now holds 74 runs."),
  ("One draw instead of thousands","The first benchmark showed 5,839 draw calls a frame at a 64 chunk distance. Chunk meshes now live in a shared pool and the whole world is submitted as a list of indirect draw commands, so the GPU walks the list instead of the CPU issuing a draw per chunk. That one change took the benchmark from 108 to 988 FPS."),
  ("Greedy meshing and 16-byte vertices","Neighbouring faces with the same texture and lighting are merged into the largest rectangle possible. Each vertex is packed into 16 bytes, and because a merged quad can be several blocks wide, texture coordinates are stored in blocks and the shader repeats the atlas tile with fract()."),
  ("Sections and culling","Chunks are split into 16x16x16 sections, which cut block memory in the benchmark from 1,056 MB to 81 MB and lets whole regions be culled at once. Faces are also grouped by the direction they point, so groups facing away from the camera are never sent to the GPU."),
  ("LODs and far terrain","Level-of-detail meshes took the 200 chunk benchmark from 129 to 1,353 FPS. A separate far-terrain pass has since pushed the render distance to 1,000 chunks at roughly 970 FPS, with the world loading in about 7 seconds.")],
 bars=("Benchmark results, step by step",[("64 chunks: baseline",108,"5,839 draw calls, 48 s load"),("64 chunks: one merged indirect draw",988,"1 draw call"),("64 chunks: 16x16x16 sections and region culling",848,"block memory 1,056 MB to 81 MB, 3 s load"),("200 chunks: first run",129,"146 s load"),("200 chunks: LODs",1353,"17 s load"),("200 chunks: face-direction culling",1540,"3.5 s load"),("1,000 chunks: far terrain",970,"7 s load")],
  "Average FPS in the benchmark's spin test at 1080p on an RX 9060 XT, taken from the project's benchmark log."),
 code=[("Greedy meshing: merging faces into rectangles","voxel-greedy.cpp","Chunk.cpp","Each cell of the mask encodes texture and ambient occlusion in one integer, so 'can these faces merge?' is a single comparison."),
  ("Skipping faces that point away from the camera","voxel-drawlist.cpp","Renderer.cpp","A small hidden group between two visible ones is drawn anyway. A draw call costs about as much as 400 triangles, so splitting around fewer than that would make things slower.")]),
}
def deep(p):
    d=DEEP.get(p["slug"])
    if not d: return ""
    h='<section class="tight" id="how"><h2>How it works</h2><div class="how">'+"".join(f"<div><h3>{E(a)}</h3><p>{E(b)}</p></div>" for a,b in d["how"])+"</div>"
    if d.get("flow"): h+=f'<figure class="flow"><figcaption>{E(d["flowtitle"])}</figcaption><ol>'+"".join(f"<li>{E(x)}</li>" for x in d["flow"])+"</ol></figure>"
    if d.get("pairs"): h+='<dl class="pairs">'+"".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a,b in d["pairs"])+"</dl>"
    if d.get("bars"):
        t,rows,note=d["bars"]; top=max(r[1] for r in rows)
        h+=f'<figure class="bars"><figcaption>{E(t)}</figcaption>'+"".join(f'<div class="bar"><span>{E(l)}</span><div><i style="width:{v/top*100:.1f}%"></i><b>{v:,} FPS</b></div><small>{E(x)}</small></div>' for l,v,x in rows)+f'<p class="muted">{E(note)}</p></figure>'
    h+="</section>"
    if d.get("code"):
        h+='<section class="tight" id="code"><h2>Code</h2><p class="muted">Short excerpts from the project. Every line shown is mine.</p>'+"".join(f'<figure class="code"><figcaption><b>{E(t)}</b><span>{E(src)}</span></figcaption><pre tabindex="0"><code>{E(open("code/"+f,encoding="utf-8").read().rstrip())}</code></pre><p>{E(why)}</p></figure>' for t,f,src,why in d["code"])+"</section>"
    return h
# Headline numbers shown as a strip at the top of a project page: (number, label)
STATS={
"kyomen":[("4","boss phases"),("4","enemy types"),("5","person team"),("Steam","release in progress")],
"ballad-of-auld-dunrod":[("~70%","of the code written by me"),("Lead","of the programming team"),("WebGL","runs on phones and iPads"),("Client","project, delivered")],
"voxel-world":[("108 &rarr; 836","average FPS, same 64 chunk distance"),("48 s &rarr; 1.5 s","world load time"),("1,000","chunk render distance, up from 64"),("~970","FPS at 1,000 chunks, 1080p")],
"chill-fishing-game":[("48","hours, concept to release"),("5","person team"),("GGJ","Global Game Jam 2025")],
}
TEAM={"kyomen":"5 people","ballad-of-auld-dunrod":"8 people","tower-of-tales":"6 people","bob-steve":"5 people","chill-fishing-game":"5 people","voxel-world":"Solo","asteroids":"Solo","ai-recap":"Solo"}
SKILLS=[("Languages","C#, C++"),("Engines and graphics","Unity, OpenGL, WebGL builds"),("Gameplay and AI","State machines, boss and enemy behaviour, attack systems, weighted randomness, coroutine-based timing"),("Also","Git, controller input, JSON, Gemini API integration")]
PLAYNOTE={"dunrod":"Built for touch screens: drag the on-screen joystick with your finger or mouse."}
ICON="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23ff4d5e'/%3E%3Cpath d='M8 24 16 8l8 16' fill='none' stroke='%2315111f' stroke-width='4'/%3E%3C/svg%3E"
def role(p): return p["meta"].split(" | ")[0]
def context(p): return "Personal project" if p["group"]=="gl" else ", ".join(p["meta"].split(" | ")[1:])
def page(title,desc,img,body,path="",ld=""):
    url=BASE+path
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{BASE}{E(img)}">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#15111f">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;600;700&display=swap">
<link rel="stylesheet" href="style.css">{ld}</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="top-in"><a class="brand" href="index.html">{NAME}<span>Gameplay programmer</span></a>
<nav aria-label="Main"><a href="index.html#work">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact</a><a class="cv" href="{CV}">CV</a></nav></div>
<div class="hp-bar" aria-hidden="true"><i class="hp-lag"></i><i class="hp-fill"></i></div></header>
<main id="main">{body}</main>
<footer><div class="wrap foot"><span>&copy; 2026 {NAME}. Gameplay programmer, Scotland.</span><span><a href="mailto:{EMAIL}">Email</a><a href="{LI}">LinkedIn</a><a href="{GH}">GitHub</a><a href="{ITCH}">itch.io</a><a href="{CV}">CV</a></span></div></footer>
<dialog class="lightbox" aria-label="Screenshot"><img alt=""><button type="button" aria-label="Close">&times;</button></dialog>
<script src="script.js"></script></body></html>'''
def tags(p): return '<ul class="tags">'+"".join(f"<li>{E(t)}</li>" for t in p["tags"])+"</ul>"
def badges(p):
    b=('<li class="b-play">Play in browser</li>' if p["play"] else "")+('<li>Trailer</li>' if p["yt"] else '<li>Video</li>' if p["video"] else "")
    return f'<ul class="badges">{b}</ul>' if b else ""
def card(p):
    return f'''<a class="card" href="{p["slug"]}.html"><div class="thumb"><img src="{p["cover"]}" alt="" loading="lazy">{badges(p)}</div>
<p class="kicker">{E(p["kind"])}</p><h3>{E(p["title"])}</h3><p class="card-role">{E(role(p))} &middot; {E(TEAM[p["slug"]])}</p><p>{E(p["bullets"][0])}</p>{tags(p)}</a>'''
def stats(p):
    s=STATS.get(p["slug"])
    return '<dl class="stats">'+"".join(f"<div><dt>{n}</dt><dd>{E(l)}</dd></div>" for n,l in s)+"</dl>" if s else ""
def feat(p,img,flip=False,loop=""):
    media=f'<video autoplay muted loop playsinline preload="metadata" poster="{img}" src="{loop}" aria-label="{E(p["title"])} fly-through"></video>' if loop else f'<img src="{img}" alt="{E(p["title"])} screenshot" loading="lazy">'
    pts=[f"{n} {l}" for n,l in STATS[p["slug"]][:3]] if flip else [E(x) for x in p["bullets"][:3]]
    return f'''<div class="feat{" flip" if flip else ""}"><a class="feat-img" href="{p["slug"]}.html">{media}</a><div><p class="card-role">{E(role(p))} &middot; {E(context(p))}</p><p>{E(p["summary"])}</p>
<ul class="ticks">{"".join(f"<li>{x}</li>" for x in pts)}</ul>{tags(p)}<a class="btn main" href="{p["slug"]}.html">Read the case study</a></div></div>'''
def index():
    k=PROJECTS[0]; ks=shots(k); v=next(p for p in PROJECTS if p["slug"]=="voxel-world")
    nplay=sum(1 for p in PROJECTS if p["play"])
    b=f'''<div class="wrap hero"><div><p class="eyebrow"><i></i>Open to work &middot; Scotland / remote</p><h1>Bosses that fight back.</h1>
<p class="lede">I'm Allan, a gameplay programmer specialising in enemy AI and multi-phase boss systems in Unity and C#. I also build engine tech in C++ and OpenGL.</p>
<div class="btns"><a class="btn main" href="#work">See my work</a><a class="btn" href="{CV}">Download CV</a><a class="btn" href="mailto:{EMAIL}">Email me</a></div></div>
<a class="hero-shot" href="{k["slug"]}.html"><img src="{ks[0]}" alt="Kyomen gameplay screenshot" fetchpriority="high"><span><b>Kyomen</b> Four-phase boss fight, heading to Steam &rarr;</span></a></div>
<div class="wrap"><ul class="facts"><li><b>BSc (Hons) 2:1</b>Games Development, Glasgow Caledonian University, 2026</li><li><b>Co-founder</b>Marmot Studios Ltd, taking Kyomen to Steam</li><li><b>{sum(1 for p in PROJECTS if p["itch"])} shipped projects</b>{nplay} playable right here in your browser</li><li><b>C# and C++</b>Unity gameplay and OpenGL engine work</li></ul></div>
<section id="work"><div class="wrap"><p class="kicker">Selected work</p><h2>Featured: {k["title"]}</h2>{feat(k,ks[1])}</div></section>
<section class="tight"><div class="wrap"><h2>Engine work: {v["title"]}</h2>{feat(v,"clips/voxel-world.jpg",True,"clips/voxel-world-loop.mp4")}</div></section>
<section><div class="wrap"><h2>More projects</h2><div class="grid">{"".join(card(p) for p in PROJECTS if p not in (k,v))}</div></div></section>
<section id="about"><div class="wrap about"><div><p class="kicker">About</p><h2>I make enemies worth fighting.</h2>
<p>I graduated in 2026 with a 2:1 in Games Development from Glasgow Caledonian University. Most of my work is combat: enemy behaviour, encounter pacing, and boss fights that react to the player while staying readable enough to feel fair.</p>
<p>After Global Game Jam 2026, the five of us who made Kyomen formed Marmot Studios Ltd to take it to Steam. I work on the gameplay and boss programming, and handled the early company and Steamworks setup.</p>
<p>Outside Unity I write C++ and OpenGL, including a voxel engine I profiled and optimised from 108 to 836 FPS. I've also built an AI Recap System that uses the Gemini API to turn in-game data into play-session recaps, driven by structured JSON from Unity.</p>
<div class="btns"><a class="btn main" href="{CV}">Download CV</a><a class="btn" href="{LI}">LinkedIn</a></div></div>
<dl class="skills">{"".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a,b in SKILLS)}<div><dt>Experience</dt><dd>Co-founder and Programmer, Marmot Studios Ltd, 2026 to present</dd></div><div><dt>Education</dt><dd>BSc (Hons) Games Development, 2:1, Glasgow Caledonian University, 2022 to 2026</dd></div></dl></div></section>
{contact("Get in touch")}'''
    ld='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"Person","name":NAME,"jobTitle":"Gameplay Programmer","url":BASE,"email":"mailto:"+EMAIL,"sameAs":[LI,GH,ITCH],"alumniOf":"Glasgow Caledonian University"})+"</script>"
    return page(f"{NAME} | Gameplay Programmer","Gameplay programmer specialising in enemy AI and multi-phase boss systems in Unity/C#, with C++/OpenGL engine experience. Open to work.","img/social-card.jpg",b,"",ld)
def contact(h):
    return f'''<section id="contact"><div class="wrap"><div class="cta"><div><h2>{h}</h2><p>I'm looking for my first games industry role as a gameplay or AI programmer. Studios of any size welcome.</p></div>
<div><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a><p class="links"><a href="{CV}">CV (PDF)</a><a href="{LI}">LinkedIn</a><a href="{GH}">GitHub</a><a href="{ITCH}">itch.io</a></p></div></div></div></section>'''
def case(p):
    url,lab=p["label"].split("|") if p["label"] else ("",""); ss=shots(p)
    poster=p["video"][:-4]+".jpg"
    vid=f'<video controls muted loop playsinline preload="none" src="{p["video"]}"{f' poster="{poster}"' if os.path.exists(poster) else ""}></video>' if p["video"] else ""
    if p["yt"]: vid+=f'<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/{p["yt"]}" title="{E(p["title"])} gameplay video" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
    if vid: vid=f'<section class="tight"><h2>{"Trailer" if p["yt"] else "In motion"}</h2>{vid}</section>'
    n=PROJECTS[(PROJECTS.index(p)+1)%len(PROJECTS)]
    web=f'''<div class="play" data-game="{p["play"]}" data-title="{E(p["title"])}"><img src="{ss[0] if ss else p["cover"]}" alt="" loading="lazy"><button class="btn main" type="button">&#9654; Play in browser</button></div>
<p class="muted play-note">Runs in your browser, no download. {PLAYNOTE.get(p["play"],"Best on desktop with a keyboard and mouse.")} <button class="link" type="button" data-fs hidden>Fullscreen</button></p>''' if p["play"] else ""
    gal=f'<section class="tight"><h2>Screenshots</h2><div class="gallery">{"".join(f"""<a href="{s}"><img src="{s}" alt="{E(p["title"])} screenshot {i+1}" loading="lazy"></a>""" for i,s in enumerate(ss))}</div></section>' if len(ss)>1 else ""
    jump='<a class="btn main" href="#play">&#9654; Play in browser</a>' if p["play"] else f'<a class="btn main" href="{url}">View on itch.io</a>' if url else '<a class="btn main" href="#how">How it works</a>'
    itch=f'''<section class="tight" id="play"><h2>Play it</h2>{web}<iframe src="https://itch.io/embed/{p["itch"]}?dark=true" width="552" height="167" title="{E(p["title"])} on itch.io" loading="lazy"><a href="{url}">{E(lab)}</a></iframe></section>''' if p["itch"] else ""
    b=f'''<div class="wrap"><div class="cs-head"><div><a class="back" href="index.html#work">&larr; All projects</a><p class="kicker">{E(p["kind"])}</p><h1>{E(p["title"])}</h1><p class="lede">{E(p["summary"])}</p>
<div class="btns">{jump}<a class="btn" href="#built">What I built</a>{"<a class=btn href=#code>See the code</a>" if DEEP.get(p["slug"],{}).get("code") else ""}</div></div><img class="cover" src="{ss[0] if ss else p["cover"]}" alt="{E(p["title"])} screenshot" fetchpriority="high"></div>
<dl class="meta"><div><dt>Role</dt><dd>{E(role(p))}</dd></div><div><dt>Team</dt><dd>{E(TEAM[p["slug"]])}</dd></div><div><dt>Context</dt><dd>{E(context(p))}</dd></div><div><dt>Tech</dt><dd>{E(", ".join(p["tags"]))}</dd></div></dl>
{stats(p)}
<div class="cs-body" id="built"><div><h2>What I built</h2><ul class="ticks">{"".join(f"<li>{E(x)}</li>" for x in p["bullets"])}</ul></div>
<div><h2>My role</h2><p>{E(p["role"])}</p><h2 class="gap">What I learned</h2><p>{E(p["learned"])}</p></div></div>
{deep(p)}{vid}{gal}
{itch}
<nav class="next" aria-label="Next project"><span class="muted">Next project</span><a href="{n["slug"]}.html">{E(n["title"])} &rarr;</a></nav></div>
{contact("Like what you see?")}'''
    return page(f'{p["title"]} | {NAME}',p["summary"],ss[0] if ss else p["cover"],b,p["slug"]+".html")
open("index.html","w",encoding="utf-8").write(index())
for p in PROJECTS: open(p["slug"]+".html","w",encoding="utf-8").write(case(p))
def lost():
    b=f'<div class="wrap lost"><p class="kicker">404</p><h1>You died.</h1><p class="lede">That page does not exist, or it moved when I rebuilt the site.</p><div class="btns"><a class="btn main" href="{BASE}">Respawn at the home page</a><a class="btn" href="{BASE}#work">See my work</a></div></div>'
    h=page(f"Page not found | {NAME}","That page does not exist.","img/social-card.jpg",b,"404.html")
    for a in ('href="style.css"','src="script.js"','href="index.html',f'href="{CV}"'): h=h.replace(a,a.replace('="','="'+BASE,1))
    return h.replace("<title>",'<meta name="robots" content="noindex"><title>')
open("404.html","w",encoding="utf-8").write(lost())
open("sitemap.xml","w",encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}{u}</loc></url>\n" for u in [""]+[p["slug"]+".html" for p in PROJECTS])+"</urlset>\n")

// Boss health bar in the header drains as the page scrolls
(function(){var f=document.querySelector(".hp-fill"),l=document.querySelector(".hp-lag");if(!f)return;
function u(){var m=document.documentElement.scrollHeight-innerHeight,p=m>0?Math.min(1,scrollY/m):0;
f.style.width=l.style.width=Math.round((1-p)*100)+"%"}
addEventListener("scroll",u,{passive:true});addEventListener("resize",u);u()})();

// "Play in browser" swaps the poster for the Unity WebGL player
(function(){var b=document.querySelector(".play");if(!b)return;var fs=document.querySelector("[data-fs]");
b.querySelector("button").addEventListener("click",function(){var f=document.createElement("iframe");
f.src="play/player.html?g="+encodeURIComponent(b.dataset.game);f.title=b.dataset.title+", playable in the browser";
f.allow="fullscreen; gamepad; autoplay";f.allowFullscreen=true;b.textContent="";b.appendChild(f);f.focus();
if(fs&&b.requestFullscreen){fs.hidden=false;fs.addEventListener("click",function(){b.requestFullscreen();f.focus()})}})})();

// Screenshot gallery opens images in a lightbox instead of leaving the page
(function(){var d=document.querySelector(".lightbox");if(!d||!d.showModal)return;var img=d.querySelector("img");
document.querySelectorAll(".gallery a").forEach(function(a){a.addEventListener("click",function(e){
e.preventDefault();img.src=a.href;img.alt=a.querySelector("img").alt;d.showModal()})});
d.addEventListener("click",function(e){if(e.target!==img)d.close()})})();

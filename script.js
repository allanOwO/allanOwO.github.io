(function(){var f=document.querySelector(".hp-fill"),l=document.querySelector(".hp-lag"),t=document.querySelector(".hp-label");
function u(){var m=document.documentElement.scrollHeight-innerHeight,p=m>0?Math.min(1,scrollY/m):0,r=Math.round((1-p)*100);
f.style.width=l.style.width=r+"%";t.textContent="Phase "+Math.min(4,Math.floor(p*4)+1)+" of 4"}
addEventListener("scroll",u,{passive:true});addEventListener("resize",u);u()})();

(function(){var b=document.querySelector(".play");if(!b)return;var fs=document.querySelector("[data-fs]");
b.querySelector("button").addEventListener("click",function(){var f=document.createElement("iframe");
f.src="play/player.html?g="+encodeURIComponent(b.dataset.game);f.title=b.dataset.title+", playable in the browser";
f.allow="fullscreen; gamepad; autoplay";f.allowFullscreen=true;b.textContent="";b.appendChild(f);f.focus();
if(fs&&b.requestFullscreen){fs.hidden=false;fs.addEventListener("click",function(){b.requestFullscreen();f.focus()})}})})();

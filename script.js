(function(){var f=document.querySelector(".hp-fill"),l=document.querySelector(".hp-lag"),t=document.querySelector(".hp-label");
function u(){var m=document.documentElement.scrollHeight-innerHeight,p=m>0?Math.min(1,scrollY/m):0,r=Math.round((1-p)*100);
f.style.width=l.style.width=r+"%";t.textContent="Phase "+Math.min(4,Math.floor(p*4)+1)+" of 4"}
addEventListener("scroll",u,{passive:true});addEventListener("resize",u);u()})();

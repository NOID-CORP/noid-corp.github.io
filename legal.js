// Comportamiento compartido por las páginas legales
// Títulos de rescate (mismo algoritmo que la portada)
(function(){
  var F=[['"Gloock",Georgia,serif','italic','400'],['"Archivo Black",Impact,sans-serif','normal','400'],['"Courier Prime",Courier,monospace','normal','700'],['"IM Fell English",Georgia,serif','italic','400']];
  var P=[['#C7D8EE','#362011'],['#4D0C10','#C7D8EE'],['#55372a','#C7D8EE'],['#C7D8EE','#4D0C10'],['#362011','#C7D8EE'],['#FAECB2','#4D0C10']];
  var s=11;function r(){s=(s*9301+49297)%233280;return s/233280}
  document.querySelectorAll('.rescate').forEach(function(el){
    var t=el.getAttribute('data-t');el.textContent='';el.setAttribute('aria-label',t);
    var mant=0;
    t.split(' ').forEach(function(w,wi){
      if(wi){var e=document.createElement('span');e.className='esp';el.appendChild(e)}
      var pal=document.createElement('span');pal.className='pal';pal.setAttribute('aria-hidden','true');
      w.split('').forEach(function(c){
        var l=document.createElement('span');l.className='l';l.textContent=c;
        var f=F[Math.floor(r()*4)],p=Math.floor(r()*P.length);
        if(p===5&&mant++)p=0;
        l.style.fontFamily=f[0];l.style.fontStyle=f[1];l.style.fontWeight=f[2];
        l.style.background=P[p][0];l.style.color=P[p][1];
        l.style.transform='rotate('+((r()-.5)*9).toFixed(1)+'deg) translateY('+((r()-.5)*6).toFixed(1)+'px)';
        pal.appendChild(l);
      });
      el.appendChild(pal);
    });
  });
})();

// Índice: cerrado en celular y marca la sección visible
(function(){
  var d=document.querySelector('.indice details'),mq=matchMedia('(max-width:900px)');
  function ajusta(){if(d)d.open=!mq.matches}
  ajusta();
  if(mq.addEventListener)mq.addEventListener('change',ajusta);
  var enlaces={};
  document.querySelectorAll('.indice a').forEach(function(a){
    enlaces[a.getAttribute('href').slice(1)]=a;
    a.addEventListener('click',function(){if(d&&mq.matches)d.open=false});
  });
  if(!('IntersectionObserver' in window))return;
  var obs=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting)return;
      Object.keys(enlaces).forEach(function(k){enlaces[k].removeAttribute('aria-current')});
      var a=enlaces[e.target.id];if(a)a.setAttribute('aria-current','true');
    });
  },{rootMargin:'-20% 0px -70% 0px'});
  document.querySelectorAll('.articulo section[id]').forEach(function(s){obs.observe(s)});
})();

// Imprimir o guardar en PDF
(function(){
  var b=document.getElementById('imprimir');if(!b||!window.print)return;
  b.hidden=false;b.addEventListener('click',function(){window.print()});
})();

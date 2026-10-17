class Component extends DCLogic {
  renderVals() {
    return {};
  }
  componentDidMount() {
(function(){
'use strict';
/* ---------- data (million toman) ---------- */
// k,name,unit,fixed,rev,margin,wc,dep,months,desc,est,scores[payback,margin,water,bio,import,future]
var BASE=[
 ['broiler','مرغ گوشتی','قطعه ظرفیت',1.575,2.37,0.10,0.26,0.06,8,'حدود ۵٫۵ دوره در سال، ۲٫۷ کیلو وزن زنده و ۶٪ تلفات؛ قیمت مرغ زنده حدود ۱۷۰ هزار تومان.',1,[5,3,6,3,2,4]],
 ['layer','مرغ تخمگذار','قطعه',1.95,4.54,0.11,0.60,0.06,14,'۳۲۰ تخم در سال (حدود ۱۹٫۵ کیلو) با قیمت درب مرغداری حدود ۲۲۰ هزار تومان، به‌اضافهٔ فروش مرغ حذفی.',1,[6,4,6,3,3,5]],
 ['turkey','بوقلمون گوشتی','قطعه ظرفیت',1.6875,5.30,0.12,0.90,0.06,9,'حدود ۲٫۵ دوره در سال و ۲۳ کیلو وزن زنده برای هر جایگاه، با قیمت حدود ۲۳۰ هزار تومان.',1,[7,5,6,4,3,5]],
 ['quail','بلدرچین','قطعه ظرفیت',0.43125,0.27,0.18,0.10,0.07,4,'حدود شش دوره در سال با فروش هر قطعه حدود ۴۵ هزار تومان.',1,[4,4,7,5,4,4]],
 ['bee','زنبور عسل','کلنی',22.5,21,0.40,0.13,0.12,4,'حدود ۱۲ کیلو عسل برای هر کلنی با قیمت عمدهٔ ۱٫۵ میلیون تومان، به‌اضافهٔ موم، گرده و فروش بستهٔ زنبور.',1,[9,8,8,4,9,7]],
 ['dairy','گاو شیری','راس',635,605,0.18,0.24,0.07,15,'میانگین گله حدود ۲۵ کیلو شیر در روز (۹ تن در سال) با قیمت مصوب ۶۰٬۵۰۰ تومان، به‌اضافهٔ فروش گوساله و دام حذفی.',0,[4,4,2,5,3,6]],
 ['calf','پرواربندی گوساله اصیل','راس ظرفیت',125.375,607,0.08,2.50,0.05,7,'حدود ۱٫۷ دوره در سال و فروش دام حدود ۵۵۰ کیلویی؛ بخش بزرگ سرمایه در گردش، خرید خود گوساله است.',1,[5,3,2,6,3,3]],
 ['lamb','پرواربندی بره','راس ظرفیت',26.25,127,0.10,1.30,0.05,4,'سه دوره در سال، فروش بره حدود ۵۰ کیلویی با قیمت زنده حدود ۸۵۰ هزار تومان.',1,[8,5,3,6,4,4]],
 ['sheep','گوسفند و بز داشتی','راس',75,43,0.25,0.13,0.05,8,'حدود ۱٫۲ بره در سال برای هر میش، به‌اضافهٔ شیر و پشم.',1,[4,5,3,7,6,3]],
 ['sheephp','گوسفند و بز پرتولید','راس',156.75,85,0.28,0.10,0.05,9,'حدود ۲٫۲ بره در سال به لطف دوقلوزایی؛ دام مولد اصلاح‌شده گران‌تر است.',1,[5,6,3,7,5,7]],
 ['trout','ماهی سردآبی (قزل‌آلا)','تن ظرفیت',1012.5,330,0.25,0.13,0.06,10,'هر تن ظرفیت سالانه با قیمت درب مزرعه حدود ۳۳۰ هزار تومان در کیلو.',1,[2,4,3,5,5,6]],
 ['warm','ماهی گرمابی','تن ظرفیت',675,200,0.25,0.10,0.06,12,'یک دورهٔ پرورش در سال با قیمت حدود ۲۰۰ هزار تومان در کیلو.',1,[2,3,4,6,6,4]],
 ['tilapia','تیلاپیا','تن ظرفیت',1075,250,0.25,0.10,0.07,10,'سیستم مداربسته با قیمت حدود ۲۵۰ هزار تومان در کیلو.',1,[2,3,8,7,5,7]],
 ['cage','ماهی در قفس','تن ظرفیت',2255,550,0.30,0.09,0.10,14,'قفس دریایی با قیمت حدود ۵۵۰ هزار تومان در کیلو؛ استهلاک تجهیزات دریایی بالاست.',1,[2,5,8,5,4,8]],
 ['shrimp','میگو پرورشی','هکتار',3168,2400,0.30,0.32,0.06,10,'حدود ۴ تن در هکتار با قیمت صادراتی درب مزرعه حدود ۶۰۰ هزار تومان.',1,[6,8,6,3,5,7]],
 ['sturgeon','ماهیان خاویاری (فاز پایدار)','تن ظرفیت',1842.5,2500,0.45,0.30,0.06,90,'گوشت به‌اضافهٔ حدود ۲۵ کیلو خاویار برای هر تن ظرفیت؛ درآمد خاویار از سال هفتم یا هشتم شروع می‌شود.',1,[2,10,5,6,6,8]],
 ['soil','گلخانهٔ خاکی','متر مربع',7.425,1.26,0.35,0.05,0.06,6,'حدود ۲۸ کیلو در متر مربع با قیمت درب گلخانه حدود ۴۵ هزار تومان.',1,[2,4,5,6,6,4]],
 ['hydro','گلخانهٔ هیدروپونیک','متر مربع',11,2.40,0.40,0.05,0.08,8,'حدود ۴۸ کیلو در متر مربع با قیمت حدود ۵۰ هزار تومان؛ با بازار صادراتی بازده به حدود ۱۳٪ می‌رسد.',1,[3,5,10,7,4,10]],
 ['mushroom','قارچ خوراکی (دکمه‌ای)','تن ظرفیت',398.75,200,0.30,0.06,0.07,8,'هر تن ظرفیت سالانه با قیمت درب مزرعه حدود ۲۰۰ هزار تومان؛ با برند و بسته‌بندی بازده تقریباً دو برابر می‌شود.',1,[6,6,9,6,6,9]]
];
var DEF={};
var S=BASE.map(function(r){var o={k:r[0],name:r[1],unit:r[2],fixed:r[3],rev:r[4],margin:r[5],wc:r[6],dep:r[7],months:r[8],desc:r[9],est:!!r[10],sc:r[11]};DEF[o.k]=JSON.parse(JSON.stringify(o));return o;});
var BY={};S.forEach(function(s){BY[s.k]=s;});

/* ---------- helpers ---------- */
var fa=new Intl.NumberFormat('fa-IR',{maximumFractionDigits:1});
var fa0=new Intl.NumberFormat('fa-IR',{maximumFractionDigits:0});
var fa2=new Intl.NumberFormat('fa-IR',{maximumFractionDigits:2});
function pct(x,d){if(!isFinite(x))return '—';return (d===0?fa0:fa).format(x*100)+'٪';}
function money(m){ // m in million toman
  if(!isFinite(m))return '—';var a=Math.abs(m),s=m<0?'−':'';if(a<0.0005)return '۰';
  if(a>=1000)return s+fa.format(a/1000)+' میلیارد';
  if(a>=1)return s+fa.format(a)+' میلیون';
  return s+fa0.format(a*1000)+' هزار';
}
function $(id){return document.getElementById(id);}
function el(tag,attrs,txt){var e=document.createElementNS(tag==='svg'||/^(rect|line|text|path|g|polyline|circle)$/.test(tag)?'http://www.w3.org/2000/svg':'http://www.w3.org/1999/xhtml',tag);for(var a in attrs)e.setAttribute(a,attrs[a]);if(txt!=null)e.textContent=(tag==='text'?'\u2067'+txt+'\u2069':txt);return e;}
function css(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim();}
function safeGet(k){try{return localStorage.getItem(k);}catch(e){return null;}}
function safeSet(k,v){try{localStorage.setItem(k,v);}catch(e){}}

/* ---------- theme ---------- */
var themes=['auto','light','dark'],tIdx=Math.max(0,themes.indexOf(safeGet('agri-theme')||'auto'));
function applyTheme(){var t=themes[tIdx];if(t==='auto')document.documentElement.removeAttribute('data-theme');else document.documentElement.setAttribute('data-theme',t);$('themeBtn').setAttribute('aria-label','پوسته: '+({auto:'خودکار',light:'روشن',dark:'تیره'})[t]);}
$('themeBtn').addEventListener('click',function(){tIdx=(tIdx+1)%3;safeSet('agri-theme',themes[tIdx]);applyTheme();renderAll();});
applyTheme();
if(window.matchMedia){var mq=window.matchMedia('(prefers-color-scheme: dark)');if(mq.addEventListener)mq.addEventListener('change',function(){renderAll();});}

/* ---------- economics ---------- */
var G={p:0,c:0,x:0};
function econ(s){
  var rev=s.rev*(1+G.p), cost=s.rev*(1-s.margin)*(1+G.c), e=rev-cost;
  var fixed=s.fixed*(1+G.x), wcAbs=s.fixed*s.wc*(1+G.c), I=fixed+wcAbs;
  var net=e-fixed*s.dep, roi=net/I, pb=e>0?s.months/12+I/e:Infinity;
  return {rev:rev,cost:cost,e:e,fixed:fixed,wc:wcAbs,I:I,net:net,roi:roi,pb:pb,turn:rev/fixed,margin:rev>0?e/rev:0,per10:net*(10000/I)};
}

/* ---------- table + chart ---------- */
var sortK='roi',sortDir=-1,selK='mushroom';
function renderTable(){
  var rows=S.map(function(s){var r=econ(s);r.s=s;r.name=s.name;return r;});
  rows.sort(function(a,b){var va=sortK==='name'?a.name:(sortK==='fixed'?a.fixed:a[sortK]),vb=sortK==='name'?b.name:(sortK==='fixed'?b.fixed:b[sortK]);
    if(sortK==='name')return sortDir*va.localeCompare(vb,'fa');
    if(!isFinite(va))va=sortDir<0?-1e18:1e18;if(!isFinite(vb))vb=sortDir<0?-1e18:1e18;return sortDir*(va-vb);});
  var tb=document.querySelector('#tbl tbody');tb.textContent='';
  rows.forEach(function(r){
    var tr=el('tr',{'data-k':r.s.k,tabindex:'0'});if(r.s.k===selK)tr.className='sel';
    var td=el('td');td.appendChild(document.createTextNode(r.s.name));if(r.s.est)td.appendChild(el('span',{'class':'tag e'},'تخمین'));tr.appendChild(td);
    tr.appendChild(el('td',{},money(r.fixed)+' / '+r.s.unit));
    tr.appendChild(el('td',{},money(r.rev)));
    tr.appendChild(el('td',{},fa2.format(r.turn)));
    tr.appendChild(el('td',{},pct(r.margin,0)));
    tr.appendChild(el('td',{'class':r.roi<0?'neg':(r.roi>=0.12?'pos':'')},pct(r.roi)));
    tr.appendChild(el('td',{},isFinite(r.pb)&&r.pb<60?fa.format(r.pb):'هرگز'));
    tr.appendChild(el('td',{'class':r.per10<0?'neg':''},money(r.per10)));
    tb.appendChild(tr);
  });
  document.querySelectorAll('#tbl th button').forEach(function(b){b.setAttribute('aria-sort',b.dataset.k===sortK?(sortDir<0?'descending':'ascending'):'none');});
}
function renderRoiChart(){
  var svg=$('roiChart');svg.textContent='';
  var rows=S.map(function(s){return {s:s,r:econ(s).roi};}).sort(function(a,b){return b.r-a.r;});
  var W=560,rowH=24,top=8,H=top+rows.length*rowH+24,labW=170;
  svg.setAttribute('viewBox','0 0 '+W+' '+H);
  var vals=rows.map(function(x){return x.r;});
  var mn=Math.min(0,Math.min.apply(null,vals)),mx=Math.max(0.05,Math.max.apply(null,vals));
  var plotX0=48,plotX1=W-labW-10; // RTL: labels on right
  function X(v){return plotX1-(v-mn)/(mx-mn)*(plotX1-plotX0);} // larger -> left
  var bar=css('--bar'),bad=css('--bad'),grid=css('--grid'),fg=css('--fg');
  var z=X(0);
  [0,0.1,0.2,0.3,0.4].forEach(function(t){if(t>mx)return;var x=X(t);svg.appendChild(el('line',{x1:x,x2:x,y1:top,y2:H-20,stroke:grid,'stroke-width':1}));svg.appendChild(el('text',{x:x,y:H-6,'font-size':10,'text-anchor':'middle'},pct(t,0)));});
  rows.forEach(function(x,i){
    var y=top+i*rowH, xv=X(x.r), sel=x.s.k===selK;
    var g=el('g',{style:'cursor:pointer','data-k':x.s.k});
    g.appendChild(el('rect',{x:Math.min(xv,z),y:y+4,width:Math.max(1,Math.abs(z-xv)),height:rowH-8,rx:3,fill:x.r<0?bad:bar,opacity:sel?1:0.72}));
    g.appendChild(el('text',{x:W-4,y:y+rowH/2+4,'text-anchor':'end','class':'lbl','font-weight':sel?'700':'400'},x.s.name));
    var lx=x.r>=0?xv-4:xv+4;
    g.appendChild(el('text',{x:lx,y:y+rowH/2+4,'text-anchor':x.r>=0?'end':'start','font-size':10.5,fill:fg},pct(x.r)));
    g.addEventListener('click',function(){select(x.s.k);});
    svg.appendChild(g);
  });
  svg.appendChild(el('line',{x1:z,x2:z,y1:top,y2:H-20,stroke:fg,'stroke-width':1}));
}

/* ---------- detail ---------- */
var FIELDS=[['fixed','سرمایهٔ ثابت هر واحد (میلیون)',0.01],['rev','درآمد سالانهٔ هر واحد (میلیون)',0.01],['margin','حاشیهٔ EBITDA (٪)',1,100],['wc','سرمایه در گردش (٪ ثابت)',1,100],['dep','استهلاک سالانه (٪ ثابت)',0.5,100],['months','ماه تا اولین درآمد',1]];
function renderDetail(){
  var s=BY[selK],r=econ(s);
  $('dTitle').textContent=s.name;
  $('dDesc').textContent=s.desc;
  var k=$('dKpis');k.textContent='';
  [['بازده سالانه',pct(r.roi),r.roi<0?'neg':(r.roi>=0.12?'pos':'')],['دورهٔ بازگشت',isFinite(r.pb)&&r.pb<60?fa.format(r.pb)+' سال':'هرگز',''],['کل سرمایهٔ هر واحد',money(r.I),''],['EBITDA هر واحد',money(r.e),r.e<0?'neg':''],
   ['تغییر سود با ۱۰٪ قیمت کمتر',sens(s),'']].forEach(function(a){var d=el('div',{'class':'kpi'});d.appendChild(el('span',{},a[0]));d.appendChild(el('strong',{'class':a[2]},a[1]));k.appendChild(d);});
  var box=$('dInputs');box.textContent='';
  FIELDS.forEach(function(f){
    var id='in-'+f[0],w=el('div',{'class':'ctl'});
    w.appendChild(el('label',{'for':id},f[1]));
    var v=f[3]?+(s[f[0]]*f[3]).toFixed(2):s[f[0]];
    var inp=el('input',{id:id,type:'number',step:String(f[2]),value:String(v),min:'0'});
    inp.addEventListener('change',function(){var n=parseFloat(inp.value);if(!isFinite(n)||n<0){inp.value=String(v);return;}
      if(f[0]==='margin'&&n>95)n=95;s[f[0]]=f[3]?n/f[3]:n;renderAll(true);});
    w.appendChild(inp);box.appendChild(w);
  });
}
function sens(s){var b=econ(s).net,save=G.p;G.p=save-0.10;var l=econ(s).net;G.p=save;if(Math.abs(b)<1e-9)return '—';var ch=(l-b)/Math.abs(b);return pct(ch,0);}
$('dReset').addEventListener('click',function(){var d=DEF[selK],s=BY[selK];['fixed','rev','margin','wc','dep','months'].forEach(function(f){s[f]=d[f];});renderAll();});
function select(k){selK=k;$('lSector').value=k;renderAll();}

/* ---------- loan model ---------- */
function loanSim(s,o){
  // o: budgetM (million), share, rate, termY, grace, inf, gap, resid
  var r=econ(s); if(r.I<=0) return null;
  var units=o.budget/r.I, I=o.budget, L=I*o.share, E=I-L;
  var mi=Math.pow(1+o.inf,1/12)-1, mg=Math.pow(1+o.inf+o.gap,1/12)-1, mr=o.rate/12;
  var n=Math.round(o.termY*12), G0=o.grace;
  var pay=n>0?(mr>0?L*mr/(1-Math.pow(1+mr,-n)):L/n):0;
  var revM=r.rev*units/12, costM=r.cost*units/12;
  var cfL=[-E],cfU=[-I],years=[],bal=L,y=null;
  var N=120;
  for(var m=1;m<=N;m++){
    var op=m>s.months;
    var rv=op?revM*Math.pow(1+mg,m):0, cs=op?costM*Math.pow(1+mi,m):0, eb=rv-cs;
    var ds=0;
    if(L>0){
      if(m<=G0){ds=bal*mr;}
      else if(m<=G0+n){var it=bal*mr,pr=pay-it;bal=Math.max(0,bal-pr);ds=pay;}
    }
    var cL=eb-ds,cU=eb;
    if(m===N&&o.resid){
      var resid=r.fixed*units*Math.pow(1+mi,N)*Math.max(0,1-s.dep*10)+r.wc*units*Math.pow(1+mi,N);
      cL+=resid-(bal>0?bal:0);cU+=resid;
    }
    cfL.push(cL);cfU.push(cU);
    var yi=Math.ceil(m/12)-1;if(!years[yi])years[yi]={rev:0,eb:0,ds:0,cf:0,real:0};
    years[yi].rev+=rv;years[yi].eb+=eb;years[yi].ds+=ds;years[yi].cf+=cL;years[yi].real+=cL/Math.pow(1+mi,m);
  }
  function npv(cf,rate){var s=0;for(var i=0;i<cf.length;i++)s+=cf[i]/Math.pow(1+rate,i);return s;}
  function irr(cf){var lo=-0.3,hi=1,flo=npv(cf,lo),fhi=npv(cf,hi);if(!isFinite(flo)||flo*fhi>0)return NaN;for(var i=0;i<200;i++){var md=(lo+hi)/2,f=npv(cf,md);if(f*flo>0){lo=md;flo=f;}else hi=md;}return Math.pow(1+(lo+hi)/2,12)-1;}
  function realCum(cf){var c=0,out=[],pb=null;for(var i=0;i<cf.length;i++){c+=cf[i]/Math.pow(1+mi,i);out.push(c);if(pb===null&&i>0&&c>=0)pb=i;}return {c:out,pb:pb};}
  var rl=realCum(cfL),ru=realCum(cfU);
  var irrL=irr(cfL),irrU=irr(cfU);
  var realL=isFinite(irrL)?(1+irrL)/(1+o.inf)-1:NaN, realU=isFinite(irrU)?(1+irrU)/(1+o.inf)-1:NaN;
  var dscr=null,fullFrom=Math.ceil(s.months/12);years.forEach(function(yr,i){if(i>=fullFrom&&yr.ds>0){var d=yr.eb/yr.ds;if(dscr===null||d<dscr)dscr=d;}});
  var realRate=(1+o.rate)/(1+o.inf)-1;
  return {units:units,I:I,L:L,E:E,pay:pay,years:years,cumL:rl.c,cumU:ru.c,pbL:rl.pb,pbU:ru.pb,irrL:irrL,irrU:irrU,realL:realL,realU:realU,dscr:dscr,realRate:realRate,npvL:npv(cfL,mi),npvU:npv(cfU,mi)};
}
function loanOpts(){
  var b=parseFloat($('lBudget').value);if(!isFinite(b)||b<=0)b=50;
  return {budget:b*1000,share:+$('lShare').value/100,rate:+$('lRate').value/100,termY:+$('lTerm').value,grace:+$('lGrace').value,inf:+$('lInf').value/100,gap:+$('lGap').value/100,resid:$('lResid').checked};
}
function kpi(box,label,val,cls,sub){var d=el('div',{'class':'kpi'});d.appendChild(el('span',{},label));d.appendChild(el('strong',{'class':cls||''},val));if(sub)d.appendChild(el('em',{},sub));box.appendChild(d);}
function pbTxt(m){return m===null?'بیش از ۱۰ سال':fa.format(m/12)+' سال';}
function renderLoan(){
  var s=BY[$('lSector').value]||BY.mushroom,o=loanOpts(),R=loanSim(s,o);
  $('oShare').textContent=fa0.format(o.share*100)+'٪';$('oRate').textContent=fa0.format(o.rate*100)+'٪';$('oTerm').textContent=fa0.format(o.termY)+' سال';
  $('oGrace').textContent=fa0.format(o.grace)+' ماه';$('oInf').textContent=fa0.format(o.inf*100)+'٪';$('oGap').textContent=(o.gap>0?'+':'')+fa0.format(o.gap*100)+' واحد';
  $('lTitle').textContent='نتیجه برای '+s.name;
  var k=$('lKpis');k.textContent='';
  if(!R){k.appendChild(el('p',{},'داده کافی نیست.'));return;}
  kpi(k,'ظرفیت قابل خرید',fa0.format(R.units)+' '+s.unit);
  kpi(k,'سهم آورده',money(R.E),'',R.L>0?'وام: '+money(R.L):'بدون وام');
  kpi(k,'قسط ماهانه بعد از تنفس',R.L>0?money(R.pay):'—');
  kpi(k,'نرخ واقعی وام',pct(R.realRate),R.realRate<0?'pos':'neg',R.realRate<0?'منفی یعنی وام به نفع وام‌گیرنده است':'وام از تورم گران‌تر است');
  kpi(k,'بازده واقعی آورده (با وام)',pct(R.realL),R.realL<0?'neg':'pos','IRR اسمی: '+pct(R.irrL));
  kpi(k,'بازده واقعی بدون وام',pct(R.realU),R.realU<0?'neg':'','IRR اسمی: '+pct(R.irrU));
  kpi(k,'بازگشت آورده (واقعی)',pbTxt(R.pbL),'','بدون وام: '+pbTxt(R.pbU));
  kpi(k,'کمترین DSCR (سال‌های کامل بهره‌برداری)',R.dscr===null?'—':fa2.format(R.dscr),R.dscr!==null&&R.dscr<1.2?'neg':'', R.dscr!==null&&R.dscr<1?'درآمد قسط را پوشش نمی‌دهد':'');
  var v=$('lVerdict'),txt,warn=false;
  var lev=(isFinite(R.realL)&&isFinite(R.realU))?R.realL-R.realU:NaN;
  if(R.L===0)txt='بدون وام، بازده واقعی سرمایه '+pct(R.realU)+' است.';
  else if(R.dscr!==null&&R.dscr<1){warn=true;txt='در دست‌کم یک سال، درآمد عملیاتی قسط وام را پوشش نمی‌دهد. یا دورهٔ تنفس را بیشتر کنید، یا سهم وام را کم کنید.';}
  else if(isFinite(lev)&&lev>0){txt='وام بازده واقعی سهم شما را حدود '+pct(lev)+' بالا می‌برد. بخشی از این مزیت از منفی‌بودن نرخ واقعی وام می‌آید، نه از خود تولید.';}
  else if(isFinite(lev)){warn=true;txt='با این شرایط وام بازده سهم شما را پایین می‌آورد؛ بازده عملیاتی فعالیت از هزینهٔ واقعی وام کمتر است.';}
  else {warn=true;txt='جریان نقدی در افق ده‌ساله به نقطهٔ بازگشت نمی‌رسد؛ با این فرض‌ها طرح توجیه مالی ندارد.';}
  v.textContent=txt;v.className='verdict'+(warn?' warn':'');
  renderCf(R);
  var tb=document.querySelector('#cfTbl tbody');tb.textContent='';
  R.years.forEach(function(yr,i){var tr=el('tr');[fa0.format(i+1),money(yr.rev),money(yr.eb),money(yr.ds),money(yr.cf),money(yr.real),yr.ds>0&&i>=Math.ceil(s.months/12)?fa2.format(yr.eb/yr.ds):'—'].forEach(function(c,j){tr.appendChild(el('td',{'class':(j===4||j===5)&&(j===4?yr.cf:yr.real)<0?'neg':''},c));});tb.appendChild(tr);});
}
function renderCf(R){
  var svg=$('cfChart');svg.textContent='';
  var W=720,H=280,pl=24,pr=100,pt=12,pb=28;svg.setAttribute('viewBox','0 0 '+W+' '+H);
  var all=R.cumL.concat(R.cumU),mn=Math.min.apply(null,all),mx=Math.max.apply(null,all);if(mx===mn){mx+=1;}
  var pad=(mx-mn)*0.06;mn-=pad;mx+=pad;
  var n=R.cumL.length-1;
  function X(i){return W-pr-(i/n)*(W-pr-pl);} // RTL: time flows right-to-left
  function Y(v){return pt+(mx-v)/(mx-mn)*(H-pt-pb);}
  var grid=css('--grid'),fg=css('--fg');
  for(var t=0;t<=5;t++){var v=mn+(mx-mn)*t/5,y=Y(v);svg.appendChild(el('line',{x1:pl,x2:W-pr,y1:y,y2:y,stroke:grid}));svg.appendChild(el('text',{x:W-pr+6,y:y+4,'font-size':10,'text-anchor':'start'},money(v)));}
  for(var yr=0;yr<=10;yr+=2){var x=X(yr*12);svg.appendChild(el('text',{x:x,y:H-8,'font-size':10.5,'text-anchor':'middle'},'سال '+fa0.format(yr)));}
  if(mn<0&&mx>0)svg.appendChild(el('line',{x1:pl,x2:W-pr,y1:Y(0),y2:Y(0),stroke:fg,'stroke-width':1}));
  function line(arr,color){var p='';for(var i=0;i<arr.length;i++)p+=(i?' ':'')+X(i).toFixed(1)+','+Y(arr[i]).toFixed(1);svg.appendChild(el('polyline',{points:p,fill:'none',stroke:color,'stroke-width':2.5,'stroke-linejoin':'round'}));}
  line(R.cumU,css('--bar2'));line(R.cumL,css('--bar'));
}

/* ---------- scoring ---------- */
var WN=['بازگشت','حاشیهٔ سود','آب و اقلیم','ریسک زیستی','استقلال از واردات','آینده و فناوری'],W=[20,20,15,15,15,15];
(function(){var box=$('wCtl');WN.forEach(function(n,i){var w=el('div',{'class':'ctl'}),id='w'+i;var lab=el('label',{'for':id});lab.appendChild(document.createTextNode(n+' '));var out=el('output',{id:'ow'+i},fa0.format(W[i])+'٪');lab.appendChild(out);w.appendChild(lab);
  var inp=el('input',{id:id,type:'range',min:'0',max:'40',step:'5',value:String(W[i])});inp.addEventListener('input',function(){W[i]=+inp.value;renderScore();});w.appendChild(inp);box.appendChild(w);});})();
function renderScore(){
  var tot=W.reduce(function(a,b){return a+b;},0)||1;
  W.forEach(function(w,i){$('ow'+i).textContent=fa0.format(w/tot*100)+'٪';});
  var rows=S.map(function(s){var sc=s.sc.reduce(function(a,v,i){return a+v*W[i]/tot;},0);return {s:s,sc:sc};}).sort(function(a,b){return b.sc-a.sc;});
  var tb=document.querySelector('#scTbl tbody');tb.textContent='';
  rows.forEach(function(r,i){var tr=el('tr',{'data-k':r.s.k,tabindex:'0'});tr.appendChild(el('td',{},fa0.format(i+1)));tr.appendChild(el('td',{},r.s.name));r.s.sc.forEach(function(v){tr.appendChild(el('td',{},fa0.format(v)));});tr.appendChild(el('td',{'class':'pos'},fa2.format(r.sc)));tb.appendChild(tr);});
}

/* ---------- wiring ---------- */
function syncSeg(){var key=[G.p*100,G.c*100,G.x*100].map(Math.round).join(',');document.querySelectorAll('[data-scn]').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.scn===key));});}
function readG(){G.p=+$('gPrice').value/100;G.c=+$('gCost').value/100;G.x=+$('gCapex').value/100;
  $('oPrice').textContent=(G.p>0?'+':'')+fa0.format(G.p*100)+'٪';$('oCost').textContent=(G.c>0?'+':'')+fa0.format(G.c*100)+'٪';$('oCapex').textContent=(G.x>0?'+':'')+fa0.format(G.x*100)+'٪';syncSeg();}
['gPrice','gCost','gCapex'].forEach(function(id){$(id).addEventListener('input',function(){readG();renderAll();});});
document.querySelectorAll('[data-scn]').forEach(function(b){b.addEventListener('click',function(){var v=b.dataset.scn.split(',');$('gPrice').value=v[0];$('gCost').value=v[1];$('gCapex').value=v[2];readG();renderAll();});});
document.querySelectorAll('#tbl th button').forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.k;if(sortK===k)sortDir=-sortDir;else{sortK=k;sortDir=k==='name'||k==='pb'||k==='fixed'?1:-1;}renderTable();});});
function rowPick(e){var tr=e.target.closest('tr[data-k]');if(!tr)return;if(e.type==='keydown'&&e.key!=='Enter'&&e.key!==' ')return;if(e.type==='keydown')e.preventDefault();select(tr.dataset.k);}
['click','keydown'].forEach(function(t){document.querySelector('#tbl tbody').addEventListener(t,rowPick);document.querySelector('#scTbl tbody').addEventListener(t,rowPick);});
var sel=$('lSector');S.forEach(function(s){sel.appendChild(el('option',{value:s.k},s.name));});sel.value=selK;
sel.addEventListener('change',function(){selK=sel.value;renderAll();});
['lBudget','lShare','lRate','lTerm','lGrace','lInf','lGap','lResid'].forEach(function(id){$(id).addEventListener('input',renderLoan);$(id).addEventListener('change',renderLoan);});

function renderAll(keepDetailInputs){renderTable();renderRoiChart();if(keepDetailInputs){var s=BY[selK],r=econ(s);/* refresh kpis only */var save=document.activeElement&&document.activeElement.id;renderDetail();if(save&&$(save))$(save).focus();}else renderDetail();renderLoan();renderScore();}
readG();renderAll();
})();
  }
}
dcMount(["\n","\n",{"n":"div","k":["\n",{"n":"header","a":{"class":"top"},"k":[{"n":"div","a":{"class":"top-in"},"k":["\n  ",{"n":"a","a":{"class":"brand","href":"./"},"k":[{"n":"i","a":{"aria-hidden":"true"}},"رضا هاشمی"]},"\n  ",{"n":"nav","a":{"aria-label":"بخش‌های صفحه"},"k":["\n    ",{"n":"a","a":{"href":"#dashboard"},"k":["داشبورد"]},"\n    ",{"n":"a","a":{"href":"#loan"},"k":["مدل وام"]},"\n    ",{"n":"a","a":{"href":"#score"},"k":["امتیازدهی"]},"\n    ",{"n":"a","a":{"href":"#method"},"k":["روش و منابع"]},"\n    ",{"n":"a","a":{"href":"./#writing"},"k":["نوشته‌ها"]},"\n  "]},"\n  ",{"n":"button","a":{"class":"tbtn","id":"themeBtn","type":"button","aria-label":"تغییر پوسته","title":"تغییر پوسته"},"k":[{"n":"svg","a":{"viewBox":"0 0 16 16","width":"15","height":"15","aria-hidden":"true"},"k":[{"n":"circle","a":{"cx":"8","cy":"8","r":"6.3","fill":"none","stroke":"currentColor","stroke-width":"1.5"},"sf":1},{"n":"path","a":{"d":"M8 1.7a6.3 6.3 0 0 1 0 12.6z","fill":"currentColor"},"sf":1}]}]},"\n"]}]},"\n\n",{"n":"main","k":["\n  ",{"n":"p","a":{"class":"eyebrow"},"k":["اقتصاد کشاورزی · داشبورد تعاملی"]},"\n  ",{"n":"h1","k":["سرمایه‌گذاری در کشاورزی، با عدد"]},"\n  ",{"n":"p","a":{"class":"lead"},"k":["جدول‌های رسمی معمولاً فقط می‌گویند ورود به هر فعالیت چقدر سرمایهٔ ثابت می‌خواهد. این صفحه یک قدم جلوتر می‌رود: برای ۱۹ فعالیت کشاورزی، درآمد، سود، دورهٔ بازگشت و اثر وام و تورم را کنار هم می‌گذارد تا بتوانید فرض‌ها را خودتان عوض کنید و نتیجه را همان لحظه ببینید."]},"\n  ",{"n":"p","a":{"class":"note"},"k":["پایهٔ سرمایهٔ ثابت: برآورد مهندسین مشاور پارس رابین برای سه‌ماههٔ چهارم ۱۴۰۵ (با دامنهٔ نوسان ±۲۰٪). قیمت‌های فروش از بازار مهر ۱۴۰۵ است و هر جا عدد دقیق در دسترس نبود، با برچسب «تخمین» مشخص شده. این ابزار برای غربال اولیه ساخته شده و جای طرح توجیهی را نمی‌گیرد."]},"\n\n  ",{"n":"section","a":{"aria-labelledby":"h-find"},"k":["\n    ",{"n":"h2","a":{"id":"h-find","style":"font-size:20px"},"k":["چهار یافتهٔ اصلی"]},"\n    ",{"n":"div","a":{"class":"grid g4"},"k":["\n      ",{"n":"div","a":{"class":"card find"},"k":[{"n":"b","k":["گردش دارایی"]},{"n":"p","k":["وقتی درآمد سالانه کمتر از یک‌سوم سرمایهٔ ثابت باشد، با قیمت بازار داخلی سودی باقی نمی‌ماند؛ گلخانه و شیلات گوشتی در این دسته‌اند."]}]},"\n      ",{"n":"div","a":{"class":"card find b"},"k":[{"n":"b","k":["اهرم قیمت"]},{"n":"p","k":["مرغ، بوقلمون و پرواربندی با ۲۰٪ افزایش قیمت چند برابر سود می‌دهند و با ۱۰٪ کاهش زیان‌ده می‌شوند."]}]},"\n      ",{"n":"div","a":{"class":"card find"},"k":[{"n":"b","k":["تاب‌آوری"]},{"n":"p","k":["زنبور عسل، میگو و قارچ در سناریوی بد هم سودشان را نگه می‌دارند."]}]},"\n      ",{"n":"div","a":{"class":"card find b"},"k":[{"n":"b","k":["وام ارزان"]},{"n":"p","k":["وقتی تورم از نرخ وام بالاتر است، بخش بزرگی از بازده سهم سرمایه‌گذار از خود وام می‌آید، نه از تولید. بخش «مدل وام» این را نشان می‌دهد."]}]},"\n    "]},"\n  "]},"\n\n  ","\n  ",{"n":"section","a":{"id":"dashboard","aria-labelledby":"h-dash"},"k":["\n    ",{"n":"p","a":{"class":"eyebrow"},"k":["بخش ۱"]},"\n    ",{"n":"h2","a":{"id":"h-dash"},"k":["مقایسهٔ ۱۹ فعالیت"]},"\n    ",{"n":"p","a":{"class":"muted"},"k":["با لغزنده‌ها کل بازار را جابه‌جا کنید. روی هر ردیف جدول بزنید تا فرض‌های همان فعالیت را ببینید و ویرایش کنید؛ همان فعالیت در مدل وام هم انتخاب می‌شود."]},"\n\n    ",{"n":"div","a":{"class":"card"},"k":["\n      ",{"n":"div","a":{"class":"grid g3"},"k":["\n        ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"gPrice"},"k":["تغییر قیمت فروش ",{"n":"output","a":{"id":"oPrice"},"k":["۰٪"]}]},{"n":"input","a":{"id":"gPrice","type":"range","min":"-30","max":"50","step":"5","value":"0"}}]},"\n        ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"gCost"},"k":["تغییر هزینهٔ جاری (خوراک، انرژی، دستمزد) ",{"n":"output","a":{"id":"oCost"},"k":["۰٪"]}]},{"n":"input","a":{"id":"gCost","type":"range","min":"-20","max":"40","step":"5","value":"0"}}]},"\n        ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"gCapex"},"k":["تغییر سرمایهٔ ثابت (دامنهٔ ±۲۰٪ جدول) ",{"n":"output","a":{"id":"oCapex"},"k":["۰٪"]}]},{"n":"input","a":{"id":"gCapex","type":"range","min":"-20","max":"20","step":"5","value":"0"}}]},"\n      "]},"\n      ",{"n":"div","a":{"class":"row","style":"margin-top:12px"},"k":["\n        ",{"n":"span","a":{"class":"small muted"},"k":["سناریوی آماده:"]},"\n        ",{"n":"div","a":{"class":"seg","role":"group","aria-label":"سناریوها"},"k":["\n          ",{"n":"button","a":{"type":"button","data-scn":"0,0,0","aria-pressed":"true"},"k":["پایه"]},"\n          ",{"n":"button","a":{"type":"button","data-scn":"20,0,0","aria-pressed":"false"},"k":["قیمت +۲۰٪"]},"\n          ",{"n":"button","a":{"type":"button","data-scn":"-10,0,20","aria-pressed":"false"},"k":["بدبینانه"]},"\n          ",{"n":"button","a":{"type":"button","data-scn":"0,25,0","aria-pressed":"false"},"k":["جهش نهاده"]},"\n        "]},"\n      "]},"\n    "],"c":"chf"},"\n\n    ",{"n":"div","a":{"class":"grid g2"},"k":["\n      ",{"n":"div","a":{"class":"card"},"k":["\n        ",{"n":"h3","k":["بازده سالانهٔ سرمایه (ROI)"]},"\n        ",{"n":"p","a":{"class":"small muted","style":"margin:0 0 6px"},"k":["سود خالص بعد از استهلاک، تقسیم بر سرمایهٔ ثابت به‌اضافهٔ سرمایه در گردش. ارقام به قیمت ثابت امروزند، پس تقریباً «واقعی»‌اند."]},"\n        ",{"n":"svg","a":{"id":"roiChart","class":"chart","role":"img","aria-label":"نمودار میله‌ای بازده سرمایهٔ فعالیت‌ها"}},"\n      "]},"\n      ",{"n":"div","a":{"class":"card","id":"detail"},"k":["\n        ",{"n":"h3","a":{"id":"dTitle"},"k":["—"]},"\n        ",{"n":"p","a":{"class":"small muted","id":"dDesc","style":"margin:0 0 10px"}},"\n        ",{"n":"div","a":{"class":"kpis","id":"dKpis"}},"\n        ",{"n":"h3","k":["فرض‌های این فعالیت"],"a":{"style":"margin-top:16px;font-size:15px"}},"\n        ",{"n":"div","a":{"class":"grid g3","id":"dInputs","style":"gap:10px"}},"\n        ",{"n":"div","a":{"class":"row"},"k":[{"n":"button","a":{"type":"button","class":"btn","id":"dReset"},"k":["بازگرداندن فرض‌های پیش‌فرض"]}],"c":"cwf"},"\n      "]},"\n    "],"c":"chf"},"\n\n    ",{"n":"div","a":{"class":"tbox"},"k":["\n      ",{"n":"table","a":{"id":"tbl"},"k":["\n        ",{"n":"thead","k":[{"n":"tr","k":["\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"name"},"k":["فعالیت"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"fixed"},"k":["سرمایهٔ ثابت/واحد"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"rev"},"k":["درآمد سالانه/واحد"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"turn"},"k":["گردش دارایی"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"margin"},"k":["حاشیهٔ EBITDA"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"roi","aria-sort":"descending"},"k":["ROI"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"pb"},"k":["بازگشت (سال)"]}]},"\n          ",{"n":"th","a":{"scope":"col"},"k":[{"n":"button","a":{"type":"button","data-k":"per10"},"k":["سود سالانهٔ ۱۰ میلیارد"]}]},"\n        "]}]},"\n        ",{"n":"tbody"},"\n      "]},"\n    "],"c":"chf"},"\n    ",{"n":"p","a":{"class":"small muted","style":"margin-top:8px"},"k":["مبالغ به میلیون تومان، مگر جایی که واحد دیگری نوشته شده. «سود سالانهٔ ۱۰ میلیارد» یعنی اگر ۱۰ میلیارد تومان کل سرمایه (ثابت و در گردش) وارد همین فعالیت شود."]},"\n  "]},"\n\n  ","\n  ",{"n":"section","a":{"id":"loan","aria-labelledby":"h-loan"},"k":["\n    ",{"n":"p","a":{"class":"eyebrow"},"k":["بخش ۲"]},"\n    ",{"n":"h2","a":{"id":"h-loan"},"k":["مدل وام و تورم"]},"\n    ",{"n":"p","a":{"class":"muted"},"k":["در اقتصاد تورمی، قسط وام ثابت می‌ماند ولی قیمت محصول بالا می‌رود. این مدل جریان نقدی ماه‌به‌ماه را برای ده سال شبیه‌سازی می‌کند و بازده سهم سرمایه‌گذار را با وام و بدون وام مقایسه می‌کند."]},"\n\n    ",{"n":"div","a":{"class":"grid g2"},"k":["\n      ",{"n":"div","a":{"class":"card"},"k":["\n        ",{"n":"div","a":{"class":"grid g3"},"k":["\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lSector"},"k":["فعالیت"]},{"n":"select","a":{"id":"lSector"}}],"c":"cwh"},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lBudget"},"k":["کل سرمایهٔ طرح (میلیارد تومان)"]},{"n":"input","a":{"id":"lBudget","type":"number","min":"1","max":"5000","step":"1","value":"50"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lShare"},"k":["سهم وام ",{"n":"output","a":{"id":"oShare"},"k":["۶۰٪"]}]},{"n":"input","a":{"id":"lShare","type":"range","min":"0","max":"80","step":"5","value":"60"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lRate"},"k":["نرخ سود وام (سالانه) ",{"n":"output","a":{"id":"oRate"},"k":["۲۳٪"]}]},{"n":"input","a":{"id":"lRate","type":"range","min":"4","max":"40","step":"1","value":"23"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lTerm"},"k":["مدت بازپرداخت ",{"n":"output","a":{"id":"oTerm"},"k":["۵ سال"]}]},{"n":"input","a":{"id":"lTerm","type":"range","min":"1","max":"10","step":"1","value":"5"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lGrace"},"k":["دورهٔ تنفس ",{"n":"output","a":{"id":"oGrace"},"k":["۱۲ ماه"]}]},{"n":"input","a":{"id":"lGrace","type":"range","min":"0","max":"36","step":"3","value":"12"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lInf"},"k":["تورم سالانهٔ مورد انتظار ",{"n":"output","a":{"id":"oInf"},"k":["۴۰٪"]}]},{"n":"input","a":{"id":"lInf","type":"range","min":"0","max":"70","step":"5","value":"40"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","a":{"for":"lGap"},"k":["رشد قیمت محصول نسبت به تورم ",{"n":"output","a":{"id":"oGap"},"k":["۰ واحد"]}]},{"n":"input","a":{"id":"lGap","type":"range","min":"-15","max":"10","step":"1","value":"0"}}]},"\n          ",{"n":"div","a":{"class":"ctl"},"k":[{"n":"label","k":[{"n":"span","k":[{"n":"input","a":{"id":"lResid","type":"checkbox","checked":""}}," ارزش باقی‌ماندهٔ دارایی در پایان سال دهم حساب شود"]}]}],"c":"cwh"},"\n        "],"c":"cwg"},"\n        ",{"n":"p","a":{"class":"small muted"},"k":["پیش‌فرض‌ها: نرخ تسهیلات کشاورزی حدود ۱۸ تا ۲۳ درصد و تورم ۴۰ درصد، که هر دو تخمین‌اند و قابل تغییرند. در دورهٔ تنفس فقط سود پرداخت می‌شود و بعد از آن اقساط مساوی ماهانه است. «رشد قیمت نسبت به تورم» برای کالاهایی است که قیمت دستوری دارند و عقب می‌مانند (مثلاً ۵- واحد برای شیر)."],"c":"cwi"},"\n      "]},"\n      ",{"n":"div","a":{"class":"card"},"k":["\n        ",{"n":"h3","a":{"id":"lTitle"},"k":["نتیجه"]},"\n        ",{"n":"div","a":{"class":"kpis","id":"lKpis"}},"\n        ",{"n":"div","a":{"id":"lVerdict","class":"verdict"}},"\n      "]},"\n    "],"c":"chf"},"\n\n    ",{"n":"div","a":{"class":"card"},"k":["\n      ",{"n":"h3","k":["جریان نقدی تجمعی سهم سرمایه‌گذار (به قیمت امروز)"]},"\n      ",{"n":"div","a":{"class":"legend"},"k":[{"n":"span","k":[{"n":"i","a":{"style":"background:var(--bar)"}},"با وام"]},{"n":"span","k":[{"n":"i","a":{"style":"background:var(--bar2)"}},"بدون وام (همهٔ سرمایه از جیب)"]}]},"\n      ",{"n":"svg","a":{"id":"cfChart","class":"chart","role":"img","aria-label":"نمودار جریان نقدی تجمعی ده‌ساله"}},"\n      ",{"n":"p","a":{"class":"small muted","style":"margin:6px 0 0"},"k":["همهٔ مبالغ با نرخ تورم به ارزش امروز برگردانده شده‌اند. جایی که خط از صفر رد می‌شود، سرمایهٔ شخصی برگشته است."]},"\n    "],"c":"chf"},"\n\n    ",{"n":"details","k":["\n      ",{"n":"summary","k":["جدول سالانهٔ جریان نقدی"]},"\n      ",{"n":"div","a":{"class":"tbox"},"k":[{"n":"table","a":{"id":"cfTbl","style":"min-width:640px"},"k":[{"n":"thead","k":[{"n":"tr","k":[{"n":"th","k":["سال"]},{"n":"th","k":["درآمد (اسمی)"]},{"n":"th","k":["EBITDA (اسمی)"]},{"n":"th","k":["قسط و سود وام"]},{"n":"th","k":["جریان نقد سهامدار (اسمی)"]},{"n":"th","k":["همان، به قیمت امروز"]},{"n":"th","k":["DSCR"]}]}]},{"n":"tbody"}]}],"c":"cwf"},"\n      ",{"n":"p","a":{"class":"small muted"},"k":["DSCR یعنی EBITDA تقسیم بر قسط و سود سالانه. بانک‌ها معمولاً حداقل ۱٫۲ تا ۱٫۳ می‌خواهند."]},"\n    "]},"\n  "]},"\n\n  ","\n  ",{"n":"section","a":{"id":"score","aria-labelledby":"h-score"},"k":["\n    ",{"n":"p","a":{"class":"eyebrow"},"k":["بخش ۳"]},"\n    ",{"n":"h2","a":{"id":"h-score"},"k":["ماتریس امتیازدهی"]},"\n    ",{"n":"p","a":{"class":"muted"},"k":["بازده مالی همهٔ ماجرا نیست. شش معیار، هر کدام از ۱ تا ۱۰ (عدد بالاتر یعنی بهتر). وزن‌ها را مطابق اولویت خودتان تغییر دهید."]},"\n    ",{"n":"div","a":{"class":"card"},"k":["\n      ",{"n":"div","a":{"class":"grid g3","id":"wCtl"},"c":"cwg"},"\n      ",{"n":"p","a":{"class":"small muted"},"k":["جمع وزن‌ها خودکار به ۱۰۰٪ نرمال می‌شود."],"c":"cwi"},"\n    "],"c":"chf"},"\n    ",{"n":"div","a":{"class":"tbox"},"k":[{"n":"table","a":{"id":"scTbl"},"k":[{"n":"thead","k":[{"n":"tr","k":[{"n":"th","k":["رتبه"]},{"n":"th","k":["فعالیت"]},{"n":"th","k":["بازگشت"]},{"n":"th","k":["حاشیهٔ سود"]},{"n":"th","k":["آب و اقلیم"]},{"n":"th","k":["ریسک زیستی"]},{"n":"th","k":["استقلال از واردات"]},{"n":"th","k":["آینده و فناوری"]},{"n":"th","k":["امتیاز"]}]}]},{"n":"tbody"}]}],"c":"chf"},"\n  "]},"\n\n  ","\n  ",{"n":"section","a":{"id":"method","aria-labelledby":"h-method"},"k":["\n    ",{"n":"p","a":{"class":"eyebrow"},"k":["بخش ۴"]},"\n    ",{"n":"h2","a":{"id":"h-method"},"k":["روش، فرض‌ها و منابع"]},"\n    ",{"n":"div","a":{"class":"grid g2"},"k":["\n      ",{"n":"div","a":{"class":"card"},"k":["\n        ",{"n":"h3","k":["فرمول‌ها"]},"\n        ",{"n":"p","a":{"class":"small"},"k":["درآمد واحد × (۱ + تغییر قیمت) − هزینهٔ جاری × (۱ + تغییر هزینه) = EBITDA"]},"\n        ",{"n":"p","a":{"class":"small"},"k":["ROI = (EBITDA − استهلاک) ÷ (سرمایهٔ ثابت + سرمایه در گردش)"]},"\n        ",{"n":"p","a":{"class":"small"},"k":["دورهٔ بازگشت ساده = زمان تا اولین درآمد + کل سرمایه ÷ EBITDA"]},"\n        ",{"n":"p","a":{"class":"small"},"k":["مدل وام: شبیه‌سازی ۱۲۰ ماهه، با رشد درآمد و هزینه به اندازهٔ تورم، قسط ثابت اسمی، و تنزیل همه‌چیز با نرخ تورم. IRR از جریان نقدی ماهانهٔ سهامدار محاسبه و سالانه می‌شود."]},"\n        ",{"n":"p","a":{"class":"small muted"},"k":["درآمد کشاورزی طبق مادهٔ ۸۱ قانون مالیات‌های مستقیم معاف است، پس مالیات کسر نشده."]},"\n      "]},"\n      ",{"n":"div","a":{"class":"card"},"k":["\n        ",{"n":"h3","k":["قیمت‌های پایه (مهر ۱۴۰۵)"]},"\n        ",{"n":"ul","a":{"class":"small","style":"padding-inline-start:18px;margin:0"},"k":["\n          ",{"n":"li","k":["شیر خام درب دامداری: ۶۰٬۵۰۰ تومان در کیلو"]},"\n          ",{"n":"li","k":["تخم‌مرغ: شانهٔ ۳۰تایی ۵۳۵ تا ۵۴۰ هزار تومان در خرده‌فروشی؛ حدود ۲۲۰ هزار در کیلو درب مرغداری (تخمین)"]},"\n          ",{"n":"li","k":["قارچ دکمه‌ای: ۲۸۰ هزار تومان خرده‌فروشی؛ حدود ۲۰۰ هزار درب مزرعه (تخمین)"]},"\n          ",{"n":"li","k":["قزل‌آلا: ۴۶۰ هزار تومان خرده‌فروشی؛ حدود ۳۳۰ هزار درب مزرعه (تخمین)"]},"\n          ",{"n":"li","k":["مرغ زنده حدود ۱۷۰ هزار، عسل حدود ۱٫۵ میلیون، گوجهٔ گلخانه‌ای حدود ۴۵ هزار تومان (تخمین)"]},"\n        "]},"\n      "]},"\n    "]},"\n    ",{"n":"details","k":["\n      ",{"n":"summary","k":["محدودیت‌ها"]},"\n      ",{"n":"ul","a":{"class":"small","style":"padding-inline-start:18px"},"k":["\n        ",{"n":"li","k":["واحدها یکسان نیستند: «تن» در شیلات و قارچ یعنی ظرفیت تولید سالانه و «قطعه» در مرغ گوشتی یعنی ظرفیت هر دوره."]},"\n        ",{"n":"li","k":["جدول سرمایهٔ ثابت برای سه‌ماههٔ چهارم ۱۴۰۵ است و قیمت‌های فروش برای مهر؛ پس نتایج کمی محافظه‌کارانه‌اند."]},"\n        ",{"n":"li","k":["حاشیه‌های سود و عملکردها از استانداردهای رایج صنعت برآورد شده‌اند و ممکن است ۱۰ تا ۳۰ درصد با واقعیت یک واحد مشخص فاصله داشته باشند."]},"\n        ",{"n":"li","k":["خاویاری در «فاز پایدار» آمده؛ در هفت تا هشت سال اول تقریباً درآمد خاویار ندارد."]},"\n      "]},"\n    "]},"\n    ",{"n":"h3","k":["منابع"],"a":{"style":"margin-top:20px"}},"\n    ",{"n":"ol","a":{"class":"src"},"k":["\n      ",{"n":"li","k":["مهندسین مشاور پارس رابین (ETARH.com)، برآورد سرمایهٔ ثابت فعالیت‌های اولویت‌دار بخش کشاورزی، سه‌ماههٔ چهارم ۱۴۰۵."]},"\n      ",{"n":"li","k":[{"n":"a","a":{"href":"https://www.yjc.ir/fa/news/9132760","target":"_blank","rel":"noopener"},"k":["قیمت خرید هر کیلو شیر خام ۶۰ هزار و ۵۰۰ تومان، باشگاه خبرنگاران جوان"]}]},"\n      ",{"n":"li","k":[{"n":"a","a":{"href":"https://nabzgheymat.ir/%D9%82%DB%8C%D9%85%D8%AA-%D9%82%D8%A7%D8%B1%DA%86-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%DB%B1%DB%B3-%D9%85%D9%87%D8%B1-%DB%B1%DB%B4%DB%B0%DB%B5-%E2%94%82-%D9%82%D8%A7%D8%B1%DA%86-%D8%AF%DA%A9%D9%85%D9%87/","target":"_blank","rel":"noopener"},"k":["قیمت قارچ، ۱۳ مهر ۱۴۰۵، نبض قیمت"]}]},"\n      ",{"n":"li","k":[{"n":"a","a":{"href":"https://nabzgheymat.ir/%D9%82%DB%8C%D9%85%D8%AA-%D8%AA%D8%AE%D9%85-%D9%85%D8%B1%D8%BA-%D8%AF%D8%B1-%D9%85%D9%87%D8%B1-%DB%B1%DB%B4%DB%B0%DB%B5-%E2%94%82-%D8%B4%D8%A7%D9%86%D9%87-%DB%B3%DB%B0-%D8%B9%D8%AF%D8%AF%DB%8C-%D8%A8/","target":"_blank","rel":"noopener"},"k":["قیمت تخم‌مرغ در مهر ۱۴۰۵، نبض قیمت"]}]},"\n      ",{"n":"li","k":[{"n":"a","a":{"href":"https://www.qudsonline.ir/news/1167496","target":"_blank","rel":"noopener"},"k":["قیمت مرغ، تخم‌مرغ و ماهی، ۴ مهر ۱۴۰۵، قدس آنلاین"]}]},"\n      ",{"n":"li","k":[{"n":"a","a":{"href":"https://nabzgheymat.ir/%D9%82%DB%8C%D9%85%D8%AA-%D8%B9%D8%B3%D9%84-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%D8%B4%D9%86%D8%A8%D9%87-%DB%B1%DB%B8-%D9%85%D9%87%D8%B1-%DB%B1%DB%B4%DB%B0%DB%B5-%E2%94%82-%D8%B9%D8%B3%D9%84-%D8%B7%D8%A8/","target":"_blank","rel":"noopener"},"k":["قیمت عسل، ۱۸ مهر ۱۴۰۵، نبض قیمت"]}]},"\n      ",{"n":"li","k":["Mekonnen, M. M. & Hoekstra, A. Y. — ردپای آب محصولات دامی و گیاهی، Water Footprint Network."]},"\n    "]},"\n  "]},"\n"]},"\n",{"n":"footer","a":{"class":"foot"},"k":[{"n":"span","k":["سرمایه‌گذاری در کشاورزی، با عدد · رضا هاشمی"]},{"n":"span","k":["آخرین به‌روزرسانی: ۲۳ مهر ۱۴۰۵"]}]},"\n\n"],"a":{"style":"direction: rtl"}},"\n"],Component);

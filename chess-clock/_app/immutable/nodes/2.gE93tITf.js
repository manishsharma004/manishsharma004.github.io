import{s as Y,d as q,n as W,r as Z}from"../chunks/scheduler.DHKgWpgq.js";import{S as $,i as x,e as w,b as N,s as L,c as O,d as B,f as U,g as _,h as R,m as k,j as F,k as r,n as z,l as X}from"../chunks/index.vMr7mszy.js";const ee=!0,te=!0,ce=Object.freeze(Object.defineProperty({__proto__:null,prerender:ee,ssr:te},Symbol.toStringTag,{value:"Module"}));function se(s){let t;return{c(){t=N("∥")},l(e){t=U(e,"∥")},m(e,n){F(e,t,n)},d(e){e&&_(t)}}}function le(s){let t;return{c(){t=N("►")},l(e){t=U(e,"►")},m(e,n){F(e,t,n)},d(e){e&&_(t)}}}function ne(s){let t,e,n,d=s[8](s[3])+"",f,p,c,T,u,g=s[8](s[2])+"",E,v,j,h,i,a,D,b,I,S,C,G;function H(l,o){return l[4]?se:le}let V=H(s),m=V(s);return{c(){t=w("div"),e=w("div"),n=w("button"),f=N(d),T=L(),u=w("button"),E=N(g),j=L(),h=w("div"),i=w("button"),m.c(),D=L(),b=w("button"),I=N("↺"),this.h()},l(l){t=O(l,"DIV",{class:!0});var o=B(t);e=O(o,"DIV",{class:!0});var y=B(e);n=O(y,"BUTTON",{class:!0});var J=B(n);f=U(J,d),J.forEach(_),T=R(y),u=O(y,"BUTTON",{class:!0});var K=B(u);E=U(K,g),K.forEach(_),y.forEach(_),j=R(o),h=O(o,"DIV",{class:!0});var P=B(h);i=O(P,"BUTTON",{class:!0});var M=B(i);m.l(M),M.forEach(_),D=R(P),b=O(P,"BUTTON",{class:!0});var Q=B(b);I=U(Q,"↺"),Q.forEach(_),P.forEach(_),o.forEach(_),this.h()},h(){k(n,"class",p=q(`button button-white ${s[1]==="white"?"selected":""}`)+" svelte-pu3rke"),n.disabled=c=!s[0],k(u,"class",v=q(`button button-black ${s[1]==="black"?"selected":""}`)+" svelte-pu3rke"),k(e,"class","buttons svelte-pu3rke"),k(i,"class","button reset-button svelte-pu3rke"),i.disabled=a=!s[0],k(b,"class","button reset-button svelte-pu3rke"),b.disabled=S=!s[0],k(h,"class","actions svelte-pu3rke"),k(t,"class","container svelte-pu3rke")},m(l,o){F(l,t,o),r(t,e),r(e,n),r(n,f),r(e,T),r(e,u),r(u,E),r(t,j),r(t,h),r(h,i),m.m(i,null),r(h,D),r(h,b),r(b,I),C||(G=[z(n,"click",s[9]),z(u,"click",s[10]),z(i,"click",s[6]),z(b,"click",s[5])],C=!0)},p(l,[o]){o&8&&d!==(d=l[8](l[3])+"")&&X(f,d),o&2&&p!==(p=q(`button button-white ${l[1]==="white"?"selected":""}`)+" svelte-pu3rke")&&k(n,"class",p),o&1&&c!==(c=!l[0])&&(n.disabled=c),o&4&&g!==(g=l[8](l[2])+"")&&X(E,g),o&2&&v!==(v=q(`button button-black ${l[1]==="black"?"selected":""}`)+" svelte-pu3rke")&&k(u,"class",v),V!==(V=H(l))&&(m.d(1),m=V(l),m&&(m.c(),m.m(i,null))),o&1&&a!==(a=!l[0])&&(i.disabled=a),o&1&&S!==(S=!l[0])&&(b.disabled=S)},i:W,o:W,d(l){l&&_(t),m.d(),C=!1,Z(G)}}}const A=6e5;function oe(s,t,e){let n=!1,d="",f=A,p=A,c;const T=()=>{clearInterval(c),e(4,c=0)},u=()=>{T(),e(2,f=A),e(3,p=A),e(0,n=!1)},g=()=>{c?T():E()},E=()=>{T(),e(4,c=setInterval(()=>{d==="white"?e(3,p-=100):d==="black"&&e(2,f-=100),(f<=0||p<=0)&&u()},100))},v=(a="")=>{e(1,d=a),e(0,n=!0),c||E()};return[n,d,f,p,c,u,g,v,a=>{const b=a%1e3/100;a=Math.floor(a/1e3);const I=a%60;return`${Math.floor(a/60)}m:${I}.${b}s`},()=>v("black"),()=>v("white")]}class ue extends ${constructor(t){super(),x(this,t,oe,ne,Y,{})}}export{ue as component,ce as universal};

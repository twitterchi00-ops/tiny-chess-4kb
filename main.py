import json as j,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
V=[0,100,320,330,500,900,0]
ND=[-33,-31,-18,-14,14,18,31,33]
BD=[-17,-15,15,17]
RD=[-16,-1,1,16]
AD=BD+RD
Z=1e5;C=[0];X=Exception;Y={0:2,7:1,112:8,119:4};T={};L=[[0,0]]*64
J=lambda f,t,r:[(f,t,q)for q in((5,4,3,2)if(t>>4)==r else(0,))]
def p(a,b):return j.load(u.urlopen(U+a,j.dumps(b).encode()))
def P(f):
 w=f.split();b=[0]*128;i=0
 for c in w[0]:
  if c=='/':continue
  elif c.isdigit():i+=int(c)
  else:b[(7-i//8)*16+i%8]=('PNBRQK'.index(c.upper())+1)*(c.isupper()*2-1);i+=1
 s=w[1]!='w'
 c=sum(1<<'KQkq'.index(k)for k in w[2]if k!='-')
 e=-1 if w[3]=='-'else R(w[3])
 return b,s,c,e
def A(b,s,q):
 o=1-2*q
 for W,n in(((-15*o,-17*o),1),(ND,2),(AD,6)):
  for d in W:
   t=s+d
   if not t&136 and b[t]==n*o:return 1
 for d in AD:
  t=s+d
  while not t&136:
   v=b[t]
   if v:
    if v==(3 if d in BD else 4)*o or v==5*o:return 1
    break
   t+=d
 return 0
def G(b,s,c,e,l=1):
 m=[];g=1-2*s;d=16*g;r0=1+5*s;r1=7-7*s
 for f,v in enumerate(b):
  if not v or v*g<0:continue
  a=abs(v)
  if a==1:
   t=f+d
   if not t&136 and b[t]==0:
    m+=J(f,t,r1)
    if(f>>4)==r0 and b[f+2*d]==0:m.append((f,f+2*d,0))
   for x in(d-1,d+1):
    t=f+x
    if not t&136 and(b[t]*g<0 or t==e):
     m+=J(f,t,r1)
  else:
   for x in(ND,BD,RD,AD,AD)[a-2]:
    t=f+x
    while not t&136:
     if b[t]:
      if b[t]*g<0:m.append((f,t,0))
      break
     m.append((f,t,0))
     if a in(2,6):break
     t+=x
 k=4+112*s
 if b[k]==6-12*s:
  for d in(2,-2):
   j=k+d
   if c&((1+(d<0))<<2*s) and not b[k+d//2]and not b[j]and(d>0 or not b[j-1])and b[k+7*d//4]==4-8*s and all(not A(b,k+i*d//2,1-s)for i in range(3)):m.append((k,j,0))
 return[x for x in m if not A((n:=M(b,s,c,e,x)[0]),n.index(6-12*s),1-s)]if l else m
def M(b,s,c,e,m):
 f,t,q=m;n=b[:];v=n[f];n[f]=0;o=c;w=-1
 if abs(v)==1 and t==e:n[t+32*s-16]=0
 if abs(v)==1 and abs(t-f)==32:w=(f+t)//2
 if abs(v)==6:
  if abs(t-f)==2:n[f+(t-f)//2]=n[f+3-7*(f>t)];n[f+3-7*(f>t)]=0
  o&=~[3,12][s]
 o&=~(Y.get(f,0)|Y.get(t,0))
 n[t]=q*(1-2*s)if q else v
 return n,1-s,o,w
def E(b,s):
 w=0
 for i,v in enumerate(b):
  if v:
   a=abs(v);f=i&7;r=i>>4;g=(v>0)*2-1;w+=g*V[a];d=r if v>0 else 7-r;z=abs(f-3)+abs(r-3)
   if a==1:w+=g*4*d
   elif a<4:w+=g*(16-3*z)
   elif a==6:w+=g*(20 if i%112 in(2,6)else-10*d)
 w+=30*((b.count(3)==2)-(b.count(-3)==2))
 return w*(1-2*s)
def O(b,m):return V[abs(b[m[0]])]-10*V[abs(b[m[1]])]-180*m[2]
def Q(b,s,c,e,al,be,pl):
 C[0]+=1
 if C[0]>4e4:raise X
 if A(b,b.index(6-12*s),1-s):
  m=G(b,s,c,e)
  if not m:return-Z+pl
 else:
  t=E(b,s)
  if t>=be:return be
  if t>al:al=t
  m=[x for x in G(b,s,c,e,0)if(b[x[1]]or x[2]or x[1]==e)and not A((n:=M(b,s,c,e,x)[0]),n.index(6-12*s),1-s)]
 m.sort(key=lambda m:O(b,m))
 for x in m:
  n,a,o,w=M(b,s,c,e,x)
  y=-Q(n,a,o,w,-be,-al,pl+1)
  if y>=be:return be
  if y>al:al=y
 return al
def S(b,s,c,e,d,al,be,pl):
 C[0]+=1
 if C[0]>4e4:raise X
 if d<=0:return Q(b,s,c,e,al,be,pl)
 al=max(al,-Z+pl);be=min(be,Z-pl)
 if al>=be:return al
 k=(tuple(b),s,c,e);t=T.get(k);K=b.index(6-12*s)
 m=G(b,s,c,e)
 if not m:return-Z+pl if A(b,K,1-s)else 0
 if d>2 and E(b,s)>=be and not A(b,K,1-s)and-S(b,1-s,c,-1,d-3,-be,1-be,pl+1)>=be:return be
 m.sort(key=lambda x:O(b,x)-(x in L[pl])*999-(x==t)*1e5)
 bm=None
 for x in m:
  n,a,o,w=M(b,s,c,e,x)
  y=-S(n,a,o,w,d-1,-be,-al,pl+1)
  if y>al:al=y;bm=x
  if al>=be:
   if not b[x[1]]:L[pl]=[x,L[pl][0]]
   break
 T[k]=bm or m[0]
 return al
def H(b,s,c,e,lm):
 C[0]=0;T.clear();bm=lm[0];d=1
 while 1:
  try:
   lm.sort(key=lambda x:(x!=bm,O(b,x)))
   bv=-Z;bb=None
   for x in lm:
    n,a,o,w=M(b,s,c,e,x)
    y=-S(n,a,o,w,d-1,-Z,Z,1)
    if y>bv:bv=y;bb=x
   bm=bb;d+=1
   if bv>Z-1000:break
  except X:break
 f,t,q=bm
 return f"{K[f&7]}{(f>>4)+1}{K[t&7]}{(t>>4)+1}{'nbrq'[q-2]if q else''}"
K="abcdefgh";R=lambda u:16*ord(u[1])+ord(u[0])-881
while(g:=p("/game",{}))["status"]!="done":
 while g["status"]=="your_move":
  b,s,c,e=P(g["fen"])
  g=p("/move",{"game":g["game"],"move":H(b,s,c,e,[(R(u),R(u[2:]),"nbrq".index(u[4])+2 if u[4:] else 0)for u in g["legal_moves"]])})

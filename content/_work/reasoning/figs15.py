from engines import *
from engines import _points, _on_seg
from fractions import Fraction as Fr
import itertools
def sq(a,b,c,d): return PL((a,b),(c,b),(c,d),(a,d),(a,b))
def tris(segs):
    ms = maximal_segments(segs); pts = sorted(_points(ms))
    on = {q: {i for i, s in enumerate(ms) if _on_seg(q, s)} for q in pts}
    out=[]
    for a,b,c in itertools.combinations(pts,3):
        ar=abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2
        if ar==0: continue
        if on[a]&on[b] and on[b]&on[c] and on[a]&on[c]: out.append((ar,(a,b,c)))
    return out
def by_area(segs):
    d={}
    for ar,_ in tris(segs): d[ar]=d.get(ar,0)+1
    return sorted((float(k),v) for k,v in d.items())
tri=PL((4,0),(0,6),(8,6),(4,0))
def cev(k,h):
    s=list(tri)
    for i in range(1,k+1): s.append(((4,0),(Fr(8*i,k+1),6)))
    for j in range(1,h+1):
        y=Fr(6*j,h+1); x=Fr(4*(6-y),6)  # left edge x at height y... left edge from (4,0) to (0,6): x=4-4y/6
        xl=4-Fr(4,6)*y; xr=4+Fr(4,6)*y
        s.append(((xl,y),(xr,y)))
    return s
FIG=dict(
 sqdiag=sq(0,0,4,4)+[((0,0),(4,4)),((4,0),(0,4))],
 union=sq(0,0,4,4)+[((0,0),(4,4)),((4,0),(0,4)),((2,0),(2,4)),((0,2),(4,2))],
 mid=tri+PL((2,3),(6,3),(4,6),(2,3)),
 rect2diag=sq(0,0,8,4)+[((4,0),(4,4)),((0,0),(4,4)),((4,0),(0,4)),((4,0),(8,4)),((8,0),(4,4))],
 sq_inner_d=sq(0,0,4,4)+PL((2,0),(4,2),(2,4),(0,2),(2,0))+[((0,0),(4,4)),((4,0),(0,4))],
 grid22diag=sq(0,0,4,4)+[((2,0),(2,4)),((0,2),(4,2)),((0,0),(2,2)),((2,0),(4,2)),((0,2),(2,4)),((2,2),(4,4))],
 kite=PL((3,0),(6,3),(3,8),(0,3),(3,0))+[((3,0),(3,8)),((0,3),(6,3))],
 env=sq(0,2,6,6)+PL((0,2),(3,0),(6,2))+[((0,2),(6,6)),((6,2),(0,6))],
 tri_mid_diag=PL((0,6),(8,6),(4,0),(0,6))+[((4,6),(4,0))]+PL((2,3),(4,6),(6,3)),
)
def grid(m,n):
    return [((i,0),(i,n)) for i in range(m+1)]+[((0,j),(m,j)) for j in range(n+1)]

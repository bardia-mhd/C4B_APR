isa,isb,isc = map(int, input().split())
na,nb,nc = map(int, input().split())
fa = isa-na
fb = isb-nb
fc = isc-nc
fa = max(fa,0)
fb = max(fb,0)
fc = max(fc,0)
fa = fa // 2
fb = fb // 2
fc = fc // 2
canmake = fa+fb+fc

pa = na-isa
pb = nb-isb
pc = nc-isc

pa = max(0, pa)
pb = max(0, pb)
pc = max(0, pc)

needmake = pa+pb+pc
if(needmake <= canmake):
    print("Yes")
else:
    print("No")
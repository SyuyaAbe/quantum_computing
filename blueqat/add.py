#coding:utf-8
from blueqat import Circuit

#加算の量子回路
#2つのCNOTゲートとトフォリゲートの配置
x = Circuit().h[0,1].cx[0,2].cx[1,2].ccx[0,1,3].m[:].run(shots=1)
print(x)


#試行回数を1000にする
y = Circuit().h[0,1].cx[0,2].cx[1,2].ccx[0,1,3].m[:].run(shots=1000)

print(y)
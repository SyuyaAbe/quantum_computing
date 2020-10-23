#coding:utf-8
from blueqat import Circuit

#2つの量子ビットの情報を縺れさせると、片方が0の場合にいは必ずもう一方も0になる。逆も然り。
#cx[0,1]がCNOTゲートに相当し、00及び11の測定回数を出力
x = Circuit().h[0].cx[0,1].m[:].run(shots=1000)
#cx[0,1]ではコントロールビットが0、ターゲットビットが1である。

print(x)
#coding:utf-8
from blueqat import Circuit

#0番目の量子ビットに対してHadamard gateを配置
a = Circuit().h[0].m[:].run(shots=100)

#0番目の量子ビットに対してHadamard gateを配置
#この時、Hadamard gateを配置してない量子ビット0も出現する
b = Circuit().h[1].m[:].run(shots=100)

#0番目と1番目の量子ビットに対してHadamard gateを配置
#試行回数100の中で、00, 01, 10, 11の測定回数をそれぞれ求める
c = Circuit().h[0,1].m[:].run(shots=100)

print(a)
print(b)
print(c)
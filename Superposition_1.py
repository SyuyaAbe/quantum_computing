#coding:utf-8
from blueqat import Circuit

#量子重ね合わせ。Hadamard gateを配置して、0と1が50％ずつの確率で測定を行う
x = Circuit().h[0].m[:].run(shots=100)
print(x)
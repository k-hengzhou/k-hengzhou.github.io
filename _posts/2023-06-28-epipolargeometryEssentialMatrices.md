---
layout: post
title: "本质矩阵和基础矩阵"
categories: 视图几何
description: "对极几何基本原理"
keywords: 对极几何 本质矩阵 基础矩阵 
---

本文先通过特征点匹配关系给出本质矩阵和基础矩阵的定义，并完整的推到如何求解本质矩阵和基础矩阵，最后给出通过这两个矩阵还原旋转矩阵和位移向量的数学原理

## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则

$$
d_{x2}x_2=Rx_1+td_{x1}
$$

等式两边同时$t$叉乘两边得

$$
t \times d_{x2}x_2=t \times Rx_1+d_{x1}t \times t
$$

整理可得

$$
d_{x2}t\times x_2=t \times Rx_1
$$

在等式两边同时点成上$x_2^T$
可得
$$0=x_2^T t \times Rx_1$$
取

$$
E= t \times R
$$

假设$p_1 p_2$为像素坐标，同理可得

$$
0=p_2^t K^{-T}t \times R K^{-1}p_1
$$

取

$$
F=K^{-T}t \times R K^{-1}
$$

即

$$
F=K^{-T}EK^{-1}
$$

### 求解$F$和$E$

已知足够的配对点$x_1$ $x_2$。
由 

$$
p_1^TFp_2=0
$$

将F展开为列向量整理可以得

$$
AF=0
$$

由SVD求解得到$A^TA$的最小特征值就是F，通常取4组点对求解$F$,也就是经典的八点法。

### 由F回复R和t

$$
\begin{eqnarray*}
   F=K^{-1}EK\\
   E=t \times R
\end{eqnarray*}
$$

令$T$为$t$对应的反对称矩阵
则有

$$
\begin{equation}
   E=TR
\end{equation}
$$

对E进行SVD分解得到

$$ 
U \Sigma V^T=TR
$$

等式两边同时乘上自身的转置

$$
T*T^T=U(-I\cdot \Sigma^2)U^T
$$

其中$I$为单位矩阵，可知$-I=R_z(\frac{\pi}{2})\cdot R_z(\frac{\pi}{2})$或$-I=R_z(-\frac{\pi}{2})\cdot R_z(-\frac{\pi}{2})$
所以

$$
T*T^T=(U(R_z(\frac{\pi}{2})\Sigma U^T)(U(R_z(\frac{\pi}{2})\Sigma U^T)^T
$$

或者

$$
T*T^T=(U(R_z(-\frac{\pi}{2})\Sigma U^T)(U(R_z(-\frac{\pi}{2})\Sigma U^T)^T
$$

可得

$$
\begin{cases}
   T=\pm UR_z(\frac{\pi}{2})\Sigma U^T\\
   T=\pm UR_z(-\frac{\pi}{2}\Sigma U^T
\end{cases}
$$

将$T$代入公式\ref{for1},可得$R$,$t$的解为

$$\begin{cases}
   T= UR_z(\frac{\pi}{2})\Sigma U^T \,\,\,\, R=UR_z^T(\frac{\pi}{2})\Sigma V^T \\
   T= -UR_z(\frac{\pi}{2})\Sigma U^T \,\,\,\, R=-UR_z^T(\frac{\pi}{2})\Sigma V^T \\
   T= UR_z(-\frac{\pi}{2})\Sigma U^T \,\,\,\, R=UR_z^T(-\frac{\pi}{2})\Sigma V^T \\
   T= -UR_z(-\frac{\pi}{2})\Sigma U^T \,\,\,\, R=-UR_z^T(-\frac{\pi}{2})\Sigma V^T \\
\end{cases}$$

所以可从$E$中求解出的解$R$,$t$。实际计算时，可以最多特征点通过$R$ $t$之后有正的深度值。


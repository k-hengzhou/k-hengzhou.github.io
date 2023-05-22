---
layout: post
title: "对极几何"
categories: vo
description: "对极几何基本原理"
keywords: vo, vslam, Essential Matrix Homography
---

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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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
$$## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$
## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$

简写成

$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得
## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$

简写成

$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素
## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
等式两边同时$t$叉乘两边得
联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解tUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解
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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$## 本质矩阵 
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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
$$## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$
## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$

简写成

$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得
## 本质矩阵 
### $E$的定义

令$x_1$和$x_2$为空间点在两个不同相机坐标系下的归一化坐标，$R$，$t$为相机之间的刚体运动，则
$$d_{x2}x_2=Rx_1+td_{x1}$$
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$

简写成

$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解tUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解
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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$

简写成

$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解
$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解
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

$$\begin{eqnarray*}
   &&F=K^{-1}EK\\
   &&E=t \times R
\end{eqnarray*}$$

令$T$为$t$对应的反对称矩阵
则有

$$\begin{equation}\label{for1}
   E=TR
\end{equation}$$

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

## 单应矩阵

### 计算H

假设所有配对点的空间坐标落在同一平面上,取平面P的方程为

$$
ax+by+cz+d=0
$$

简写成

$$
n^tX+d=0
$$

其中$n=(a,b,c),x=(x,y,z)$
由假设特征点落在平面P上，即

$$
n^tx/d=-1
$$

假设$x_1$和$x_2$为空间点在两个相机坐标系下的坐标，$R$ $t$是相机之间的相对运动

$$
d_{x_2}x_2=Rx_1+td_{x_1}
$$

令

$$
d_{x_2}x_2=Rx_1-d_{x_1}tn^tx_1/d
$$

整理可得

$$
d_{x_2}x_2=d_{x_1}(R-tn^t/d)x_1
$$

等式两边都叉乘$x_2$可得

$$
0=x_2\times (R-tn^t/d)x_1
$$

令$A=Rd+tn^t$,且$H=K(R-tn^t/d)K^{-1}$

### 恢复R、t
取

$$
A=Rd+tn^t
$$

对A进行SVD分解得

$$ 
V \Sigma U=Rd+tn^t
$$

整理得

$$
\Sigma=R_1d_1+t_1n_1^t
$$

其中$R=SUR_1V^t t=Ut_1 n=vn_1 d=sd_1 s=detUdetV$
取一直基 $e_1 e_2 e_3$则

$$
n=x_1e_1+x_2e_2+x_3e_3
$$

带入原式可得

$$
d^{'}_ie_i=d_1R_1e_i+t_1x_i 
$$ 

i=1,2,3,$d^{'}_i$是$\Sigma$的对角元素

$$
d^{'}_i=d_1R_1e_i+t_1x_i 
$$

联立三个公司消掉t可得

$$
d_1R_1(x_je_i-x_ie_j)=d^{'}_ix_je_i-d^{'}_jx_ie_j
$$

因为$R_1$不改变向量的长度，所以

$$ 
\begin{cases}
(d_1^2-d^{'^2}_2)x_1^2+(d_1^2-d^{'^2}_1)x_2^2=0  \\
(d_1^2-d^{'^3}_2)x_2^2+(d_1^2-d^{'^2}_2)x_3^2=0 \\
(d_1^2-d^{'^2}_1)x_3^2+(d_1^2-d^{'^2}_3)x_1^2=0
\end{cases}
$$

因为上诉方程一定有非零解，所有对应的行列式一定为零，即

$$
(d_1^2-d^{'^2}_2)(d_1^2-d^{'^3}_2)(d_1^2-d^{'^2}_1)=0
$$

至此可以求的$d_1$ 进而求解出$R$和$t$
这部分可以参看文论《Motion and Structure from Motion in a Piecewise Planar Environment》

## 三角化

已知匹配特征点对在各种摄像头下的归一化坐标为$x$ $x'$ 各自到世界坐标系的转换矩阵为$T_{fw}$ $T_{fw}^{'}$, X为$x$ $x'$对应的世界
坐标系的三维坐标。
相机坐标系下归一化x满足

$$
x=\frac{1}{X(3)}T_{fw}X
$$

所以

$$
x\times TX=0
$$

连立两个等式就可以得到$X$的解
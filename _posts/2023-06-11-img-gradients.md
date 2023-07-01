---
layout: post
title: "灰度图像导数计算"
categories: cv
description: "灰度图像导数计算"
keywords:  雅可比 导数
---


下文介绍各种离散近视之间的差别，并通过对比说明为什么采用现有的灰度梯度计算方式。

## 导数离散近视

对于函数$f(x)$,计算泰勒展开

$$
f(x+h)=f(x)+f^{'}h+\frac{1}{2}f^{''}h^2+O(h^3)
$$

所以

$$
\begin{eqnarray*}
   && f(x+h)-f(x)+f^{'}h+\frac{1}{2}f^{''}h^2+O(h^3)\\
   \implies&&  \frac{f(x+h)-f(x)}{h}=f^{'}+O(h)
\end{eqnarray*}
$$

同理

$$
f(x-h)=f(x)-f^{'}h+\frac{1}{2}f^{''}h^2+O(h^3)
$$

所以

$$
\frac{f(x)-f(x-h)}{h}=f^{'}+O(h)
$$

将$f(x+h)$减去$f(x-h)$可得

$$
\begin{eqnarray*}
   && f(x+h)-f(x-h)=2f^{'}h+O(h^3)\\
   \implies&&  \frac{f(x+h)-f(x-h)}{2h}=f^{'}+O(h^2)
\end{eqnarray*}
$$

可知最后一种近似方法比前两种更精确

## 灰度梯度
令$I$为一张2D灰度图像，$I(X)=I(x,y)$为图像在点$X=(x,y)$处的灰度值。因为$I(X)$为离散函数。为了计算$I(X)$在点$X$处的导数，
需要对导数采用离散近似模型,所以对于灰度函数$I(X)$,灰度导数计算如下

$$\begin{eqnarray*}
  & \frac{\partial (I)}{\partial (X)}=\left[\begin{matrix}
      I_x(X),I_y(X)
   \end{matrix}\right] \\
  & I_x(x,y)=0.5*(I(x+1,y)-I(x-1,y)) \\
  & I_y(x,y)=0.5*(I(x,y+1)-I(x,y-1))
\end{eqnarray*}$$




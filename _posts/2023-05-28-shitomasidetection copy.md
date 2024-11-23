---
layout: post
title: "shi-tomasi 特征点"
categories: cv
description: "vslam 中常见的shi-tomasi 特征点介绍"
keywords:  shi-tomasi harri svo_slam
---

本文推到shi-tomasi角点的计算原理，给出harri判断的条件，并说明svo slam 的特征提取方法

## shi-tomasi 

对于图像的灰度函数为$I(x,y)$,对于图像中的一点$(x,y)$,$B(x,y)$为已该点为中心的一个方形像素块。
当$B(x,y)$ 沿向量 $(u,v)$移动，对于$B(x,y)$中每一个点$(x_i,y_i)$引起的像素变化为

$$
\begin{equation*}
    e(x_i,y_i)=[I(x_i+u,y_i+v)-I(x_i,y_i)]
\end{equation*}
$$

取每一个的均方

$$\begin{equation}\label{equ1}
   E_{uv}(x,y)=\sum_{(x_i,y_i)\in B(x_i,y_i)}[I(x_i+u,y_i+v)-I(x_i,y_i)]^2
\end{equation}$$

如果$(x,y)$是一个角点，则$E_{uv}(x,y)$应该非常大，所以我们假设当$E_{uv}(x,y)>R$时$(x,y)$是一个
角点，其中$R$为一个给定的阈值。

为了方便计算$E_{uv}(x,y)>R$,我们把$I(x_i+u,y_i+v)$按一阶泰勒展开得到

$$
I(x_i+u,y_i+v)\approx I(x_i,y_i)+uI_x(x_i,y_i)+vI_y(x_i,y_i)
$$

将上式代入公式$\ref{equ1}$,得到

$$\begin{eqnarray*}
   E_{uv}(x,y)&&=\sum_{(x_i,y_i)\in B(x_i,y_i)}(uI_x(x_i,y_i)+vI_y(x_i,y_i))^2 \\
              &&=u^2\sum_{(x_i,y_i)\in B(x_i,y_i)}I_x(x_i,y_i)^2+
                 2uv\sum_{(x_i,y_i)\in B(x_i,y_i)}I_x(x_i,y_i)I_y(x_i,y_i)+
                 v^2\sum_{(x_i,y_i)\in B(x_i,y_i)}I_y(x_i,y_i)^2\\
               &&=[u,v]\left[\begin{matrix}
                  \sum_{(x_i,y_i)\in B(x_i,y_i)}I_x(x_i,y_i)^2 && \sum_{(x_i,y_i)\in B(x_i,y_i)}I_x(x_i,y_i)I_y(x_i,y_i) \\
                  \sum_{(x_i,y_i)\in B(x_i,y_i)}I_x(x_i,y_i)I_y(x_i,y_i)         && \sum_{(x_i,y_i)\in B(x_i,y_i)}I_y(x_i,y_i)^2
                        \end{matrix}\right]\left[\begin{matrix}
                          u\\
                           v
                        \end{matrix}\right]\\
               &&\triangleq [u,v]\left[\begin{matrix}
                 I_{xx} &&  I_{xy} \\
                 I_{xy}&& I_{yy}
                        \end{matrix}\right]\left[\begin{matrix}
                          u\\
                           v
                        \end{matrix}\right]\\
               &&\triangleq [u,v]M
                  \left[\begin{matrix}
                        u\\
                        v
                  \end{matrix}\right]
\end{eqnarray*}$$

将$M$化简为$M=R^{T}\left[
   \begin{matrix}
      \lambda_1 && 0\\
      0,&&\lambda_2
   \end{matrix}
\right] R
$ 代入上式可得

$$\begin{eqnarray*}
   E_{uv}(x,y)=&& [u,v]R^{T}\left[
   \begin{matrix}
      \lambda_1 && 0\\
      0,&&\lambda_2
   \end{matrix}
\right] R
\left[\begin{matrix}
      u\\
      v
\end{matrix}\right]\\
&&=[u^{'},v^{'}]\left[
   \begin{matrix}
      \lambda_1 && 0\\
      0,&&\lambda_2
   \end{matrix}
\right] 
\left[\begin{matrix}
      u^{'}\\
      v^{'}
\end{matrix}\right] \\
&&=\lambda_1*{u^{'}}^2+\lambda_2*{v^{'}}^2
\end{eqnarray*}$$

取$\lambda_{\min}=\min\{\lambda_1,\lambda_2\}$,
所以$E_{uv}(x,y)>R \implies \lambda_{\min}>R^{'}$

### harri 判断

取$R=\det{M}-k*(trace(M))$,按$R$的值分为三种情况

- $R$很大，则为角点
- $\|R\|$很小，则为平面
- $R$为负，且$\|R\|$很大，则为边缘


### 窗函数
为了给邻域内不同的点赋予不同的权重可以在优化函数中添加窗函数

$$\begin{equation}
   E_{uv}(x,y)=\sum_{(x_i,y_i)\in B(x_i,y_i)}w(x,y)[I(x_i+u,y_i+v)-I(x_i,y_i)]^2
\end{equation}$$



## svo特征值提取

- 将图像划分为面积相等的小方格
- 提取fast角点，并计算角点得分和最小值抑制
- 计算fast角点的shi-tamasi得分，即$M$的最小特征值
- 只保留相同方格内shi-tamasi得分最大且大于fast角点得分的角点



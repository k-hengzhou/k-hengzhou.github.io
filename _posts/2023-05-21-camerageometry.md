---
layout: post
title: "针孔和鱼眼模型下的摄像机几何"
categories: 视图几何
description: "针孔和鱼眼模型下的摄像机几何"
keywords: 鱼眼模型 针孔模型 相机内参
notebook: true
---

<style>
  .notebook {
    position: relative;
    background-color: #fdfcf8;
    background-image:
      linear-gradient(rgba(120, 120, 120, 0.08) 1px, transparent 1px),
      linear-gradient(90deg, rgba(120, 120, 120, 0.08) 1px, transparent 1px);
    background-size: 24px 24px;
    background-position: -1px -1px;
    border-radius: 0.5rem;
    padding: 1.5rem 2rem;
    box-shadow: inset 0 0 0 1px rgba(120, 120, 120, 0.1);
  }
  .notebook::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 3.5rem;
    width: 1px;
    background: rgba(220, 80, 80, 0.25);
  }
  .notebook > * {
    position: relative;
    z-index: 1;
  }
</style>

<div class="notebook">

> **摘要**：本文系统阐述单摄像机下的射影几何关系。首先推导针孔相机模型中空间三维坐标到成像平面坐标及像素坐标的完整转化过程；随后建立鱼眼相机与针孔相机之间的坐标映射关系；最后列举常见的畸变投影函数。

---

## 目录

- [目录](#目录)
- [1. 针孔模型](#1-针孔模型)
  - [1.1 点到平面的投影](#11-点到平面的投影)
  - [1.2 像素坐标计算](#12-像素坐标计算)
- [2. 鱼眼畸变](#2-鱼眼畸变)
  - [2.1 针孔摄像头到鱼眼镜头](#21-针孔摄像头到鱼眼镜头)
  - [2.2 鱼眼镜头到针孔摄像头](#22-鱼眼镜头到针孔摄像头)
  - [2.3 投影函数](#23-投影函数)

---

## 1. 针孔模型

### 1.1 点到平面的投影

**定义 1（中心投影）** 考虑空间点到一张平面上的中心投影。投影中心位于一个欧氏坐标系的原点，而平面 $z=f$ 被称为**图像平面**。在针孔摄像机模型下，空间坐标为 $P=(X,Y,Z)$ 的点被映射到图像平面上的点，该点是连接点投影中心的直线与图像平面的交点 $P'$，如下图所示：

<div align="center">
  <img src="/images/post/pinhole.png" width="50%" alt="pinhole"/>
</div>

**命题 1（投影变换）** 使用相似三角形可以轻松计算 $P'$ 在图像平面坐标系 $0\text{-}x\text{-}y$ 下的坐标。相机世界坐标系到图像平面坐标系的坐标转换可表示为：

$$
\begin{aligned}
    f: \mathbb{R}^3 &\rightarrow \mathbb{R}^2 \\
    \begin{pmatrix}
        x \\ y\\ z
    \end{pmatrix} &\mapsto \begin{pmatrix}
        f \dfrac{x}{z}\\ f \dfrac{y}{z}
    \end{pmatrix}
    =\frac{1}{z} \begin{bmatrix}
        f & 0 & 0 \\
        0 & f & 0
    \end{bmatrix}
    \begin{pmatrix}
        x \\ y\\ z
    \end{pmatrix}
\end{aligned}
$$

**注** 也可以使用**齐次坐标系**表示投影：

$$
\begin{aligned}
    f: \mathbb{R}^3 &\rightarrow \mathbb{R}^3 \\
    \begin{pmatrix}
        x \\ y\\ z
    \end{pmatrix} &\mapsto \begin{pmatrix}
        fx\\ fy \\ 1
    \end{pmatrix}
    = \frac{1}{z} \begin{bmatrix}
        f & 0 & 0 \\
        0 & f & 0 \\
        0 & 0 & 1
    \end{bmatrix}
    \begin{pmatrix}
        x \\ y\\ 1
    \end{pmatrix}
\end{aligned}
$$

<div align="center">
  <img src="/images/post/pinhole1.png" width="50%" alt="pinhole1"/>
</div>

### 1.2 像素坐标计算

**定义 2（像素坐标系）** 接下来计算点 $P'$ 在像素坐标系 $o'\text{-}u\text{-}v$ 下的像素坐标。首先考虑到 $0\text{-}x\text{-}y$ 与 $o'\text{-}u\text{-}v$ 的坐标系单位刻度不同，假设坐标系 $o'\text{-}u\text{-}v$ 相对 $0\text{-}x\text{-}y$ 缩放了 $(\alpha,\beta)$。若 $0\text{-}x\text{-}y$ 的单位刻度为米，则 $\alpha$ 和 $\beta$ 的单位为：像素/米。其次，坐标系 $0\text{-}x\text{-}y$ 沿着向量 $\overrightarrow{oo'}=(c_x,c_y)$ 位移到坐标系 $o'\text{-}u\text{-}v$。

**命题 2（坐标变换）** 从坐标系 $0\text{-}x\text{-}y$ 到像素坐标系 $o'\text{-}u\text{-}v$ 的完整变换为：

$$
\begin{aligned}
    h: \mathbb{R}^2 &\rightarrow \mathbb{R}^2 \\
    \begin{pmatrix}
        x \\ y
    \end{pmatrix} &\mapsto \begin{pmatrix}
        u \\ v
    \end{pmatrix}
    =\begin{pmatrix}
        \alpha \cdot x\\ \beta \cdot y
    \end{pmatrix}
    +\begin{pmatrix}
        c_x \\ c_y
    \end{pmatrix}
\end{aligned}
$$

用齐次坐标表示如下：

$$
\begin{aligned}
    h: \mathbb{R}^2 &\rightarrow \mathbb{R}^2 \\
    \begin{pmatrix}
        x \\ y \\ 1
    \end{pmatrix} &\mapsto \begin{pmatrix}
        u \\ v \\ 1
    \end{pmatrix}
    =\begin{pmatrix}
        \alpha & 0 & c_x \\
        0 & \beta & c_y \\
        0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
        x \\ y \\ 1
    \end{pmatrix}
\end{aligned}
$$

**定理 1（针孔模型完整变换）** 将 $f$ 和 $h$ 复合可以得到针孔模型相机坐标系到像素坐标系的完整变换：

$$
\begin{aligned}
    h \circ f: \mathbb{R}^3 &\rightarrow \mathbb{R}^2 \\
    \begin{pmatrix}
        x \\ y \\ z
    \end{pmatrix} &\mapsto \begin{pmatrix}
        u \\ v \\ 1
    \end{pmatrix}
    =\frac{1}{z} \begin{pmatrix}
        \alpha \cdot f & 0 & c_x \\
        0 & \beta \cdot f & c_y \\
        0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
        x \\ y \\ z
    \end{pmatrix}
\end{aligned}
$$

**定义 3（内参矩阵）** 令

$$
\begin{aligned}
    K=\begin{pmatrix}
        \alpha \cdot f & 0 & c_x \\
        0 & \beta \cdot f & c_y \\
        0 & 0 & 1
    \end{pmatrix}
    \cong
    \begin{pmatrix}
        f_x & 0 & c_x \\
        0 & f_y & c_y \\
        0 & 0 & 1
    \end{pmatrix}
\end{aligned}
$$

则 $K$ 即为相机的**内参矩阵**。

---

## 2. 鱼眼畸变

> **背景**：在使用中我们常常会在摄像机前方加上透镜来获得更好的视角范围，称为**鱼眼相机模型**。由于增加透镜会引起图形畸变。下面我们推导针孔模型到鱼眼模型（加畸变）和鱼眼模型到针孔模型（取畸变）的数学过程。

### 2.1 针孔摄像头到鱼眼镜头

<div align="center">
  <img src="/images/post/fisheye.png" width="50%" alt="fish-eye"/>
</div>

**符号约定**：坐标系 $O_c\text{-}X_cY_cZ_c$ 是相机的世界坐标系，坐标系 $O\text{-}XY$ 是相机成像平面坐标系。点 $P$ 为点在空间的位置，点 $P_0$ 为针孔模型下 $P$ 在归一化坐标系的坐标，$P'$ 为鱼眼模型下 $P$ 在归一化坐标系的坐标，$\theta$ 为 $P$ 与 $Z_c$ 的夹角（称为**视角**），$r_d$ 为 $P'$ 的模长（称为**像高**），$f$ 为焦距，后续统一默认为 $1$。

**命题 3（鱼眼像素坐标计算）** 假设 $P_0$ 的坐标为 $(x_0,y_0)$，$P'$ 的坐标为 $(X',Y')$，由图可得：

$$
\begin{aligned}
   r &= \sqrt{x_0^2 + y_0^2} \\
   \theta &= \arctan(r/f) = \arctan(r)
\end{aligned}
$$

假设相角 $\theta$ 和视高 $r_d$ 满足函数 $r_d = f_{\theta}(\theta)$。因为三角形 $\triangle OP_0X_0$ 和 $\triangle OP'X'$ 相似，可得：

$$
\frac{x_0}{x'} = \frac{r}{r_d}
$$

同理：

$$
\frac{y_0}{y'} = \frac{r}{r_d}
$$

最后假设摄像机的内参分别为 $f_x$、$f_y$、$c_x$、$c_y$，则 $P'$ 的像素坐标 $(u,v)$ 为：

$$
\begin{aligned}
   u &= f_x x' + c_x \\
   v &= f_y y' + c_y
\end{aligned}
$$

### 2.2 鱼眼镜头到针孔摄像头

**符号约定**：坐标系 $O_c\text{-}X_cY_cZ_c$ 是相机的世界坐标系，坐标系 $O\text{-}XY$ 是相机归一化坐标系。点 $P$ 为点在空间的位置，点 $P_0$ 为针孔模型下 $P$ 在归一化坐标系的坐标，$P'$ 为鱼眼模型下 $P$ 在归一化坐标系的坐标，$\theta$ 为 $P$ 与 $Z_c$ 的夹角（称为**视角**），$r_d$ 为 $P'$ 的模长（称为**像高**），$f$ 为焦距，后续统一默认为 $1$。

**命题 4（针孔像素坐标计算）** 假设 $P_0$ 的坐标为 $(x_0,y_0)$，$P'$ 的坐标为 $(x',y')$，由图可得：

$$
\begin{aligned}
   r_d = \sqrt{(x')^2 + (y')^2}
\end{aligned}
$$

假设相角 $\theta$ 和视高 $r_d$ 满足函数 $\theta = f_{r}(r_d)$，所以 $r = \tan(\theta)$。因为三角形 $\triangle OP_0X_0$ 和 $\triangle OP'x'$ 相似，可得：

$$
\frac{x_0}{x'} = \frac{r}{r_d}
$$

同理：

$$
\frac{y_0}{y'} = \frac{r}{r_d}
$$

最后假设摄像机的内参分别为 $f_x$、$f_y$、$c_x$、$c_y$，则 $P_0$ 的像素坐标 $(u,v)$ 为：

$$
\begin{aligned}
   u &= f_x x_0 + c_x \\
   v &= f_y y_0 + c_y
\end{aligned}
$$

### 2.3 投影函数

**定义 4（常见投影模型）** 下表列举了常见的畸变投影函数及其特点：

| 投影类型                              | 投影函数                                            | 特点                                         |
| :------------------------------------ | :-------------------------------------------------- | :------------------------------------------- |
| 透视投影 (perspective projection)     | $r = f_{\theta}\tan(\theta)$                        | 针孔相机模型                                 |
| 体视投影 (stereographic projection)   | $r = 2f_{\theta}\tan\left(\dfrac{\theta}{2}\right)$ | 任何直线相交的角度，在变换后保持不变         |
| 等距投影 (equidistance projection)    | $r = f_{\theta}\theta$                              | 物体成像面上距离画面中心的距离与入射角成正比 |
| 等积投影 (equisolid angle projection) | $r = 2f_{\theta}\sin\left(\dfrac{\theta}{2}\right)$ | 在变换前后，物体所占的立体角大小不变         |
| 正交投影 (orthogonal projection)      | $r = f_{\theta}\sin(\theta)$                        | 投影畸变最大，而且最大视场角不能大于 $180°$  |

---

> **总结**：本文从针孔相机模型出发，推导了空间点到图像平面及像素坐标的完整变换过程，建立了内参矩阵 $K$ 的概念；随后在鱼眼畸变框架下，分别推导了针孔模型到鱼眼模型（加畸变）和鱼眼模型到针孔模型（取畸变）的坐标映射关系；最后总结了五种常见的投影函数模型及其几何特性。

</div>

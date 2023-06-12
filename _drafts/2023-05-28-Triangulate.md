---
layout: fragment
title: 三角化
tags: [vo]
description: vo 中三角化
keywords: vo, vslam, Triangulate
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---


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
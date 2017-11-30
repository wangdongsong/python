# SciPy积分


## 给定函数对象的积分函数

* quad 通用积分
* dblquad 通用二重积分
* tplquad 通用三重积分
* nquad 通用N重积分
* fixed_quad 对func(x)做N维高斯积分
* quadrature 在给定容限范围内的高斯积分
* romberg 对函数做Romberg积分

## 固定样本给定时的积分函数

* cumtrapz 用梯形积分法计算积分
* simps 用辛氏法则从样本中计算积分
* romb 用Romberg积分法从（2**k + 1）个均匀间隔的样本中计算积分

### 常微分函数方程中的积分函数

* odeint 差分方程的通用积分
* ode 用VODE和ZVODE的方式进行
* complex_ode 将复数值的ODE转化成实数并积分
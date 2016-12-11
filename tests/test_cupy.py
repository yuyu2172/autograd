from __future__ import absolute_import
import warnings

import cupy as cp
import autograd.cupy as cp
import autograd.numpy as np
import autograd.numpy.random as npr
from autograd import grad
npr.seed(1)


def mul(x):
    return 2 * x

np.add

grad_mul = grad(mul)
print grad_mul(cp.array(1.0))


import numpy as np

# 新的导入
from scipy.ndimage import gaussian_filter
from scipy import misc


# 修改
# __all__ = ['rand_array']
# __all__ = ['rand_array', 'smooth_image']
__all__ = ['rand_array', 'smooth_image', 'my_mat_solve']


def rand_array(shape):
    return np.random.rand(*shape)


# 添加的功能
def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)


# 添加的功能2
def my_mat_solve(A, b):
    return A.inv()*b
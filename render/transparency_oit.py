"""第 53 批：玻璃、烟雾和粒子叠在一起时顺序错、边缘发灰、折射..."""

def depth_weight(depth, thickness):
    """返回与深度和厚度相关的混合权重。"""
    raise NotImplementedError("TODO: depth_weight")

def depth_test(enabled):
    """返回是否启用透明物体深度测试。"""
    raise NotImplementedError("TODO: depth_test")

def combine_transmission(reflection, transmission):
    """合并透射与反射贡献。"""
    raise NotImplementedError("TODO: combine_transmission")

def particle_order(depths):
    """按深度返回粒子从远到近的顺序。"""
    raise NotImplementedError("TODO: particle_order")

def store_rgba_depth(rgba, depth):
    """同时存储颜色与深度。"""
    raise NotImplementedError("TODO: store_rgba_depth")

def resolve_msaa(samples):
    """对多样本颜色做解析平均。"""
    raise NotImplementedError("TODO: resolve_msaa")

def capture_frame(current, previous):
    """返回折射抓屏使用的当前帧。"""
    raise NotImplementedError("TODO: capture_frame")

def normalize_weights(weights):
    """归一化透明度混合权重。"""
    raise NotImplementedError("TODO: normalize_weights")

def stereo_buffer(view_id):
    """按眼别返回独立透明缓冲。"""
    raise NotImplementedError("TODO: stereo_buffer")

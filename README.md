# pairwise-transparency-oit

玻璃、烟雾和粒子叠在一起时顺序错、边缘发灰、折射翻转：加权混合用固定权重；深度测试写死；半透明和折射分两个 pass；粒子按发射顺序；OIT 缓冲只存颜色不存深度；Alpha 排序按对象中心；MSAA 下解析用单采样；折射抓屏用上一帧；透明物体互相遮挡时权重归一错；VR 双眼共用缓冲。render/transparency_oit.py 是核心，tests/test_transparency_oit.py 15个红。要修的是：深度相关权重；深度测试可配；透射折反射合并；粒子深度排序；颜色深度双存；逐像素排序；MSAA 解析；当前帧抓屏；权重归一；双眼独立。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。

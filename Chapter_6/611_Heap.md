### 堆的介绍

堆类似于一个完全二叉树。

最大堆和最小堆：
- 最大堆：所有子节点的值小于父节点的值
- 最小堆：所有父节点的值大于父节点的值

堆可以用一个数组来表示，其中节点的快速找寻父节点和子节点的方法为：

```
left_child_index = 2 * parent_index
right_child_index = 2 * parent_index + 1
parent_index = int(current_node_index / 2)
```


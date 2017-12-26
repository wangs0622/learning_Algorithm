此文件夹中存放着排序相关的代码，具体的内容请关注我的公众号，点击 **历史消息** 进行查看

- `__init__.py` 中写有几个函数

- `primarySort.py` 中介绍了四种初级排序算法的 python 实现，分别是: **选择排序**， **插入排序**， **冒泡排序** 以及 **希尔排序**

| 函数或者类 名 | 函数或者类作用 |
|-------| --------|
| selectionSort() | 选择排序 |
| insertionSort() | 插入排序 |
| bubbleSort() | 冒泡排序 |
| shellSort() | 希尔排序 |
| Date() | 定义日期类 |

- `mergeSort.py` 介绍归并排序

| 函数名 | 函数作用 |
|-------| --------|
| merge() | 用于实现归并操作 |
| mergeSort() | 归并排序 |
| main_mergeSort_Vs_shellSort() | 对比归并排序与希尔排序|
| mergeSortBU() | 自底向上的归并排序 |
| mergeSortWithPrimary() | 改进方法1 的归并排序 |
| mergeSortWithPrimaryAndJudge() | 改进方法1+2 的归并排序 |

------

- `maxPQ.py` 介绍优先队列以及堆操作，此文件的运行环境为 python 3.6.4

具体内容参见： [http://www.wangs0622.com/2017/12/26/PrivorityQueueAndHeap/](http://www.wangs0622.com/2017/12/26/PrivorityQueueAndHeap/)

| 函数名 | 函数作用 |
|-------| --------|
| class MaxPQ() | 创建无序 deque 的优先队列 |
| class MaxPQbasedHeap() | 创建基于堆操作的优先队列 |
| swim() | 实现堆操作的上浮操作 |
| sink() | 实现堆操作的下沉操作 |
| printHeap() | 以可视化的方式显示堆中的数据 |

------

- `PQ.py` 介绍基于 Python 内置优先队列类与内置的堆操作函数而改进后优先队列，此文件的运行环境为 python 3.6.4

Python 自带的优先队列应该算的上是 MinPQ 类，即堆中最小元素位于首位，且从第零个元素开始存储数据。

在此文件中，我们基于 Python 自带的优先队列，定义了一个 MaxPQ 类，即最大元素位于首部，从零位开始存储数据。

具体内容参见： [http://www.wangs0622.com/2017/12/26/PrivorityQueueAndHeap/](http://www.wangs0622.com/2017/12/26/PrivorityQueueAndHeap/)

| 函数/类 名 | 函数作用 |
|-------| --------|
| class MinPQ() | Python 内置的优先队列 |
| class MaxPQ() | 基于内置优先队列改变后的优先队列 |
| heapush(heap, item) | 将元素 item 添加到 heap 这个堆结构中 |
| heappop(heap) | 获取 heap 这个堆结构中最大的元素 |
| _siftdown(heap, startpos, pos) | 将位于 pos 位，一般是末尾，的元素进行下沉操作 |
| _siftup(heap, pos) | 将位于 pos 位，一般是第零位，的元素进行上浮操作 |



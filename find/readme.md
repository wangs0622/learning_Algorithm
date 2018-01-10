此文件夹中存放关于查找的代码，具体的代码内容的解释清查看 

[http://www.wangs0622.com/2018/01/10/using-python-to-study-algotithm-symbol-table/](http://www.wangs0622.com/2018/01/10/using-python-to-study-algotithm-symbol-table/)

# **`ST.py`** 有序符号表

## 基于链表的无序符号表  class ST(Link): 

| 类方法名 | 类方法的作用 |
|---|---|
| \_\_init\_\_() | 构建符号表，也就是构建一个链表 |
| put(self, key, value) | 将 key=value 这一键值对放入符号表 |
| get(self, key) | 获取 key 所对应得值，若不存在，则返回空 |
| delete(self, key) | 删除 key 所对应的键值对 |
| \_\_contains\_\_(self, key) | 判断 key 是否存在符号表中 |
| \_find(self, key) | 寻找到 key 对应得结点，并返回此结点，没有找到返回 None |



## 基于二分查找的有序符号表  class OrderedST():

| 类方法名 | 类方法的作用 |
|---|---|
| \_\_init\_\_() | 构建符号表 |
| put(self, key, value) | 将 key=value 这一键值对放入符号表 |
| get(self, key) | 获取 key 所对应得值，若不存在，则返回空 |
| delete(self, key) | 从表中删除 key 所对应的键值对 |
| \_\_contains\_\_(self, key) | 判断 key 是否存在符号表中 |
| min(self) | 返回最小的键 |
| max(self) | 返回最大的键 |
| len(self) | 返回符号表中键值对的个数 |
| ceiling(self, key) | 大于等于 key 的最小的键 |
| floor(self, key)| 小于等于 key 的最大的键 |
| rank(self, key) | 小于 key 的键的数量 |
| select(self, k) | k为整数， 返回排名为 k 的键 |
| deleteMin(self) | 删除最小的键 |
| deleteMax(self) | 删除最大的键 |
| size(self, lokey, hikey) | 位于[lokey, hikey] 之间键的个数|
| keys(self, lokey, hikey) | 位于[lokey, hikey] 之间的键，按顺序排布|


------

# **`BST.py`**  使用二叉树实现有序符号表

在这个文件中，我们定义了两个类，一个是节点类， 一个是二叉查找树类。

## 节点类

|类方法|方法作用|
|---|---|
|\_\_init\_\_(self, key=None, value=None, lchild=None, rchild=None, N=1)|构造节点类实例， 包含五个参数， key 代表键， value 代表值， lchild 代表了左节点， rchild 代表了右节点， N 代表了此节点及其以下所包含的所有节点的个数|
|\_\_repr\_\_(self)| 打印节点实例时自动调用 |

## 二叉查找树类


|类方法|方法作用|
|---|---|
|\_\_init\_\_(self, root=None)| 构造函数，创建一个二叉查找树，根结点默认为 None|
|\_\_len\_\_(self)| 返回二叉查找树的结点个数 |
|\_\_contians\_\_(self, key)| 查看 key 这个键是否包含在此二叉查找树中 |
|\_bstSearch(self, sub_tree, key)| 在 \_\_contians\_\_ 中调用，用于查找 |
|put(self, key, value, recursion=True)| 将 (key, value) 这一键值对插入二叉查找树中， 当 recursion==True 时，即默认情况，使用递归的方式插入，否则使用非递归的方式插入|
|\_put(self, sub_tree, key, value)|使用递归的方式插入键值对，在 put() 方法中调用|
|\_putWithOutRecursion(self, sub_tree, key, value)| 使用非递归的方式插入键值对，在 put() 方法中调用 |
|\_plusN(self, key)| 使用非递归的方法插入键值对后，修改相应结点的 N 值 |
|get(self, key, recursion=True)| 获取键为 key 的结点的值 value。 当 recursion=True 的时候，使用递归的方法获取值，否则使用非递归的方法获取相应的值|
|\_get(self, sub_tree, key)| 使用递归的方法获取 key 所对应结点的 value，在 get() 方法值调用|
|\_getWithOutRecursion(self, sub_tree, key)| 使用非递归的方法获取 key 中结点对应的 value，在 get() 方法值调用|
| size(self) | 返回二叉查找树中结点的个数，等同于 len() 功能|
|\_size(self, sub_tree)| 在 size() 方法中调用， 辅助作用 |
| min(self) | 返回二叉查找树的最小键 |
| \_min(self, sub_tree) | 寻找 sub_tree（一颗子二叉查找树） 的最小键所对应的结点 |
| max(self) | 返回二叉查找树的最大键 |
| \_max(self, sub_tree) | 寻找 sub_tree 的最大键所对应的结点 |
| floor(self, key) | 返回小于等于 key 的最大键 |
| \_floor(self, sub_tree, key) | 返回 sub_tree 中小于等于 key 的最大键对应的结点，没找到则返回 None|
| ceiling(self, key) | 返回大于等于 key 的最小键 |
| \_ceiling(self, sub_tree, key) | 返回 sub_tree 中大于等于 key 的最小键对应的结点，没找到返回 None |
| select(self, k) | 返回二叉查找树排名为 k 的结点的键值 |
| \_select(self, sub\_tree, k) | 返回 sub\_tree 子树中排名为 k 的结点对应的键值，在 select() 方法中调用|
| rank(self, key) | 返回键为 key 的结点的排名，对于不存在与二叉树中键，亦能返回相应的排名，即树中小于给定键的键的个数 |
| \_rank(self, sub\_tree, key) | 返回 sub\_tree 子树中 key 键对应结点的排名 |
| deleteMin(self) | 删除查询二叉树中的最小键所对应的结点 |
| _deleteMin(self, sub_tree) | 删除 sub_tree 子树中的最小键对应的结点 |
| deleteMax(self) | 删除查询二叉树中的最大键对应的结点 |
| _deleteMax(self, sub_tree) | 删除 sub_tree 子树中的最大键对应的结点|
| delete(self, key) | 删除二叉查找树中 key 所对应的结点 |
| _delete(self, sub_tree, key) | 删除 sub_tree 中 key 所对应的结点|
| getkeys(self, lokey=None, hikey=None) | 得到排名为 [lokey, hikey] 中的所以的键 |
| _getkeys(self, sub_tree, result, lokey, hikey) | 得到 sub_tree 子树中，排名在 [lokey, hikey] 之间的键，结果存储在 result 中。|



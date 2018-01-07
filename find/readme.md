此文件夹中存放关于查找的代码，具体的代码内容的解释清查看 [http://www.wangs0622.com](http://www.wangs0622.com)

# **`ST.py`** 有序符号表
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
|\_\_init\_\_(self, root=None)| 构造函数，创建一个二叉查找树，根节点默认为 None|
|\_\_len\_\_(self)| 返回二叉查找树的节点个数 |
|\_\_contians\_\_(self, key)| 查看 key 这个键是否包含在此二叉查找树中 |
|\_bstSearch(self, sub_tree, key)| 在 \_\_contians\_\_ 中调用，用于查找 |
|put(self, key, value, recursion=True)| 将 (key, value) 这一键值对插入二叉查找树中， 当 recursion==True 时，即默认情况，使用递归的方式插入，否则使用非递归的方式插入|
|\_put(self, sub_tree, key, value)|使用递归的方式插入键值对，在 put() 方法中调用|
|\_putWithOutRecursion(self, sub_tree, key, value)| 使用非递归的方式插入键值对，在 put() 方法中调用 |
|\_plusN(self, key)| 使用非递归的方法插入键值对后，修改相应节点的 N 值 |
|get(self, key, recursion=True)| 获取键为 key 的节点的值 value。 当 recursion=True 的时候，使用递归的方法获取值，否则使用非递归的方法获取相应的值|
|\_get(self, sub_tree, key)| 使用递归的方法获取 key 所对应节点的 value，在 get() 方法值调用|
|\_getWithOutRecursion(self, sub_tree, key)| 使用非递归的方法获取 key 中节点对应的 value，在 get() 方法值调用|
| size(self) | 返回二叉查找树中节点的个数，等同于 len() 功能|
|\_size(self, sub_tree)| 在 size() 方法中调用， 辅助作用 |


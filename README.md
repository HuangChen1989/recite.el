# recite.el 一个辅助记忆的插件

`(recite-buffer-string)` 将 buffer 中的文本取出来，随机隐藏部分文本，并逐个提示 Remember it?
- 按 Y 显示文本
- 按 N 显示文本，并高亮

隐藏文本有两种模式:
- 结巴分词，隐藏词语
- 在标点符号、空格、换行处分句，隐藏句子

## 安装

依赖： 
- python3 
- python 模块 jieba
- emacs27.1 json 解析
- linux

``` emacs-lisp
(add-to-list 'load-path "~/path/to/recite.el")
(require 'recite)
```



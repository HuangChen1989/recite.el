# recite.el 辅助记忆插件
## 安装
doom emacs
``` emacs-lisp
;; package.el
(package! recite.el
  :recipe (:host github :repo "Huangchen1989/recite.el" :files ("*")))

;; config.el
(require 'recite)
```

## 使用
`M-x recite-buffer-string`

## 功能
- 将 buffer 中的文本取出来，随机隐藏部分文本，头脑中进行填空，按 y 键依次显示出来 
- 隐藏文本有3种模式:
  - word 结巴分词，隐藏词语
  - sentence 只保留每个短句的第一个字
  - sentence2 隐藏短句

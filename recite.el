;;; recite.el --- 一个辅助记忆的插件
;;; Commentary:
;;; 需要python3
;;; python库 jieba
;;; emacs27 支持json解析
(require 'seq)
;;; code:
(defvar my-shell-directory
  (if load-file-name
      (file-name-directory load-file-name)
    default-directory))

(defun count-dash (text x)
  "计算_的个数，中文字符要用两个_"
  (let* ((start (elt x 0))
         (end (elt x 1))
         (range (number-sequence start (- end 1))))
    (setq dash-sum 0)
    (seq-doseq (i range)
      (if (> (aref (substring text i (+ i 1)) 0) 126)
          (setq dash-sum (+ 2 dash-sum))
        (setq dash-sum (+ 1 dash-sum))))
    dash-sum))

(defun recite-text (text blank)
  "使用overlay隐藏部分"
  (progn (switch-to-buffer "*scratch*")
         (erase-buffer)
         (insert text)
         (seq-doseq (i blank)
           (let ((start (+ 1 (elt i 0)))
                 (end (+ 1 (elt i 1))))
             (overlay-put
              (make-overlay
               start
               end)
              'display
              (make-string
               (count-dash
                text
                i) ?_))))
         (seq-doseq (i blank)
           (let ((start (+ 1 (elt i 0)))
                 (end (+ 1 (elt i 1))))
             (if (y-or-n-p "Remenber it? ")
                 (remove-overlays
                  start
                  end)
               (progn
                 (remove-overlays
                  start
                  end)
                 (overlay-put
                  (make-overlay
                   start
                   end)
                  'face
                  'error)))))))

(defun recite-buffer-string ()
  (interactive)
  (let* ((text (buffer-string))
         (choices
          '("word" "sentence" "random"))
         (mychoice (ido-completing-read          "mode:" choices))
         (cmd (format "python %srecite.py '%s' %s"
                      my-shell-directory
                      text
                      mychoice))
         (myjson (shell-command-to-string cmd))
         (blank (json-parse-string myjson)))
    (print blank)
    (recite-text text blank)))

(provide 'recite)
;;; recite.el ends here

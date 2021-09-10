;;;###autoload
(defun recite-mode ()
  (interactive)
  (let* ((text (buffer-string))
         (dir my-shell-directory)
         (choices
          '("word" "sentence" "sentence2" "random"))
         (mychoice (ido-completing-read          "mode:" choices))
         (dir
          (if load-file-name              (file-name-directory load-file-name)            default-directory))
         (cmd (format "python %srecite.py '%s' %s"
                      dir
                      text
                      mychoice))
         (myjson (shell-command-to-string cmd))
         (myseq (json-parse-string myjson)))
    (switch-to-buffer "*scratch*")
    (seq-doseq (i myseq)
      (if (y-or-n-p "Do it?")
          (progn
            (erase-buffer)
            (insert i))
        (progn
          (erase-buffer)
          (insert i)
          )))))

(provide 'recite)

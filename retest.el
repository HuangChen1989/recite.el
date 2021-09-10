(setq text "buffer-string,se eew www")

(setq dir (file-name-directory  (or load-file-name buffer-file-name)))
(setq choices
      '("word" "sentence" "sentence2" "random"))
(setq mychoice (ido-completing-read          "mode:" choices))
(setq cmd (format "python %srecite.py '%s' %s"
                  dir
                  text
                  mychoice))
(setq myjson (shell-command-to-string cmd))
myjson
(setq myseq (json-parse-string myjson))
(progn
(switch-to-buffer "*scratch*")
(seq-doseq (i myseq)
  (if (y-or-n-p "Do it?")
      (progn
        (erase-buffer)
        (insert i))
    (progn
      (erase-buffer)
      (insert i)
      ))))
(add-to-list 'load-path "~/recite.el")
(require 'recite.el)

(setq text "buffer-string,se eew www ghjhhhhyyytggvhhhhuuyyyggg%gggggg%gggggggggggggggg")

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

(setq blank [[10 20] [30 40] [50 60]])

(defun recite-text (text blank)
  (progn (switch-to-buffer "*scratch*")
         (erase-buffer)
         (visual-line-mode)
         (insert text)
         (seq-doseq (i blank)
           (overlay-put (apply 'make-overlay (append i nil)) 'display
                        (make-string
                         (+ (- (elt i 1)
                               (elt i 0))) ?_)))
         (seq-doseq (i blank)
           (if (y-or-n-p "remenber it? ")
               (apply 'remove-overlays (append i nil))
             (progn
               (apply 'remove-overlays (append i nil))
               (overlay-put (apply 'make-overlay (append i nil)) 'face 'error))))))
(recite-text text blank)

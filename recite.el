(require 'seq)
(defvar my-shell-directory
  (if load-file-name
      (file-name-directory load-file-name)
    default-directory))


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


(defun recite-buffer-string ()
  (interactive)
  (let* ((text (buffer-string))
         (choices
          '("word" "sentence" "sentence2" "random"))
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

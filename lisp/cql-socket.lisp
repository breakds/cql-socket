(in-package #:cql-socket)

(defun cql-query (q-string &key (host "localhost") (port 17373))
  (let ((s (socket-connect host port)))
    (progn
      (format (socket-stream s) q-string)
      (force-output (socket-stream s))
      (wait-for-input s)
      (loop for line = (read (socket-stream s) nil 'eof)
         until (eq line 'eof)
         collect line))))
      
      
  
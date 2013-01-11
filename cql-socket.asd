;;;; cql-socket.asd

(asdf:defsystem #:cql-socket
  :serial t
  :depends-on (#:usocket)
  :components ((:file "lisp/package")
               (:file "lisp/cql-socket")))
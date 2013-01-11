;;;; package.lisp
;;;; package definition for cql-socket


(defpackage #:breakds.cql-socket
  (:nicknames #:cql-socket)
  (:use #:cl
        #:usocket)
  (:export cql-query))
              
;;;; package.lisp
;;;; package definition for cql-socket


(defpackage #:breakds.cql-socket
  (:nicknames #:cql-socket)
  (:use #:cl
        #:usocket)
  (:export cql-query-error
	   cql-query
	   cql-ignore-error
           cql-use-keyspace))
              
(in-package #:cql-socket)

(defun cql-query (q-string &key (host "localhost") (port 17373))
  "Issue a cql query to the python cassandra socket server."
  (let ((s (socket-connect host port)))
    (progn
      (format (socket-stream s) q-string)
      (force-output (socket-stream s))
      (wait-for-input s)
      (loop for line = (read (socket-stream s) nil 'eof)
         until (eq line 'eof)
         collect line))))

(defun cql-use-keyspace (keyspace-name &key (host "localhost") (port 17373))
  "Ask the python cassandra socket server to change the keyspace it is
  connected to"
  (cql-query (format nil "use ~a" keyspace-name) 
             :host host :port port))
      
      
  
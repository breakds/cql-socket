import threading
import SocketServer
import time
import cql
import numbers

connection = cql.connect( 'localhost', 9160 )

def typed_str( s ) :
    return str(s) if isinstance( s, numbers.Number ) else '"%s"' % str(s)
        

def list2lisp( lst ) :
    return '(%s)' % ' '.join(map(typed_str,lst))

class CQLHandler( SocketServer.BaseRequestHandler ) :
    def handle( self ) :
        global connection
        data = self.request.recv( 1024 )
        print "received query", data

        # construct response
        cursor = connection.cursor()
        try :
            cursor.execute( data )
            response = ""
            for row in cursor :
                response = response + list2lisp(row) + "\n"
            self.request.sendall( response )
            cursor.close()
        except :
            self.request.sendall( "error" )
            cursor.close()

class ThreadedTCPServer( SocketServer.ThreadingMixIn, SocketServer.TCPServer ) :
    pass

if __name__ == "__main__" :
    host, port = "localhost", 17373
    
    server = ThreadedTCPServer( ( host, port ), CQLHandler )
    server.allow_reuse_address = True
    
    ip, port = server.server_address

    server_thread = threading.Thread( target=server.serve_forever )
    server_thread.daemon = True
    server_thread.start()
    
    print 'CQL python server running ...'
    
    while True :
        time.sleep(1)

    server.shutdown()

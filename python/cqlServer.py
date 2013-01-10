import threading
import SocketServer
import time

class TestHandler( SocketServer.BaseRequestHandler ) :
    def handle( self ) :
        data = self.request.recv( 1024 )
        cur_thread = threading.current_thread()
        response = "{}: {}".format( cur_thread.name, data )
        self.request.sendall( response )

class ThreadedTCPServer( SocketServer.ThreadingMixIn, SocketServer.TCPServer ) :
    pass

if __name__ == "__main__" :
    host, port = "localhost", 17373
    
    server = ThreadedTCPServer( ( host, port ), TestHandler )
    server.allow_reuse_address
    
    ip, port = server.server_address

    server_thread = threading.Thread( target=server.serve_forever )
    server_thread.daemon = True
    server_thread.start()

    print "Server loop running in thread:", server_thread.name

    print "ip:", ip
    
    print "port:", port

    while True :
        time.sleep(1)

    server.shutdown()

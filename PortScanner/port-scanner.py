import socket
import traceback
import threading
from queue import Queue


class PortScanner(object):
    def __init__(self, hosts, ports, delay):
        self.hosts = hosts
        self.ports = ports
        self.delay = delay
        self.queue = Queue()
        for port in self.ports:
            self.queue.put(port)

    def TCP_connect(self, ip, port_number, delay):
        ''' Try to connect to a specified host on a specified port.
        If the connection takes longer then the TIMEOUT we set we assume
        the host is down. If the connection is a success we can safely assume
        the host is up and listing on port x. If the connection fails for any
        other reason we assume the host is down and the port is closed.'''

        # set up our actual socket that we will use to make the connections.
        # AF_INET refers to the Address Family, which just means addresses
        # from the internet (IP addresses).
        # SOCK_STREAM is used to create a TCP connection to the host:port
        # in question (as opposed to a datagram/UDP connection).
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # the SO_REUSEADDR flag tells the kernel to reuse a local
        # socket in TIME_WAIT state, without waiting for its natural
        # timeout to expire.
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # set the timeout (5 seconds in this example)
        # to speed up the scanning a bit
        # 0.5 is also ok
        TCPsock.settimeout(delay)
        isSuccess = False
        try:
            # call connect_ex() to connect to our previously specified host
            # and port. The script then attempts to connect to the host, and
            # returns a numeric value as the response.
            # Like connect(address), but return an error indicator instead
            # of raising an exception for errors returned by the C-level
            # connect() call (other problems, such as “host not found,” can
            # still raise exceptions). The error indicator is 0 if the operation
            # succeeded, otherwise the value of the errnovariable.
            # This is useful to support, for example, asynchronous connects.
            isSuccess = TCPsock.connect_ex((ip, port_number)) == 0

            # Close the socket.
            # This prevents any connection issues or socket
            # reuse errors in future connections.
            TCPsock.close()

            # return True if port is open or False if port is closed.
            return isSuccess

#      except:
        # https://stackoverflow.com/questions/54948548/what-is-wrong-with-using-a-bare-except
        # Bare except will catch exceptions you almost certainly don't
        # want to catch, including KeyboardInterrupt (the user hitting Ctrl+C)
        # and Python-raised errors like SystemExit
        except Exception:
            print(traceback.format_exc())
            return False

    def scan(self):
        pass


class EasiestPortScanner(PortScanner):
    def scan(self):
        for host in self.hosts:
            print("----------------------------------")
            for port in self.ports:
                print("[+] Connecting to " + host + ":" + str(port))
                if self.TCP_connect(host, port, self.delay):
                    print("    [*] Port " + str(port) + " open!")


class ThreadPortScanner(PortScanner):
    def worker(self, host, delay):
        while not self.queue.empty():
            port = self.queue.get()
            with self.print_lock:
                print("[+] Connecting to " + host + ":" + str(port))
                if self.TCP_connect(host, port, delay):
                    print("    [*] Port " + str(port) + " open!")

    def scan(self):
        # It seems lock slows the process
        self.print_lock = threading.Lock()

        for host in self.hosts:
            # To run TCP_connect concurrently
            thread_list = []

            print("------------------")

            # Spawning threads to scan ports
            for i in range(10):
                t = threading.Thread(target=self.worker, args=(host, self.delay))
                thread_list.append(t)

            # Starting threads
            for i in range(10):
                thread_list[i].start()

            # Locking the main thread until all threads complete
            for i in range(10):
                thread_list[i].join()

            for port in self.ports:
                self.queue.put(port)


if __name__ == '__main__':
    hosts = ["127.0.0.1", "192.168.1.1", "192.168.2.1",
             "192.168.2.2", "192.168.2.10"]
    ports = [22, 23, 80, 443, 445, 1026, 3306, 3389, 9999, 60000]
    portScanner = ThreadPortScanner(hosts, ports, 5)
    portScanner.scan()

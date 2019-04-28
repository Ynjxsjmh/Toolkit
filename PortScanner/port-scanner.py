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
        # set up our actual socket that we will use to make the connections.
        # AF_INET refers to the Address Family, which just means addresses from the internet (IP addresses).
        # SOCK_STREAM is used to create a TCP connection to the host:port in question (as opposed to a datagram/UDP connection).
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # set the timeout (5 seconds in this example) to speed up the scanning a bit
        TCPsock.settimeout(delay)
        isSuccess = False
        try:
            # call connect_ex() to connect to our previously specified host and port.
            # The script then attempts to connect to the host, and
            # returns a numeric value as the response.
            if TCPsock.connect_ex((ip, port_number)) == 0:
                isSuccess = True

            # Close the socket.
            # This prevents any connection issues or socket reuse errors in future connections.
            TCPsock.close()
            return isSuccess

#      except:
        # https://stackoverflow.com/questions/54948548/what-is-wrong-with-using-a-bare-except
        # Bare except will catch exceptions you almost certainly don't want to catch,
        # including KeyboardInterrupt (the user hitting Ctrl+C) and Python-raised errors like SystemExit
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
    hosts = ["127.0.0.1", "192.168.1.1", "192.168.2.1", "192.168.2.2", "192.168.2.10"]
    ports = [22, 23, 80, 443, 445, 1026, 3306, 3389, 9999, 60000]
    portScanner = ThreadPortScanner(hosts, ports, 5)
    portScanner.scan()

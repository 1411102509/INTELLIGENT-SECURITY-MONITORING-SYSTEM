import threading
import cv2
import time
import queue

#import socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('192.168.1.247',8000))



# url="rtsp://admin:admin12345678@192.168.1.13/Streaming/Channels/1"

class hkCamera(threading.Thread):
    def __init__(self, queue, ip, username="admin", password="abc12345"):
        threading.Thread.__init__(self)
        self.q = queue
        self.ip = ip
        self.username = username
        self.password = password
    def run(self):
        url = "rtsp://{}:{}@{}/Streaming/Channels/1".format(self.username, self.password, self.ip)
        cap = cv2.VideoCapture(url)
        while True:
            ret, img = cap.read()
            if ret:
                self.q.put(img)
                self.q.get() if self.q.qsize() > 4 else time.sleep(0.01)

def show_image(queueImage, identification):
    cv2.namedWindow(identification)
    #cv2.resizeWindow(identification, 640, 480)
    while (True):
        if queueImage.qsize() > 0:
            img = queueImage.get()
            cv2.imshow(identification, img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            cv2.destroyWindow(identification)
            break

def captureMutipleCamera(ip_list):
    thread_list = []
    for ip in ip_list:
        queueImage = queue.Queue(maxsize=4)
        identification = ip

        threadRead = hkCamera(queueImage, ip)
        threadShow = threading.Thread(target=show_image, args=(queueImage, identification))

        thread_list.append(threadRead)
        thread_list.append(threadShow)

    for thread in thread_list:
        #thread.daemon = True
        thread.start()

if __name__ == '__main__':
    #ip_list = ["192.168.1.11", "192.168.1.12", "192.168.1.13", "192.168.1.14",
    #            "192.168.1.15", "192.168.1.16"]
    #ip_list = ["192.168.1.2", "192.168.1.3"]
    ip_list = ["192.168.213.74"]
    captureMutipleCamera(ip_list)

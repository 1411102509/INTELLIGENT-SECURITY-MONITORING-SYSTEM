# import threading
# import cv2
# import time
# import queue
# import multiprocessing as mp
#
# src = "D:/workspace/webstorm_workspace/anfang/guard.mp4"
#
# class camera(threading.Thread):
#     def __init__(self, queue, src):
#         threading.Thread.__init__(self)
#         self.q = queue
#         self.src = src
#     def run(self):
#         cap = cv2.VideoCapture(self.src)
#         while True:
#             ret, img = cap.read()
#             if ret:
#                 self.q.put(img)
#                 self.q.get() if self.q.qsize() >= 5 else time.sleep(0.01)
#
# # class threadCameraRSTP(threading.Thread):
# #     def __init__(self, queue):
# #         threading.Thread.__init__(self)
# #         self.q = queue
# #     def run(self):
# #         cap = cv2.VideoCapture("D:/workspace/webstorm_workspace/anfang/guard.mp4")
# #         while True:
# #             ret, img = cap.read()
# #             if ret:
# #                 self.q.put(img)
# #                 self.q.get() if self.q.qsize() >= 5 else time.sleep(0.01)
# #
# # class threadCameraUSB(threading.Thread):
# #     def __init__(self, queue):
# #         threading.Thread.__init__(self)
# #         self.q = queue
# #     def run(self):
# #         print(self.q.qsize())
# #         cap = cv2.VideoCapture("D:/workspace/webstorm_workspace/anfang/guard.mp4")
# #         while True:
# #             ret, img = cap.read()
# #             if ret:
# #                 self.q.put(img)
# #                 self.q.get() if self.q.qsize() >= 5 else time.sleep(0.01)
#
# def image_save(queueImage, identification):
#     cv2.namedWindow(identification, cv2.WINDOW_NORMAL)
#     cv2.resizeWindow(identification, 640, 480)
#     while (True):
#         if queueImage.qsize() >= 1:
#             img = queueImage.get()
#             cv2.imshow(identification, img)
#         if cv2.waitKey(1) & 0xff == ord('q'):
#             cv2.destroyWindow(identification)
#             break
#
# def captureMutipleCamera(cam_list):
#     thread_ids = []
#
#     for id in cam_list:
#     ## 1.start camera threads and save threads
#         queueImage = queue.Queue(maxsize=4)
#
#         identification = id
#         threadRead = camera(queueImage, id)
#         thread_ids.append(threadRead)
#         thread_ids.append(threading.Thread(target=image_save, args=(queueImage, identification)))
#
#     for thread in thread_ids:
#         # thread.daemon = True
#         thread.start()
#
# # def captureMutipleCamera():
# #     thread_ids = []
# #     ## 1.start camera threads and save threads
# #     queueImage1 = queue.Queue(maxsize=4)
# #     queueImage2 = queue.Queue(maxsize=4)
# #
# #     identification1 = "win1"
# #     thread1 = threadCameraRSTP(queueImage1)
# #     thread_ids.append(thread1)
# #     thread_ids.append(threading.Thread(target=image_save, args=(queueImage1, identification1)))
# #
# #     identification2 = "win2"
# #     thread2 = threadCameraUSB(queueImage2)
# #     thread_ids.append(thread2)
# #     thread_ids.append(threading.Thread(target=image_save, args=(queueImage2, identification2)))
# #
# #     for thread in thread_ids:
# #         # thread.daemon = True
# #         thread.start()
#
# # url="rtsp://admin:admin12345678@192.168.1.13/Streaming/Channels/1"
#
# if __name__ == '__main__':
#     # cam_list = ["192.168.1.11", "192.168.1.12", "192.168.1.13", "192.168.1.14",
#     #             "192.168.1.15", "192.168.1.16"]
#     cam_list = ["D:/workspace/webstorm_workspace/anfang/guard.mp4", "D:/workspace/webstorm_workspace/anfang/guard1.mp4"]
#     captureMutipleCamera(cam_list)


import cv2

import time
import multiprocessing as mp

"""
Source: Yonv1943 2018-06-17
https://github.com/Yonv1943/Python/tree/master/Demo
"""
# rtsp://admin:admin12345678@192.168.1.2/Streaming/Channels/1
def image_put(q, ip, username, password):
    url = "rtsp://{}:{}@{}/Streaming/Channels/1".format(username, password, ip)
    cap = cv2.VideoCapture(url)
    while True:
        q.put(cap.read()[1])
        q.get() if q.qsize() > 1 else time.sleep(0.01)

def image_get(q, window_name):
    cv2.namedWindow(window_name, flags=cv2.WINDOW_FREERATIO)
    while True:
        frame = q.get()
        cv2.imshow(window_name, frame)
        cv2.waitKey(30)
        if cv2.waitKey(30) & 0xff == ord('q'):
            cv2.destroyWindow(window_name)
            break

def run_multi_camera(cam_list):

    mp.set_start_method(method='fork')  # init
    processes = []
    for cam in cam_list:
        queue = mp.Queue(maxsize=4)
        processes.append(mp.Process(target=image_put, args=(queue, cam[0], cam[1], cam[2])))
        processes.append(mp.Process(target=image_get, args=(queue, cam[0])))

    for process in processes:
        process.daemon = True
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    ip_list = [["192.168.1.2","admin","admin12345678"],
               ["192.168.1.11","admin","admin12345678"],
               ["192.168.1.12","admin","admin12345678"],
               ["192.168.213.79","admin","abc12345"],
               ["192.168.213.76","admin","abc12345"],
               ["192.168.1.15","admin","admin12345678"]]
    run_multi_camera(ip_list)

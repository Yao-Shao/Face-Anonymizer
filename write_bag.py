# cv2 4.1.2.30 required

import rosbag
import os
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from tqdm import *

######## config #######
BAG_NAME = r'your rosbag file name'
BAG_PATH_OLD = r'path to rosbag file folder' + BAG_NAME + '.bag'
BAG_PATH_NEW = r'path to rosbag file folder' + BAG_NAME + '_blur.bag'
PIC_PATH_BLURRED = r'path to the folder containing blurred pictures' + BAG_NAME + '_blur'
PIC_FORMAT = 'jpg'
#######################

camera_list= ['cam0','cam1','cam2','cam3','cam4','cam5']

def get_cam_path():
	res = []
	for i,cam in enumerate(camera_list):
		p = PIC_PATH_BLURRED + '/' + cam
		pp = os.listdir(p)
		pp.sort()
		ppp = [p + '/' + i for i in pp]
		# print(ppp)
		res.append(ppp)
	return res

with rosbag.Bag(BAG_PATH_NEW, 'w') as outbag:
	cp = get_cam_path()
	cnt = [0,0,0,0,0,0]
	print('loading bag...')
	inbag = rosbag.Bag(BAG_PATH_OLD)
	print('loading success!')
	num = inbag.get_message_count()
	br = CvBridge()
	with tqdm(total=num) as pbar:
		for topic, msg, t in inbag.read_messages():
			if topic == '/camera_array/cam0/image_raw/compressed':
				cv_img = cv2.imread(cp[0][cnt[0]])
				img_msg = br.cv2_to_compressed_imgmsg(cv_img, dst_format=PIC_FORMAT)
				outbag.write(topic, img_msg, msg.header.stamp if msg._has_header else t)
				cnt[0] += 1
			elif topic == '/camera_array/cam1/image_raw/compressed':
				cv_img = cv2.imread(cp[1][cnt[1]])
				img_msg = br.cv2_to_compressed_imgmsg(cv_img, dst_format=PIC_FORMAT)
				outbag.write(topic, img_msg, msg.header.stamp if msg._has_header else t)
				cnt[1] += 1
			elif topic == '/camera_array/cam2/image_raw/compressed':
				cv_img = cv2.imread(cp[2][cnt[2]])
				img_msg = br.cv2_to_compressed_imgmsg(cv_img, dst_format=PIC_FORMAT)
				outbag.write(topic, img_msg, msg.header.stamp if msg._has_header else t)
				cnt[2] += 1
			elif topic == '/camera_array/cam3/image_raw/compressed':
				cv_img = cv2.imread(cp[3][cnt[3]])
				img_msg = br.cv2_to_compressed_imgmsg(cv_img, dst_format=PIC_FORMAT)
				outbag.write(topic, img_msg, msg.header.stamp if msg._has_header else t)
				cnt[3] += 1
			elif topic == '/camera_array/cam4/image_raw/compressed':
				cv_img = cv2.imread(cp[4][cnt[4]])
				img_msg = br.cv2_to_compressed_imgmsg(cv_img, dst_format=PIC_FORMAT)
				outbag.write(topic, img_msg, msg.header.stamp if msg._has_header else t)
				cnt[4] += 1
			elif topic == '/camera_array/cam5/image_raw/compressed':
				cv_img = cv2.imread(cp[5][cnt[5]])
				# print(type(cv_img))
				img_msg = br.cv2_to_compressed_imgmsg(cv_img, dst_format=PIC_FORMAT)
				outbag.write(topic, img_msg, msg.header.stamp if msg._has_header else t)
				cnt[5] += 1
			else:
				outbag.write(topic, msg, msg.header.stamp if msg._has_header else t)
			pbar.update()

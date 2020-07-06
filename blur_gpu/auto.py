# 1. source /media/msc/Elements/Research/self-driving/Anonymizer/blur_gpu/myvenv/bin/activate
# 2. python3 auto.py

import os

cd = 'cd /media/msc/Elements/Research/self-driving/Anonymizer/blur_gpu/anonymizer'
os.system(cd)

# act = 'source ./myvenv/bin/activate'
# os.system(act)

# cd2 = 'cd anonymizer'
#os.system(cd2)

bag_name = r'your rosbag name'   
base_path = r'/media/msc/Elements/Research/self-driving/Anonymizer/bags'
exe = r'PYTHONPATH=$PYTHONPATH:/media/msc/Elements/Research/self-driving/Anonymizer/blur_gpu/anonymizer python /media/msc/Elements/Research/self-driving/Anonymizer/blur_gpu/anonymizer/anonymizer/bin/anonymize.py'
my_input = r' --input ' + base_path + '/' + bag_name + '/cam'
my_output = r' --image-output ' + base_path + '/' + bag_name + '_blur/cam' 
my_weight = r' --weights /media/msc/Elements/Research/self-driving/Anonymizer/blur_gpu/anonymizer/weight --no-write-detections'

if not os.path.exists(base_path + '/' + bag_name + '_blur'):
	os.mkdir(base_path + '/' + bag_name + '_blur')
	print('create new folder at {}'.format(base_path + '/' + bag_name + '_blur'))

for i in range(0,1):
	if not os.path.exists(base_path + '/' + bag_name + '_blur/cam' + str(i)):
		os.mkdir(base_path + '/' + bag_name + '_blur/cam' + str(i))

	job = exe + my_input + str(i) + my_output + str(i) + my_weight
	os.system(job)

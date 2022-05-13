import re

test = '''
2022-05-06 22:37:35,819 Thread 0 handle 500 data.
2022-05-06 22:37:35,820 end of for
2022-05-06 22:37:39,184 end of for 2
2022-05-06 22:50:11,227 end of for 3
2022-05-06 22:50:11,500 end of for 4
2022-05-06 22:50:11,502 before return
2022-05-06 22:50:11,502 teacher's valid_mIoU 0.493
2022-05-06 22:50:11,752 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 22:50:11,752 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 22:50:11,752 lr: 0.007252151801982005
2022-05-06 23:01:16,115 teacher's train_mIoU 0.553
2022-05-06 23:01:16,246 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 23:01:16,246 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 23:01:16,246 lr: 0.007194134587566149
2022-05-06 23:12:21,413 teacher's train_mIoU 0.572
2022-05-06 23:12:21,535 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 23:12:21,535 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 23:12:21,535 lr: 0.00713658151086562
2022-05-06 23:23:25,664 teacher's train_mIoU 0.562
2022-05-06 23:23:25,818 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 23:23:25,818 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 23:23:25,818 lr: 0.007079488858778695
2022-05-06 23:34:30,132 teacher's train_mIoU 0.571
2022-05-06 23:34:30,282 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 23:34:30,282 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 23:34:30,282 lr: 0.007022852947908466
2022-05-06 23:45:34,784 teacher's train_mIoU 0.580
2022-05-06 23:45:34,915 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 23:45:34,915 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 23:45:34,915 lr: 0.006966670124325198
2022-05-06 23:56:39,206 teacher's train_mIoU 0.569
2022-05-06 23:56:39,359 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-06 23:56:39,359 train-512x1024_teacher_batch12-20220506-142555
2022-05-06 23:56:39,359 lr: 0.006910936763330596
2022-05-07 00:07:43,683 teacher's train_mIoU 0.559
2022-05-07 00:07:43,838 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-07 00:07:43,838 train-512x1024_teacher_batch12-20220506-142555
2022-05-07 00:07:43,838 lr: 0.006855649269223951
2022-05-07 00:18:48,270 teacher's train_mIoU 0.571
2022-05-07 00:18:48,383 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-07 00:18:48,383 train-512x1024_teacher_batch12-20220506-142555
2022-05-07 00:18:48,383 lr: 0.00680080407507016
2022-05-07 00:29:52,642 teacher's train_mIoU 0.584
2022-05-07 00:29:52,795 /home/asg1g18/FasterSeg/train/fasterseg
2022-05-07 00:29:52,795 train-512x1024_teacher_batch12-20220506-142555
2022-05-07 00:29:52,795 lr: 0.006746397642469599
2022-05-07 00:40:57,192 teacher's train_mIoU 0.572
2022-05-07 00:40:57,194 1
2022-05-07 00:40:57,194 Thread 0 handle 500 data.
'''

train_miou = re.compile("train_mIoU (\d+.\d+)")
valid_miou = re.compile("valid_mIoU (\d+.\d+)")

fpath = './teacher_trained_100.txt'

with open(fpath) as f:
    for line in f:
        if re.search(train_miou, line):
            print('t: ', re.findall(train_miou, line)[0])
        elif re.search(valid_miou, line):
            print('v: ', re.findall(valid_miou, line)[0])
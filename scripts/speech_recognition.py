#!/usr/bin/env python
# -*- coding: utf-8 -*-
from speech_recognition_msgs.msg import SpeechRecognitionCandidates
from std_msgs.msg import String
import rospy

class SpeechRecognition(object):
    def __init__(self):
        rospy.Subscriber('/Tablet/voice', SpeechRecognitionCandidates, self.callback)
        self.pub_ = rospy.Publisher('/speech', String, queue_size=1)
        self.num_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
        self.num_list = ['1','2','3','4','5','6','7','8','9']
        self.subject_list = ['全部', 'everything']
        self.verb_list = ['片付けて', '片付けといて', '直して', '直しといて', 'なおして', 'なおしといて', 'clean']
        print SpeechRecognitionCandidates

    def callback(self, msg):
        rospy.loginfo('{} ({})'.format(msg.transcript[0], msg.confidence[0]))
        raw_msg = str()
        pub_msg = str()
        if msg.confidence[0] > 0.5 :
            raw_msg = msg.transcript[0]
            tmp_flg = True

            for n_dic_key in self.num_dict.keys():
                if n_dic_key in raw_msg:
                    raw_msg = raw_msg.replace(n_dic_key,self.num_dict[n_dic_key])

            rospy.loginfo('%s', raw_msg)
            
            for sbj in self.subject_list:
                if sbj in raw_msg:
                    for verb in self.verb_list:
                        if verb in raw_msg:
                            tmp_flg = False
                            self.pub_.publish('99')
            if tmp_flg:
                for data in list(raw_msg):
                    if data in self.num_list:
                        pub_msg += data
                if len(pub_msg) == 2:
                    self.pub_.publish(pub_msg)
    

if __name__ == '__main__':
    rospy.init_node('speech_recognition')
    speech_recognition = SpeechRecognition()
    rospy.spin()

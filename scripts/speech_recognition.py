#!/usr/bin/env python
# -*- coding: utf-8 -*-
from speech_recognition_msgs.msg import SpeechRecognitionCandidates
from std_msgs.msg import String
import rospy

class SpeechRecognition(object):
    def __init__(self):
        rospy.Subscriber('/Tablet/voice', SpeechRecognitionCandidates, self.callback)
        self.pub_ = rospy.Publisher('/speech', String, queue_size=1)
        self.num_list = ['1','2','3','4','5','6','7','8','9']
        print SpeechRecognitionCandidates

    def callback(self, msg):
        rospy.loginfo('{} ({})'.format(msg.transcript[0], msg.confidence[0]))
        raw_msg = str()
        pub_msg = str()
        if msg.confidence[0] > 0.9 :
            raw_msg = msg.transcript[0]
            for data in list(raw_msg):
                if data in self.num_list:
                    pub_msg += data
            if len(pub_msg) == 2:
                self.pub_.publish(pub_msg)
    

if __name__ == '__main__':
    rospy.init_node('speech_recognition')
    speech_recognition = SpeechRecognition()
    rospy.spin()

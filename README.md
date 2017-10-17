# speech_recognition
Speech Recognition node for motoman pick & place task using [rwt_speech_recognition]().  
This package transfers the topic from rwt_speech_recognition into `/speech` topic.  

## Usage
### 1. launch rwt_speech_recognition
```bash
$ roslaunch rwt_speech_recognition rwt_speech_recognition.launch
```

### 2. Open the link
Open the link -> http://localhost:8000/rwt_speech_recognition using Chrome or Chromium Browser.  
**!! CAUTION !!** You can not use any other browsers including Firefox !

### 3. run this program
```bash
$ rosrun speech_recognition speech_recognition.py
```

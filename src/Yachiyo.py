
from PySide6.QtCore import QObject, Signal, QTimer

class Yachiyo(QObject):
    emotion_changed = Signal(str)#创建一个信号
    
    def __init__(self):
        super().__init__()
        self.emotion = "normal"
        self.name="Yachiyo"
    
    def touch_head(self):
        self.emotion = "happy"
        self.emotion_changed.emit(self.emotion)
        #label.setText("Yachiyo is happy!")#设置标签文本
        #持续一段时间，发生一些变化和表现，然后回归正常，
        #中间涉及表情的等变化，还会有语音
        #time.sleep(5)错误的
        QTimer.singleShot(5000, self.normal)  # 5秒
    def touch_nose(self):
        self.emotion = "angry"
        self.emotion_changed.emit(self.emotion)
        QTimer.singleShot(5000, self.normal)  
        # 5秒生气之后可以变傲娇

    def normal(self):
        self.emotion = "normal"
        self.emotion_changed.emit(self.emotion)
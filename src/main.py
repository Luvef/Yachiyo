#print("hello Yachiyo")
import sys 
#import time不可以，会阻塞UI线程，导致界面卡死
from Yachiyo import Yachiyo
from UI import update_emotion, window_set

def main():
    #button.clicked.connect(touch_head)#按钮点击事件绑定函数
    window,app, button_happy, button_angry, label, layout = window_set()  # 创建窗口和应用
    update_emotion("normal",label)  # 初始化情绪显示为正常
    yachiyo = Yachiyo()
    yachiyo.emotion_changed.connect(lambda emotion: update_emotion(emotion, label))  # 连接信号和槽函数
    button_happy.clicked.connect(yachiyo.touch_head)
    button_angry.clicked.connect(yachiyo.touch_nose)  # 这里可以根据需要定义不同的行为
    sys.exit(app.exec())#时间循环

if __name__ == "__main__":
    main()

import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

#button.clicked.connect(touch_head)#按钮点击事件绑定函数
def update_emotion(emotion,label):
    if emotion == "happy":
        label.setText("Yachiyo is happy!")
        print("Yachiyo is happy!")
    elif emotion == "angry":
        label.setText("Yachiyo is angry!")
        print("Yachiyo is angry!")
    elif emotion == "normal":
        label.setText("Yachiyo is normal!")
        print("Yachiyo is normal!")

def window_set():
    app = QApplication(sys.argv)#创建Qt应用
    label = QLabel("hello Yachiyo")#创建标签
    button_happy = QPushButton("摸摸头,开心")#创建按钮
    button_angry = QPushButton("摸摸头,生气")#创建按钮
    layout = QVBoxLayout()#创建垂直布局
    layout.addWidget(label)#添加标签到布局
    layout.addWidget(button_happy)#添加开心按钮到布局
    layout.addWidget(button_angry)#添加生气按钮到布局

    window = QWidget()#创建窗口
    window.setWindowTitle("Yachiyo")#设置窗口标题
    window.resize(800,600)#设置窗口大小
    #window.show()#展示窗口
    window.setLayout(layout)#设置窗口布局
    window.show()#展示窗口
    return window, app, button_happy, button_angry, label, layout
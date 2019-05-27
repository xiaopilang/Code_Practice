import  os
import  allure
class Test:

    def test_001(self):
        print("测试开始")

        with open(os.getcwd() + os.sep + "scripts/4.PNG", "rb")as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)

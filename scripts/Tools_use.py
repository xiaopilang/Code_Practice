import  os
import  allure
import pytest


class Test:

    @allure.step(title="我是测试第一步")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        print("001测试开始")

        with open(os.getcwd() + os.sep + "scripts/4.PNG", "rb")as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        assert  False


    @allure.step(title="我是测试第二步")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_002(self):
        allure.attach("用户名:", "张三")
        allure.attach("密码:", "123456")
        print("002测试开始")
        with open(os.getcwd() + os.sep + "scripts/4.PNG", "rb")as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        assert True
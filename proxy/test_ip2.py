import telnetlib
# 测试ip是否可用

try:
    telnetlib.Telnet('10.10.1.10', port='1080', timeout=3)
except:
    print('ip无效！')
else：
    print('ip有效！')
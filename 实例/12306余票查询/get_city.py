import re,requests
import json

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Cookie': 'JSESSIONID=9E3488966D924E61AB79EEF6F01AB2A9; _jc_save_wfdc_flag=dc; RAIL_EXPIRATION=1589428661271; RAIL_DEVICEID=WCoYP_NLfSDSadho5zWOklc6cAettdAggtkfSCP_OGoZvLDVdLaxOeohq2tPSwv6sp2zuk244A7rfyPXR86UebPgyVMx3xv3OW6RreoSLeb9xij7ZFw_njR4S4ixFu2qzh65YPWQaeLRiWPpB0co304Luhdy_vfs; BIGipServerotn=367526154.64545.0000; route=495c805987d0f5c8c84b14f60212447d; BIGipServerpassport=887619850.50215.0000; BIGipServerportal=2949906698.16671.0000; _jc_save_fromStation=%u8D35%u9633%u5317%2CKQW; _jc_save_toStation=%u6850%u6893%u4E1C%2CTDE; _jc_save_fromDate=2020-05-13; _jc_save_toDate=2020-05-11'
}
response = requests.get(url=url,headers=headers)
#将车站的名字和编码进行提取
chezhan = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
chezhan_code = dict(chezhan)
#进行交换
chezhan_names = dict(zip(chezhan_code.keys(),chezhan_code.values()))
#打印出得到的车站字典
# print(chezhan_names)
with open('result.json', 'w', encoding='utf-8') as fw:
	# ensure_ascii=False 解决乱码
	# fw.write(json.dumps(stat, ensure_ascii=False))
	json.dump(chezhan_names,fw,ensure_ascii=False)
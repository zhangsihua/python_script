"""一、安装（python 版本建议 3.7 以上）
    pip install --upgrade  prestool   (pip 版本22.0.3以上才可安装成功)
"""

'''二、常用工具'''

from prestool.Tool import Tool


tool = Tool()

'''随机数据'''
tool.random_name()  # 随机姓名
tool.random_phone()  # 随机手机号
tool.random_ssn()  # 随机身份证

tool.random_string(16)  # 随机位数的字符串
tool.random_number(8)  # 随机位数的数字

tool.random_ua()  # 随机UA
tool.random_ua('chrome')  # 随机UA-Chrome
tool.random_ua('firefox')  # 随机UA-Firefox
tool.random_ua('ie')  # 随机UA-IE
tool.random_ua('opera')  # 随机UA-opera
tool.random_ua('safari')  # 随机UA-safari

'''编码解码'''
tool.url_encode('编码前的url地址')  # 编码
tool.url_decode('解码前的url地址')  # 解码

tool.base_64_encode('编码前的字符串')  # base64编码


'''加密相关'''
tool.to_md5('原始字符串')
tool.to_hmac_256('原始字符串', '加密key')
tool.to_sha_256('原始字符串')

'''发送消息'''
'钉钉'
tool.ding_talk_token = '钉钉机器人token'
tool.ding_talk_sign_key = '钉钉机器人签名key'

tool.send_ding_talk_msg('消息内容')
'企业微信'
tool.qy_wechat_token = '企业微信机器人token'

tool.send_qy_wechat_msg('消息内容')
'邮件'
tool.mail_from_user_host = '发件地址host'
tool.mail_from_user = '发件人邮箱号'
tool.mail_from_user_pwd = '发件人pwd'

tool.send_mail_msg(to_user='收件人邮箱地址（列表）', title='邮件标题', content='邮件内容')

'''时间相关'''
tool.time_stamp()  # 秒级时间戳10位
tool.time_stamp('ms')  # 毫秒级时间戳13位

tool.get_now_time()  # 获取当前时间 20201206000000
tool.get_now_time('-')  # 获取当前时间 2020-12-06 00:00:00

tool.date_to_time_stamp('2012-01-01 00:00:00')  # 时间字符串转为时间戳
tool.time_stamp_to_date(1732312234)  # 时间戳转为时间字符串

'格式转换'
tool.json_dumps({"test": "python字典"})  # 字典转json
tool.json_loads('{"test": "python字典"}')  # json转字典
tool.xml_to_dict('<xml><data>字符串</data></xml>')  # xml转成python字典
tool.dict_to_xml({"test": "python字典"})  # python字典 转成xml

'http 请求'
tool.http_client(url='', data={}, method='GET')  # get请求
tool.http_client(url='', data={}, method='POST')  # post请求

tool.get_cookies(url='接口地址', data={}, method='GET')
tool.get_cookies(url='接口地址', data={}, method='POST')

tool.trans_data_to_url(url='接口地址', data={})  # 把参数拼接到url上

'dubbo 接口'
tool.dubbo_args('参数1', '参数2', '参数3')  # dubbo接口参数
tool.invoke_dubbo('地址', '端口', '服务API名', '接口方法名', 'dubbo接口参数')  # 请求dubbo接口

'其他'
tool.logger('日志信息')
tool.get_ip_by_url('url地址')  # 获取ip

"""三、数据库语句（MySQL）"""
'1) 生成数据库 sql 语句'
from prestool.PresMySql import SqlStr

sql = SqlStr()

'''查询语句'''
'''target 不传时，为全部字段，即 *，where={'key':'value'}'''
sql.select_sql_str(table='table1', where={'id': 1, 'name': '张三'})

'''select * from table1 where id = 1 and name = '张三';'''
'''target=[i1,i2,i3] 时，为相应字段'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], where={'id': 1, 'name': '张三'})

'''select a, b, c from table1 where 1=1 and id=1 and name='张三';'''
'''limit=10 limit='10,1000' 为筛选限制字段'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], order={'age': 'desc', 'score': 'desc'}, limit=20)

'''select a, b, c from table1 where 1=1 order by age desc, score desc limit 20;'''
'''where 条件中有的字段为 null 或者 not null 时'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], where={'id': 1, 'name': 'null', 'age': not None})

'''select a, b, c from table1 where 1=1 and id=1 and name is null and age is not null;'''
'''支持排序语句'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], order={'age': 'desc', 'score': 'desc'})

'''select a, b, c from table1 order by age desc, score desc;'''
'''支持查询 in 语句'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], select_in={'orders': [123121312, 123123445, 213123]})

'''select a, b, c from table1 where 1=1 and orders in (123121312, 123123445, 213123);'''
'''支持 like 语句'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], like={'name': '%光', 'address': "中国%"})

'''select a, b, c from table1 where 1=1 and name like '%光' and address like '中国%';'''
'''支持 between 语句'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'], between={'age': (10, 20), 'year': (2021, 2022)})

'''select a, b, c from table1 where 1=1 and age between 10 and 20 and year between 2021 and 2022;'''
'''支持大于、小于语句'''
sql.select_sql_str(table='table1', target=['a', 'b', 'c'],
                   compare={'age': {'>': 10, '<': 20}, 'year': {'>=': '2021'}})

'''select a, b, c from table1 where 1=1 and age > 10 and age < 20 and year >= 2021;'''


'''更新语句'''
'''target 为要更新的数据，为字典结构 (支持大于、小于语句、between 语句、like 语句、in 语句)'''
sql.update_sql_str(table='table1', target={'name': '李四', 'age': 15}, where={'id': 1, 'name': '张三'})
'''update table1
set name='李四',
    age=15
where id = 1
  and name = '张三';

删除数据
支持大于、小于语句、between 语句、like 语句、in 语句
sql.delete_sql_str(table='table1', where={'id': 1, 'name': '张三'})
delete
from table1
where id = 1
  and name = '张三';

插入数据
sql.insert_sql_str(table='table1', target={'id': 1, 'name': '张三'})
insert into table1 (id, name)
values (1, '张三');'''


"""2) 执行数据库语句"""

from prestool.PresMySql import PresMySql

pres = PresMySql()
'''初始化数据库信息'''
pres.mysql_host = ''
pres.mysql_port = 3306
pres.mysql_user = ''
pres.mysql_pwd = ''
pres.mysql_db_name = ''
pres.mysql_charset = 'utf8mb4'

'''执行相应语句即可，执行的方法参数等同于第三节所述的 sql 语句，如'''
pres.to_query(table='table1', target=['a', 'b', 'c'], between={'age': (10, 20), 'year': (2021, 2022)})

pres.to_insert(table='table1', target={'id': 1, 'name': '张三'})

pres.to_delete(table='table1', where={'id': 1, 'name': '张三'})

pres.to_update(table='table1', target={'name': '李四', 'age': 15}, where={'id': 1, 'name': '张三'})

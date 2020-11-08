#!/usr/bin/python3
import mysql.connector
import pymysql
import json,os,sys,getopt,argparse

#选择所属组号

# 内部接口：
# 从前端接收的：
# {
#     "user_id":"00001",
#     "user_group_id":"1"
# }
# 返回的：
# {
#     "status":true,
#     "msg":"选择成功"
# }
# {
#     "status":false,
#     "msg":"？"
# }




class choose_group():
    def my_choose_group(jsonmessage):
        tmp = json.loads(jsonmessage)
        mydb = pymysql.connect("localhost","root","","vote_system" )
        gcursor = mydb.cursor()

        ret = {'status':'','msg':''}
        try:
            gcursor.execute("UPDATE account SET user_group_id = %s WHERE user_id = %s",[ tmp['user_group_id'], tmp['user_id'] ])
            mydb.commit()
            #回送成功消息
            ret['status'] = 'true'
            ret['msg'] = '选择成功'
        except:
            mydb.rollback()
            #回送失败消息
            ret['status'] = 'false'
            ret['msg'] = '选择失败'
        gcursor.close()
        mydb.close()
        return json.dumps(ret)


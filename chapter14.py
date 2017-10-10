# pyhon3 操作mysql
import pymysql

#封装数据库
class mysqlHelper():
    def __init__(self, config): #初始化数据库连接信息，以字典形式
       self.config=config       #config={'host':'localhost'}
#连接数据库
    def getCon(self):
        try:
            self.db = pymysql.connect(**self.config) #字典转换为列表传入
            self.curs=self.db.cursor()
            print('数据库连接成功')
        except pymysql.DatabaseError as  e:
            print('数据库连接异常:%s'%e)
#关闭数据库
    def closeCon(self):
        try:
            self.curs.close()
            self.db.close()
            print('数据库关闭成功')
        except pymysql.Error as e:
            print('数据库关闭异常:%s'%e)
#查询操作
    def select(self,sql,*params):
        self.getCon()
        try:
            count=self.curs.execute(sql,params) #cursor.execute()执行会返回影响行数
            result=self.curs.fetchall()
            print('查询成功,共有%s条,结果为:\n%s'%(count,result))
            return result
        except pymysql.Error as e:
            print('***查询异常:%s'%e)
        finally:
            self.closeCon()
#更新操作
    def update(self,sql,*params):
        self.getCon()
        try:
            affect=self.curs.execute(sql,params)
            self.db.commit()
            print('更新成功,受影响行数有%s条:'%affect)
        except pymysql.Error as e:
            print('***更新异常:%s'%e)
            self.db.rollback()
            print('---数据已回滚---')
        finally:
            self.closeCon()
#删除操作
    def delete(self,sql,*params):
        self.getCon()
        try:
            affect = self.curs.execute(sql,params)
            self.db.commit()
            print('删除成功,受影响行数有%s条:' % affect)
        except pymysql.Error as e:
            print('***删除异常:%s' % e)
            self.db.rollback()
            print('---数据已回滚---')
        finally:
            self.closeCon()

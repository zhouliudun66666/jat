## JAT

JEX Auto Test - JEX 接口自动化测试

## 项目结构

- 1、业务层
   - 1.文件夹如：service文件夹
     -  ServiceUser.py --编写文件为用户管理所有接口业务逻辑代码
- 2、数据层
   - 1.文件夹如：data文件夹
     - Db.py --编写连接数据库以及查询sql
- 3、测试报告层
   - 1.文件夹如：report文件夹
     - TestReport_20180816135241.html --自动生成测试报告html 
- 4、测试用例层
   - 1.文件夹如：testcase文件夹
     - TestCaseUser.py --编写用户管理测试用例
- 5、公共方法层
   - 1.文件夹如：common
     - Common.py --编写存放公共方法
     - Utils.py --编写get、post方法封装

## 安装工具、下载安装包

- 1、安装编辑器：IntelliJ IDEA 2018.1 x64
- 2、环境准备
   - 开发语言：Python3
   - 安装python，配置环境变量
- 3、安装库如下
   - pip install requests 
   - pip install PyMySQL

## git常用命令   

- 1.克隆库： git clone http://git.coinfex.com/qa/jat.git
- 2.创建分支：git checkout -b feature/user
- 3.查看状态：git status
- 4.修改所有文件到暂存区：git add .
- 5.提交到工作区的备注：git commit -m "XXXX"
- 6.拉取远程分支到本地分支（合并）：git pull origin develop
- 7.将本地分支提交到远程分支：git push origin develop

- test
# 这是工作报告功能的Api，用来记录员工工作时间，工作时长以及工作内容。
# working_report

# Set up 
# 安装虚拟环境 
sudo apt install python3-virtualenv
# 建立虚拟环境 
virtualenv venv
# 激活虚拟环境 
source venv/bin/activate  
# 安装依赖 
pip install -r requirements.txt
# 安装数据库 
flask db init
flask db migrate
flask db upgrade 
# 启动服务器 
gunicorn app:app -b 0.0.0.0:5000 -D -p app.pid -w 4 --reload

# Postman的Json文档文件的根目录下。

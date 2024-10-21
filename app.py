from flask import Flask, render_template, request, session, redirect #轉向
from functools import wraps
from dbUtils import getList ,add ,setfinish ,delete #import dbUtils 並得到 getList 這個指令

# creates a Flask application, specify a static folder on /
app = Flask(__name__, static_folder='static',static_url_path='/')
#set a secret key to hash cookies
app.config['SECRET_KEY'] = '123TyU%^&'

#define a function wrapper to check login session
def login_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		loginID = session.get('loginID')
		if not loginID:
			return redirect('/loginPage.html')
		return f(*args, **kwargs)
	return wrapper
#wraps(f) 讓沒有登入的人看不到內容

@app.route("/") 
@login_required
def hello(): 
	message = "Hello, World .Im Eva"
	return message




@app.route("/test/<string:name>/<int:id>")
#取得網址作為參數
def useParam(name,id):
	return f"got name={name}, id={id} "
def useParam(name,id):
 #check login inside the function
 if not isLogin():
  return redirect('/loginPage.html')
 return f"got name={name}, id={id} "

@app.route("/edit")
#使用server side render: template 樣板
def h1():
	dat={
		"name": "大牛",
		"content":"內容說明文字123",
		"option1":"yes",
		"option2":"NO",
		"img":"/dog.jpg"
	}
	#editform.html 存在於 templates目錄下, 將dat 作為參數送進 editform.html, 名稱為 data
	return render_template('editform.html', data=dat)


@app.route("/update",methods=['POST'])
def upd():
	name=request.form['name']  #用post的話用form取得  用的get話用args取得   
	cnt=request.form['content']
	#sql
	html=f"update===> nnn:{name} , cnt:{cnt}"
	return html

@app.route("/list")
#使用server side render: template 樣板
def h2():
	dat=[ 
		{
			"name": "大牛",
			"p":"愛吃瓜"
		},
		{
			"name": "小李",
			"p":"怕榴槤"
		},
		{
			"name": "",
			"p":"ttttt"
		},
		{
			"name": "老謝",
			"p":"來者不拒"
		}
	]
	return render_template('list.html', data=dat)

@app.route('/input', methods=['GET', 'POST']) #取得使用使用者輸入參數的
def userInput():
	if request.method == 'POST':
		form =request.form
	else:
		form= request.args

	txt = form['txt']  # pass the form field name as key
	note =form['note']
	select = form['sel']
	msg=f"method: {request.method} txt:{txt} note:{note} sel: {select}"
	return msg

@app.route("/listjob") #db顯示
#使用server side render: template 樣板
def gl():
	dat=getList()
	return render_template('todolist.html', data=dat) 
#把傳回值交給todolist.html樣版並填入 給查詢的人看

#another way to check login session
def isLogin():
 return session.get('loginID')

#handles login request
@app.route('/login', methods=['POST']) #log in 
def login():
	form =request.form
	id = form['ID']
	pwd =form['PWD']
	#validate id/pwd
	if id=='123' and pwd=='456':
		session['loginID']=id
		return redirect("/")
	else:
		session['loginID']=False
		return redirect("/loginPade.html")
	
@app.route('/addjob', methods=['POST']) #取得使用使用者輸入參數的
def addjob():
	if request.method == 'POST':
		form =request.form
	else:
		form= request.args

	jobname = form['name']  # pass the form field name as key
	jobcontent =form['jobcontent']
	due = form['due']
	add(jobname,jobcontent,due) #上面那幾個變數
	return redirect("/listjob")

@app.route('/setfinish', methods=['GET']) 
def done():
	if request.method == 'POST':
		form =request.form
	else:
		form= request.args

	id = form['id']  
	setfinish(id)
	return redirect("/listjob")

@app.route('/delete', methods=['GET']) 
def delete_job():
	if request.method == 'POST':
		form =request.form
	else:
		form= request.args
	id = request.args.get('id') 
	#id = form.get['id']  
	delete(id)
	return redirect("/listjob")
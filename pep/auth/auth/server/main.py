from flask import Blueprint, redirect, request, render_template, flash, abort, jsonify, session, make_response
from .models import User
from .forms import LoginForm
from datetime import datetime, timedelta
from urllib.request import Request, urlopen
import json

main = Blueprint('main', __name__)
expire_minutes = 180

@main.route('/auth/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            #if is_authorized(dict(request.headers), user):
            session.permanent = True                
            main.permanent_session_lifetime = timedelta(minutes=expire_minutes)
            expires = int(datetime.now().timestamp())+60*expire_minutes
            
            user.last_login = str(datetime.now().timestamp())
            session[str(user.id)] = user.last_login 
            
            response = make_response(redirect(request.args.get('next')))
            response.set_cookie('user_id', str(user.id), expires=expires)
            response.set_cookie('last_login', user.last_login, expires=expires)
            return response
            #else: abort(401) # Unauthorized
        else:
            flash('Invalid username/password, please check your login details and try again.')
            return redirect('/auth/login')
    return render_template('login.html', form=form, next=dict(request.headers)['Request-Uri'])

@main.route('/auth/logout', methods=['GET'])
def logout():
    user_id = request.cookies.get('user_id', None)
    last_login = request.cookies.get('last_login', None)
    if user_id is not None and last_login is not None:
        if user_id in session and session[user_id] == last_login:
            session.pop(user_id)
    response = make_response(abort(401))
    response.set_cookie('user_id', '', expires=0)
    response.set_cookie('last_login', '', expires=0)
    return response

@main.route('/auth/is_login', methods=['GET','POST','PUT'])
def is_login():
    ### デバッグ用：リクエスト内容の表示
    print('----- Debug: Request Header -----')
    print(request.headers)
    print('----- /Debug: Request Header -----')
    print('----- Debug: Request Body -----')
    print(request.data)
    print('----- /Debug: Request Body -----')
    
    ### Cookieを見てユーザがログイン済みの状態ならPDPに通してよいか確認する
    user_id = request.cookies.get('user_id', None)
    last_login = request.cookies.get('last_login', None)
    if user_id is not None and last_login is not None:
        if user_id in session and session[user_id] == last_login:
            user = User.query.filter_by(id=user_id).first()
            ### 引数にPDPに必要なデータを渡す
            if is_authorized(dict(request.headers), user):
                # 許可された場合、ステータスコード200を返す
                return jsonify({'message':'OK'}), 200
            else:
                # 拒否された場合、Unauthorizedを返す
                abort(403)
        else:
            # 認証されていない場合、Unauthenticatedを返す
            return abort(401) 
    else:
        # 認証されていない場合、Unauthenticatedを返す
        return abort(401) 
    return jsonify({'message':'OK'}), 200

### ここでPDPとのデータのやり取りを行う。
### オリジナルのリクエストから、必要なデータをJSON形式で送信する
### 追加で送信が必要な場合はここのrequest_infoに追加する
def is_authorized(headers, user):
    request_info = {}
    request_info['X-Forwarded-For'] = headers['X-Forwarded-For']
    request_info['Request-Host'] = headers['Request-Host']
    request_info['Request-Uri'] = headers['Request-Uri']
    request_info['User'] = user.name
    request_info['Role'] = user.role
    if 'Request' in headers.keys():
        request_info['Request'] = headers['Request']
    if 'Request-Method' in headers.keys():
        request_info['Request-Method'] = headers['Request-Method']
    if 'Request-Body-File' in headers.keys():
        request_info['Request-Body-File'] = headers['Request-Body-File']
    if 'Request-Body' in headers.keys():
        request_info['Request-Body'] = headers['Request-Body']
    # リクエストを作成してPOSTする
    with urlopen(Request('http://pdp:5000/', json.dumps(request_info).encode(), method='POST')) as response:
        response_body = json.loads(response.read().decode())
        print(response_body)
    if response_body['message'] == 'OK': return True
    else: return False

@main.route('/403', methods=['GET'])
def unauthorized():
    return render_template('401.html')
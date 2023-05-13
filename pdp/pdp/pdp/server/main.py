from flask import Blueprint, request, render_template, flash, abort, jsonify, session
from .models import User
from datetime import datetime, timedelta
import json

main = Blueprint('main', __name__)

@main.route('/', methods=['POST'])
def PA():
    ### PEPから送られてきたデータを受信する
    request_info = json.loads(request.get_data().decode())

    ### Policy Engineにリクエスト内容を送信し、送信判定を行う
    ### PEがFalseの場合はアクセスNG。Trueの場合はアクセスOKとする
    if not PE(request_info):
        print({'message':'NG'})
        return jsonify({'message':'NG'}), 200
    else:
        print({'message':'OK'})
        return jsonify({'message':'OK'}), 200
    
def PE(request_info):
    ### デバッグ用：リクエスト内容の表示
    print('----- Debug: Request Data -----')
    print(request_info)
    print('----- /Debug: Request Data -----')
    
    ### Trust Algorithmにて信用スコアを計算する
    ### 方程式等によりスコアを計算したい場合に使用する
    #trust_score = TrustAlgorithm(request_info)

    ### ここでリクエストを通して良いか判定を行う
    ### request_info内のパラメータの取得例
    ### 接続元IPアドレス：request_info['X-Forwarded-For']
    
    return True

def TrustAlgorithm(request_info):
    ### 信用スコアを計算したい場合に使用
    return 1

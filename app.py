import datetime
import random
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

today = datetime.date.today()

@app.context_processor
def return_today():
    today = datetime.date.today()
    return dict(today=today)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/dateCalcultor', methods=['GET', 'POST'])
def dateCalcultor():
    days = 'xx'
    year = today.year
    month = today.month
    day = today.day
    saying = [
        '机不可失，时不再来。',
        '莫说年纪小，人生容易老。',
        '把一生年作一天，把一天看作一生。',
        '寸阴自惜。',
        '一寸光阴一寸金，寸金难买寸光阴。',
        '少年易学老难成，一寸光阴不可轻。——朱熹',
        '吾生也有涯，而知也无涯。——庄子',
        '时间的步伐有三种：未来姗姗来迟，现在像箭一样飞逝，过往永远静立不动。——席勒',
        '最严重的浪费就是时间的浪费。——布封',
        '人生有一道困难，那就是如何使一寸光阴即是一寸生命。'
    ]
    if request.method == 'POST':
        year = request.form.get('year') #传入表单对应输入字段的name值
        month = request.form.get('month')
        day = request.form.get('day')
        fmt = '%Y-%m-%d'
        # 验证数据
        try:
            inputDate = datetime.datetime.strptime('-'.join([year, month, day]), fmt).date()
        except ValueError:
            flash('哦豁，输入数据有误。康康是不是输错了8')
            return redirect(url_for('dateCalcultor')) #重定向回主页
        # if inputDate = datetime.datetime.strptime('-'.join([year, month, day]), fmt).date():
        #     flash('输入数据有误.')
        #     return redirect(url_for('dateCalcultor')) #重定向回主页
        flash(saying[random.randint(0, len(saying) - 1)])
        # inputDate = datetime.datetime.strptime('-'.join([year, month, day]), fmt).date()
        days = (inputDate - today).days
    return render_template('index.html', days=days, year=year, month=month, day=day)

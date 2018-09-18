## django工程
项目结构：

```
├── combat_team  # 战队管理
├── extra_apps  # xadmin源码
├── game # 现金积分相关
├── cmd.txt # 启动项目命令
├── common  # 一些utils或者组件
├── member  # 用户中心
├── mysite  # 项目配置文件
├── static  # 静态文件资源
├── templates #html
├── manage.py #启动文件

```

## 数据表

```
+------------------------------------+
| members            				 |  # 用户信息
| CombatTeam                 		 |  # 战队信息
| GameType				             |	# 游戏类型
| CombatTeamMembers      			 |  # 战队人员信息
| TeamRequest				         |  # 申请入队信息              |
+------------------------------------+
```

## app目录典型结构
```
├── __init__.py
├── ad.py
├── adminx.py  # 后台注册一些view
├── apis.py  # 接口逻辑
├── forms.py
├── i18n.txt
├── logics.py  # 逻辑实现
├── management  # 脚本
├── middlewares.py  # 中间件
├── migrations  # 数据库migrate
├── models.py  # 数据表模型
├── static  # 静态文件
├── templates  # 模板文件里面有pc、mobile、xadmin三个文件夹
├── tests.py
├── urls.py  # url路径
└── views.py  # views

```

# 提取命令

python manage_local.py makemessages -l en -l zh-hans -l zh-hant -l th --no-location -v3 --keep-pot \
--ignore=xadmin/* --ignore=config/* --ignore=jarvis/* --ignore=restful/* --ignore=django/* \
--ignore=xadmin/* --ignore=common/* --ignore=i18n/*  --settings=config.local

python manage_local.py makemessages -l ko_KR --no-location -v3 --keep-pot \
--ignore=xadmin/* --ignore=config/* --ignore=jarvis/* --ignore=restful/* --ignore=django/* \
--ignore=xadmin/* --ignore=common/* --ignore=i18n/*  --settings=config.local

python manage_local.py makemessages -l zh_Hant --no-location -v3 --keep-pot \
--ignore=xadmin/* --ignore=config/* --ignore=jarvis/* --ignore=restful/* --ignore=django/* \
--ignore=xadmin/* --ignore=common/* --ignore=i18n/*  --settings=config.local

# 编译
python manage.py compilemessages --settings=config.local

#python manage.py compilemessages --settings=config.local

# 启动
python manage_local.py runserver



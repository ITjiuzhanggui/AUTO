#!/usr/bin/env python
import time
import os
from conf import ConfManagement
from core.defaultslog import *
from core.clearlogs import *
from core.statusDef import *
from core.statusCle import *

auto_path = ConfManagement().get_ini("AUTOMATEDLOGPARSING")

date = time.strftime("%Y-%m-%d", time.localtime()).replace(' ', ':').replace(':', ':')

CURPATH = os.path.dirname(os.path.realpath(__file__)) + "/%s" % date
os.makedirs(CURPATH, exist_ok=True)
os.system("cp 1.sh %s/" % auto_path)


def get_log_update(cmd, logs_patg):
    for i in range(1):
        os.system("{} > {}/{}.logs 2>&1 ".format(
            cmd, logs_patg, time.strftime( \
                "%Y-%m-%d-%H:%M:%S", \
                time.localtime()).replace(' ', ':'). \
                replace(':', ':'))
        )


path = os.path.join(CURPATH, "update")
os.makedirs(path, exist_ok=True)
make_path = auto_path + "/1.sh"
make_path += " make update"
get_log_update(make_path, path)


def get_log_status(cmd, logs_patg):
    for i in range(1):
        os.system("{} > {}/{}.logs 2>&1 ".format(
            cmd, logs_patg, time.strftime( \
                "%Y-%m-%d-%H:%M:%S", \
                time.localtime()).replace(' ', ':'). \
                replace(':', ':'))
        )


path = os.path.join(CURPATH, "status_log")
os.makedirs(path, exist_ok=True)
make_path = auto_path + '/1.sh'
make_path += " make status"
get_log_status(make_path, path)
test_cmd = ["make httpd", "make nginx", ""]


def get_log_test(cmd, logs_patg):
    for i in range(1):
        os.system("{} > {}/{}.logs 2>&1 ".format(
            cmd, logs_patg, time.strftime( \
                "%Y-%m-%d-%H:%M:%S", \
                time.localtime()).replace(' ', ':'). \
                replace(':', ':'))
        )


def anlies():
    list = os.listdir(CURPATH)
    if "status_log" in list:
        logs = os.path.join(CURPATH, "status_log")
        for i in os.listdir(logs):
            curl_path = os.path.join(logs, i)
            ConfManagement().set_ini(session="STATUS_LOG_PATH", value=curl_path)
            StaDefHttpd().serialization()
            StaClrHttpd().serialization()
            StaDefNginx().serialization()
            StaClrNginx().serialization()
            # StaDefMemcached().serialization()
            # StaClrMemcached().serialization()
            # StaDefRedis().serialization()
            # StaClrRedis().serialization()
            # StaDefPhp().serialization()
            # StaClrPhp().serialization()
            # StaDefPython().serialization()
            # StaClrPython().serialization()
            # StaDefGolang().serialization()
            # StaClrGolang().serialization()
            # StaDefNode().serialization()
            # StaClrNode().serialization()

    # if "update_log" in list:
    #     for i in os.path.join(CURPATH, "update_log"):
    #         pass

    if "test_log" in list:
        logs = os.path.join(CURPATH, "test_log")
        for i in os.listdir(logs):
            log = os.path.join(logs, i)
            print(log)
            for curl_path in os.listdir(log):
                p = os.path.join(log, curl_path)
                ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                DefHttpd().serialization()
                ClrHttpd().serialization()
                DefNginx().serialization()
                ClrNginx().serialization()
                # DefMemcached.serialization()
                # ClrMemcached().serialization()
                # DefRedis().serialization()
                # ClrRedis().serialization()
                # DefPhp().serialization()
                # ClrPhp().serialization()
                # DefPython.serialization()
                # ClrPython().serialization()
                # DefGoalng().serialization()
                # ClrGoalng().serialization()
                # DefNode().serialization()
                # ClrNode().serialization()


for i in test_cmd:
    path = os.path.join(CURPATH, "test_log")
    path = os.path.join(path, i.split(' ')[-1])
    os.makedirs(path, exist_ok=True)
    make_path = auto_path + '/1.sh'
    make_path += " %s" % i
    get_log_test(make_path, path)
anlies()

sh = auto_path + '/1.sh'
os.system("rm %s" % sh)

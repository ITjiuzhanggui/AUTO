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

JSON_PATH = os.path.join(CURPATH, "json")
os.makedirs(JSON_PATH, exist_ok=True)
JSON_STATUS_PATH = os.path.join(JSON_PATH, "status")
JSON_TEST_PATH = os.path.join(JSON_PATH, "test")
os.makedirs(JSON_TEST_PATH, exist_ok=True)
os.makedirs(JSON_STATUS_PATH, exist_ok=True)
os.system("chmod a+x 1.sh")
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
make_path += "%s make update" % auto_path
# get_log_update(make_path, path)


def get_log_status(cmd, logs_patg):
    print(cmd)
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
make_path += " %s make status" % auto_path
# get_log_status(make_path, path)


test_cmd = ["make httpd", "make nginx"]


def get_log_test(cmd, logs_patg):
    print(cmd)
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
            StaDefMemcached().serialization()
            StaClrMemcached().serialization()
            StaDefRedis().serialization()
            StaClrRedis().serialization()
            StaDefPhp().serialization()
            StaClrPhp().serialization()
            StaDefPython().serialization()
            StaClrPython().serialization()
            StaDefGolang().serialization()
            StaClrGolang().serialization()
            StaDefNode().serialization()
            StaClrNode().serialization()
            StaDefOpenjdk().serialization()
            StaClrOpenjdk().serialization()
            StaDefRuby().serialization()
            StaClrRuby().serialization()

    if "test_log" in list:
        logs = os.path.join(CURPATH, "test_log")
        for i in os.listdir(logs):
            log = os.path.join(logs, i)

            if "httpd" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefHttpd().serialization()
                    ClrHttpd().serialization()

            if "nginx" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefNginx().serialization()
                    ClrNginx().serialization()

            if "memcached" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefMemcached.serialization()
                    ClrMemcached().serialization()

            if "redis" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefRedis().serialization()
                    ClrRedis().serialization()

            if "php" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefPhp().serialization()
                    ClrPhp().serialization()

            if "python" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefPython().serialization()
                    ClrPython().serialization()

            if "golang" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefGoalng().serialization()
                    ClrGoalng().serialization()

            if "node" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefNode().serialization()
                    ClrNode().serialization()

            if "openjdk" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefOpenjdk().serialization()
                    ClrOpenjdk().serialization()

            if "ruby" in log:
                for files in os.listdir(log):
                    p = os.path.join(log, files)
                    ConfManagement().set_ini(session="TEST_LOG_PATH", value=p)
                    DefRuby().serialization()
                    ClrRuby().serialization()

        os.system("cp data.json %s" % (JSON_TEST_PATH + "/%d.json" % int(time.time())))
        os.system("cp ini_data.json data.json")


for i in test_cmd:
    path = os.path.join(CURPATH, "test_log")
    path = os.path.join(path, i.split(' ')[-1])
    os.makedirs(path, exist_ok=True)
    make_path = auto_path + '/1.sh'
    make_path += " {} {} ".format(auto_path, i)
    get_log_test(make_path, path)

anlies()

sh = auto_path + '/1.sh'
os.system("rm %s" % sh)

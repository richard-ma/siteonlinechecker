#!/usr/bin/env bash
# -*- coding: utf-8 -*-
echo "-------------------------------------------"
echo "                开始安装                   "
echo "-------------------------------------------"

echo "正在安装依赖..."
pip install -r requirements.txt

if [ ! -f "config.cfg" ]; then
    echo "正在创建配置文件config.cfg..."
    cp config.cfg.sample config.cfg
else
    echo "[skip]配置文件已存在，不再创建"
fi

if [ ! -f "targets.data" ]; then
    echo "正在创建检测数据文件targets.data..."
    touch targets.data
else
    echo "[skip]数据文件已存在，不再创建"
fi

echo "-------------------------------------------"
echo "                开始测试                   "
echo "-------------------------------------------"

pytest

echo "-------------------------------------------"
echo "                配置说明                   "
echo "-------------------------------------------"

echo "1. 请先填写config.cfg文件中的相关配置参数。"
echo "2. 需要监测的网站地址每行一个，写入targets.data文件中，例如："
echo "http://www.baidu.com"

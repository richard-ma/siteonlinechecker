#!/usr/bin/env bash
# -*- coding: utf-8 -*-
echo "开始安装"

echo "正在安装依赖..."
pip install -r requirements.txt

echo "正在创建配置文件config.cfg..."
cp config.cfg.sample config.cfg

echo "正在创建检测数据文件targets.data..."
touch targets.data

echo "安装完成，请先填写config.cfg文件中的相关配置参数。"
echo "需要监测的网站地址每行一个，写入targets.data文件中，例如："
echo "http://www.baidu.com"

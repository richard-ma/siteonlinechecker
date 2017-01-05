# siteonlinechecker

[![Build Status](https://travis-ci.org/richard-ma/siteonlinechecker.svg?branch=master)](https://travis-ci.org/richard-ma/siteonlinechecker)
[![Code Climate](https://codeclimate.com/github/richard-ma/siteonlinechecker/badges/gpa.svg)](https://codeclimate.com/github/richard-ma/siteonlinechecker)

## 安装

### 系统需求

* Python 2.6~2.7
* pip

### 安装过程

本软件使用一次安装脚本安装，直接执行install.sh即可完成安装过程。

* chmod +x install.sh
* ./install.sh

### 安装后的配置

* 填写config.cfg中defalut和smtp段中的相应参数，可参考配置文件一节
* 填写targets.data中的检测站点域名，可参考检测站点列表一节

### 运行和停止

本软件使用siteonlinechecker.sh脚本控制软件的开启和停止监控

* ./siteonlinechecker.sh start 开始监控
* ./siteonlinechecker.sh stop  停止监控

### 测试运行

如需要测试运行本软件，可直接执行siteonlinechecker/scheduler.py文件

* python ./siteonlinechecker/scheduler.py

所有运行信息都会直接打印在屏幕上

## 配置文件

### 软件配置文件config.cfg
* default段是基本配置段
* smtp段是有关发送邮件的smtp服务器配置

### 检测站点列表targets.data
域名每行一个，请记得加上http或https开头，例如：
http://baidu.com
http://www.163.com

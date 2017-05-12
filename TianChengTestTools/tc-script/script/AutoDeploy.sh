#! /bin/bash

ip="192.168.18.84"
username="tester"
bResult=1

#部署到远程主机
funJustDeploy(){
    echo "["`date "+%Y-%m-%d %H:%M:%S"`"] 拷贝${1}到${ip}:/tmp/目录下"
    scp -rp ${1} "${username}@${ip}:/tmp"                                                       #将制定的程序拷贝到服务器tmp目录下
    
    ssh -p 22 "${username}@"${ip}  << deployapp
    echo "["`date "+%Y-%m-%d %H:%M:%S"`"] 执行部署脚本..."
    . /opt/tiancheng/AUTOTEST/script/deploy.sh ${2} ${3}                                                #调用部署程序的脚本
    #. /opt/tiancheng/AUTOTEST/script/test.sh ${2} ${3}                                                   #调用部署程序的脚本
deployapp

}

funJustDeploy ${1} ${2} ${3}

bResult=`ssh "${username}@"${ip} "cat /opt/tiancheng/AUTOTEST/script/result"`
if [ "${bResult##*=}"x == "0"x ];then
   echo "bResult=0"
   exit -1
else
    echo "bResult="${bResult##*=}
fi

#!/bin/sh


###################################################################
#  获取配置文件中的变量
check_deploy_path()
{
# 创建天秤系统的svn code路径
if [ ! -d $svn_checkout_path ]; then
	mkdir -p $svn_checkout_path
fi
}

##################################################################o#
##  读取配置文件并且设置参数
export_key_value()
{
    input=$1
    cat $input | grep -Ev "^$|^#"  | while read line;
    do
        if [ "X$line" != "X" ]; then
            key=${line%=*}
            value=${line#*=}

            echo "export $key=$value"

            [ "X$key" != "X" ] && [ "X$value" != "X" ] && export $key=$value 

        fi
    done 
}

#export_key_value $DEPLOY_CONFIG_FILE
help()
{
        echo ""
        echo "[Warning]#################################################$1"
        echo "Please input at lease 2 parameters!"
        echo "Usage: $0 checkout|update CONFIG_NAME "
        echo ""
}

source_parameter()
{
        if [ "${DEPLOY_CONFIG_FILE%/*}" != "$DEPLOY_CONFIG_FILE" ]; then
                source ${DEPLOY_CONFIG_FILE%/*}/./${DEPLOY_CONFIG_FILE##*/}
        else
                source ./$DEPLOY_CONFIG_FILE
        fi

        source ~/.bash_profile
}
##################################################################
# svn checkout http://192.168.18.14/svn/niiwoo/TianChengSystem/code/
tc_svn_checkout()
{
	for project_name in ${TC_SVN_PROJECT_LISTS[@]}
	do
		echo "##########start checkout $project_name##########"
		svn checkout $SVN_SERVER_URL/$project_name $svn_checkout_path/$project_name
		echo "##########end checkout $project_name##########"
	done
}
##################################################################
#  获取更新svn所有
main()
{
	check_deploy_path
	case $1 in
	checkout)
		source_parameter
		tc_svn_checkout
	;;

	update)
		source_parameter
		tc_svn_update
	;;

	*)
		echo "First Parameter must between in (checkout | update)"
		help $LINENO
	;;
        esac
}

SVN_CMD=$1
DEPLOY_CONFIG_FILE=$2

if [ $# -lt 2 ];then
	help $LINENO
	exit
fi

svn_checkout_path=$HOME/workspace/TianChengSystem/code

############################# [main] ##############################
main $SVN_CMD $DEPLOY_CONFIG_FILE

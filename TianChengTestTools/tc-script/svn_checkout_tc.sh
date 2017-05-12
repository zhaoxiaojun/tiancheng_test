#!/bin/sh

tc_svn_update()
{
	project_name=$1
        echo $TC_PROJECT/$project_name

        cd $TC_PROJECT/$project_name
        svn update .
        cd -
}



###################################################################
tc_svn_update $1

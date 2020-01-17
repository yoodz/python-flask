# -*- coding: utf-8 -*-
import logging
import subprocess

from logger import *

logger = logging.getLogger("logger")

def execute_shell_command(command):
    return subprocess.call(command, shell=True)


def scp_util(local_path, origin_path):
    command = 'scp %s %s'%(local_path, origin_path)
    logger.info('执行scp_util的操作,命令为%s' % (command))
    return execute_shell_command(command)

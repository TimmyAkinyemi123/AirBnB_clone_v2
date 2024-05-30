#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path
import re
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ["100.25.167.169", "100.25.196.96"]
env.key_filename = "~/.ssh/school"


def do_pack():
    """Creates an archive of the web_static directory"""
    local("mkdir -p versions")
    dt = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{dt}.tgz'
    result = local(f'tar -cvzf {archive_path} web_static')
    if result.failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """Deploys an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        name_no_ext = file_name.split(".")[0]
        release_path = f"/data/web_static/releases/{name_no_ext}"
        
        put(archive_path, '/tmp/')
        sudo(f'mkdir -p {release_path}')
        sudo(f'tar -xzf /tmp/{file_name} -C {release_path}')
        sudo(f'rm /tmp/{file_name}')
        sudo(f'mv {release_path}/web_static/* {release_path}')
        sudo('rm -rf /data/web_static/current')
        sudo(f'ln -s {release_path} /data/web_static/current')
        return True
    except Exception:
        return False


def deploy():
    """Creates and deploys an archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

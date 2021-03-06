"""
Created on Nov 18, 2016

@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)
"""

from __future__ import absolute_import
import os
import shutil

#============================
# Django imports
#----------------------------
from django.conf import settings


class FileHandler(object):

    """
    Handles all the file/dir operations.
    """

    def __init__(self):
        """initialize."""
        self.wd_root = settings.WORKING_DIR_ROOT
        self.rd_root = settings.RESULTS_DIR_ROOT

    @staticmethod
    def rename(src, dst):
        """recursive dir/file renaming from src to dst."""
        os.renames(src, dst)

    @staticmethod
    def move(src, dst):
        """move dir/file from src to dst."""
        shutil.move(src, dst)

    def make_tmp_wd(self, dir_name):
        """make a temporary working dir."""
        print "making temporary working directory ..."
        path = os.path.join(self.wd_root, dir_name)
        os.makedirs(path)

    def make_tmp_rd(self, dir_name):
        """make a temporary results dir."""
        pass

    def copy_wf(self, wf_name, wf_version, dir_name):
        """copy the workflow in the given directory."""
        pass

    def rmdir(self, dirpath):
        """remove directory."""
        pass

    def clone(self, repo, dpath):
        """clone the given repository in the destination path."""
        pass

    def create_virtenv(self, reqs):
        """create a python virtualenv usgin the given requirements."""
        pass

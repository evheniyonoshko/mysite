# -*- coding: utf-8 -*-

import os
import uuid

__author__ = 'Yevhenii Onoshko'


def generate_uuid_file_path(filename):
    """
    Helper tool to generate unique path for files
    """
    ext = filename.split('.')[-1]
    filename = '{filename}.{ext}'.format(filename=uuid.uuid4(), ext=ext)
    return "{}/{}/{}".format(filename[:1], filename[2:3], filename)

def get_document_upload_path(instance, filename):
    return '{}'.format(generate_uuid_file_path(filename))

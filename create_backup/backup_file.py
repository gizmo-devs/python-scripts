import utils
import os
from shutil import copyfile
import datetime


def gen_target_filename(system_cfg):
    if system_cfg['add_timestamp']:
        ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename_str = ts + "_" + system['backup_file_prefix'] + system['backup_file']
    else:
        filename_str = system['backup_file_prefix'] + system['backup_file']
    return filename_str


for system in utils.cfg['systems']:
    print("Processing System: " + system['name'])

    source_file_path = os.path.join(system['location'], system['backup_file'])
    if not utils.path_exists(source_file_path):
        print("Cannot find source file to back up: " + source_file_path)
        exit()

    backup_file_path = os.path.join(system['location'], system['backup_location'])
    if not utils.path_exists(backup_file_path):
        print("Folder for backups doesnt exits: " + backup_file_path + ". Creating")
        utils.create_backup_loc(backup_file_path)

    target_filename = gen_target_filename(system)

    # print(target_filename)

    target_file = os.path.join(backup_file_path, target_filename)

    try:
        copyfile(source_file_path, target_file)
    except IOError:
        print("IOError, Cannot write to folder: " + backup_file_path)

    print("File created {}/{}".format(system['backup_location'],target_filename))

    print("Finished processing: " + system['name'])
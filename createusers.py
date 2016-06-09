# -*- coding: utf-8 -*-
# Copyright 2016 Thomas Saliou - Abstrium SAS <team (at) pydio.com>

import subprocess
import argparse
import sys

def create(user, password, nb, verbose=None):
    created = 0
    for Id in range(nb):
        # create workspaces php cmd.php -u=admin -p=password -r=ajxp_conf -a=edit --sub_action=create_repository --DISPLAY=test2 --DRIVER=fs --DRIVER_OPTION_CREATE=true --DRIVER_OPTION_PATH=/path/data/test2
        cmd = "php cmd.php -u=" + user + " -p=" + password + \
            " -r=ajxp_conf -a=edit --sub_action=create_user --new_user_login=user" + str(Id) + " --new_user_pwd=user000xxx\n"
        out = ""
        try:
            if verbose:
                print(cmd)
            out = subprocess.check_output(cmd, shell=True)
            if not out.find('<message type="SUCCESS">'):
                print(out)
                print("You need to enable ioncube for php-cli")
                return -1
            else:
                created += 1
        except:
            if out.find("xist") > -1:
                # user exists move on
                pass
            else:
                # connection issue? try again
                Id -= 1
    return created

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Pydio batch action')
    parser.add_argument('-u', '--user', help="Admin user name", type=unicode, required=True)
    parser.add_argument('-p', '--password', help="Admin password", type=unicode, required=True)
    parser.add_argument('-n', '--nb', help="Number of users to add", type=unicode, default=9)
    parser.add_argument('-v', '--verbose', help="More info", action="store_true")
    args, _ = parser.parse_known_args()
    done = create(args.user, args.password, args.nb, args.verbose)
    if args.verbose:
        print("Created {} users".format(done))


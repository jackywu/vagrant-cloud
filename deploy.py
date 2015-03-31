#!/usr/bin/env python
# encoding: utf-8
# vim:fileencoding=utf-8:ts=4:sw=4:sts=4
import commands

def get_os_version():
    with open('/etc/system-release-cpe') as fp:
        for line in fp:
            if line.strip() == '':
                continue
            else:
                segments = line.strip.split(':')
                for seg in segments:
                    if seg.isdigit(): return seg

def main():
    # install puppet
    version = get_os_version()
    cmd = ''' rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-%s.noarch.rpm ''' % version
    print commands.getstatusoutput(cmd)

    # install virtualbox module of puppet

    # puppet apply install virtualbox

    pass

if __name__ == '__main__':
    main()



#!/usr/bin/env python
# encoding: utf-8
# vim:fileencoding=utf-8:ts=4:sw=4:sts=4
import commands

def exec_cmd(cmd):
    status, output = commands.getstatusoutput(cmd)
    print 'status: %s' % status
    print output

def get_os_version():
    with open('/etc/system-release-cpe') as fp:
        for line in fp:
            if line.strip() == '':
                continue
            else:
                segments = line.strip().split(':')
                for seg in segments:
                    if seg.isdigit(): return seg

def main():
    # install puppet
    version = get_os_version()
    cmd = ''' rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-%s.noarch.rpm ''' % version
    exec_cmd(cmd)

    # install virtualbox module of puppet
    cmd = ''' puppet module install danzilio-virtualbox '''
    exec_cmd(cmd)

    # puppet apply install virtualbox
    cmd = ''' puppet apply site.pp --modulepath=/etc/puppet/modules/:./modules '''
    exec_cmd(cmd)

    pass

if __name__ == '__main__':
    main()
    #print get_os_version()



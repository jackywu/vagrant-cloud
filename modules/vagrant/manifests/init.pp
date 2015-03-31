class vagrant {
  
  package {'vagrant':
    provider      => 'rpm',
    source        => '../files/vagrant_1.7.2_x86_64.rpm',
    ensure        => installed,
    allow_virtual => true,
  }

}

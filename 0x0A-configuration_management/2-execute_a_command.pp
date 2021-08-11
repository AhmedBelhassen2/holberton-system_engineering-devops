# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill-killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
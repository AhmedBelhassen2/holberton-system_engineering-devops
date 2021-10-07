# Fixing issue with multiple open files for specific user
exec{ 'change-os-configuration-for-holberton-user':
    command => 'echo "" > /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}

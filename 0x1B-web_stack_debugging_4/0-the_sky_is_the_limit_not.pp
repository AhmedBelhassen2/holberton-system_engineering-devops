# Fixing issue with multiple open files in nginx, changing Ulimit
exec{ 'fix--for-nginx':
    command => 'echo "ULIMIT=\"-n 2000\"" > /etc/default/nginx && /etc/init.d/nginx restart',
    path    => '/usr/local/bin/:/bin/',
}

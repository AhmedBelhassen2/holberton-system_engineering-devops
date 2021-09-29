#fix it and then automate it using Puppet
exec {'debug':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}

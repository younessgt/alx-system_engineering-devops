exec {'correct_php':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => ["/bin", "/usr/bin"],
  onlyif  => "grep -q class-wp-locale.phpp /var/www/html/wp-settings.php",
}

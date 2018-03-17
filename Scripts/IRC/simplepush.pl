use strict;
use warnings;
use Irssi;
use vars qw($VERSION %IRSSI);

$id = ""
$pw = ""
$salt = ""
$title = "PM From:"

$VERSION = "1.0";
%IRSSI = (
    authors     => 'Ainsey11',
    name        => 'simplepush.pl',
    description => 'Send a message about Simplepush.io when you receive a new private message.',
);
 
sub tmsg {
    my ($server,$nick) = @_;
    system("bash ~/code/.irssi/send-encrypted.sh -k $id -p $pw -s $salt -e IRC -t $title  -m $nick");
    }
}
Irssi::signal_add_last('message private', 'tmsg');

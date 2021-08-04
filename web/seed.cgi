#!/usr/bin/perl

use CGI qw/:standard/;

@ignore = (
"CONTENT_TYPE",
"DOCUMENT_ROOT",
"GATEWAY_INTERFACE",
"HTTP_ACCEPT_CHARSET",
"HTTP_ACCEPT_ENCODING",
"HTTP_ACCEPT",
"HTTP_CACHE_CONTROL",
"HTTP_CONNECTION",
"HTTP_HOST",
"HTTP_PRAGMA",
"HTTP_VIA",
"HTTP_X_FORWARDED_FOR",
"PATH",
"REQUEST_URI",
"SCRIPT_FILENAME",
"SCRIPT_NAME",
"SERVER_ADDR",
"SERVER_ADMIN",
"SERVER_NAME",
"SERVER_PORT",
"SERVER_PROTOCOL",
"SERVER_SIGNATURE",
"SERVER_SOFTWARE");

foreach $ignore (@ignore) {
   $ignore{$ignore} = 1;
}


$query = new CGI();

$g = $query->param("POSTDATA");
$g =~ s/[^ -~]//g;
#$g =~ s/^(.{36}).*/$1/g;
$g = substr($g, 0, 36);
$g =~ s/[^-0-9a-fA-F]//g; # sanitize!

if (!length($g)) {
   $g = ".null";
}

if ($query->param("SHARD") eq "Testing") {
   $g = $g . "-t";
   $ENV{"grid"} = "aditi";
}

open FILE, ">gates/$g";

foreach $var (sort(keys(%ENV))) {
   if (!defined($ignore{$var})) {
      print FILE "$var: $ENV{$var}\n";
   }
}

foreach $param (sort($query->param)) {
      print FILE $param . ": " . $query->param($param) . "\n";
}

print FILE "TIMESTAMP: " . (0+time()) . "\n";

if (! -e "birth/$g") {
   print FILE "BORN: " . (0+time()) . "\n";
}
else {
   ($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,
            $atime,$mtime,$ctime,$blksize,$blocks) = stat "birth/$g";
   $time = $atime;
   if ($mtime < $time) {
      $time = $mtime;
   }
   if ($ctime < $time) {
      $time = $ctime;
   }
   print FILE "BORN: " . $time . "\n";
}

print FILE "rev: v400\n";

close FILE;

if (! -e "birth/$g") {
   `cp gates/$g birth/$g`;
}

print "Content-type: text/plain\n\n";

open FILE, ".lastpost";
while (<FILE>) {
   print $_;
}
close FILE;

#open FILE, "ls gates|";
#@list = <FILE>;
#close FILE;
#
#print $list[int(rand($#list+2))];

open FILE, ">.lastpost";
print FILE $query->param("POSTDATA");
close FILE;


#!/usr/bin/perl

open FILE, "ls gates|";
@list = <FILE>;
close FILE;

$now = time();

foreach $item (@list) {
   chomp $item;
   ($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,
                          $atime,$mtime,$ctime,$blksize,$blocks)
                                = stat("gates/$item");
   $atime = $now - $atime;
   $mtime = $now - $mtime;
   $ctime = $now - $ctime;
   
   if ($mtime > (60*60)) {
      `mv gates/$item grave`;
   }
   elsif (-e "grave/$item") {
      `rm -f grave/$item`;
   }
}

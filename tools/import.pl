#!/usr/bin/perl

$now = localtime();

open FILE, "<tools/untitled.xml";
@xml = <FILE>;
close FILE;

open FILE, "ls bin/|";
@ls = <FILE>;
close FILE;

for ($i = 0; $i < $#xml; $i++) {
   if ($xml[$i] =~ /<key>inventory<\/key>/) {
      $inventory_start = $i;
   }
   if (defined($inventory_start) && !defined($inventory_end) && $xml[$i] =~ /<\/array>/) {
      $inventory_end = $i;
   }
   $xml[$i] =~ s/NAME_HERE/chord9 $now/g;
}

for ($i = 0; $i <= ($inventory_start + 1); $i++) {
   print $xml[$i];
}
foreach $file (@ls) {
   chomp $file;
   open FILE, "<bin/$file";
   @lsl = <FILE>;
   close FILE;

   for ($i = 0; $i < $#lsl; $i++) {
      if ($lsl[$i] =~ /SOFTWARE_REV [a-f0-9]{32}/) {
         $tmp = $lsl[$i];
         $tmp =~ s/([a-f0-9]{32})/$rev = $1/ge;
      }
   }
   $tmp = $rev;
   $tmp =~ s/([a-f0-9]{8})([a-f0-9]{4})([a-f0-9]{4})([a-f0-9]{4})([a-f0-9]{12})/$rev="$1-$2-$3-$4-$5"/ge;

   print "               <map>\n";
   print "                   <key>desc</key>\n";
   print "                   <string>2011-06-14 22:39:53 lsl2 script</string>\n";
   print "                   <key>item_id</key>\n";
   print "                   <string>$rev</string>\n";
   print "                   <key>name</key>\n";
   print "                   <string>}$file</string>\n";
   print "                   <key>type</key>\n";
   print "                   <string>lsltext</string>\n";
   print "               </map>\n";

   `cp bin/$file import/import_assets/$rev.lsltext`;

}
for ($i = $inventory_end; $i <= $#xml; $i++) {
   print $xml[$i];
}

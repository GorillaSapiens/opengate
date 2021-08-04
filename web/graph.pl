#!/usr/bin/perl

@colors = (
      "white",
      "red",
      "orange",
      "yellow",
      "green",
      "cyan",
      "blue",
      "indigo",
      "violet",
      "lightgray",
      "gray",
      "darkgray",
       );

$len=1;
$fgcolor="white";
$bgcolor="black";

sub c($$$) {
   my $a = shift @_;
   my $b = shift @_;
   my $c = shift @_;

   if (!length($a) || !length($b)) {
      return;
   }

   if (!defined($hash{$a})) {
      $hash{$a} = 0;
   }

   if (!defined($hash{$b})) {
      $hash{$b} = 0;
   }

   if (!length($c)) {
      $c = "black";
   }

   $links{"$a:$b"} = $c;
#print  "   n$a -> n$b [ color=\"$c\", len=$len ];\n";
}

sub n($) {
   my $a = shift @_;

   $a =~ s/-//g;
   $a =~ s/@.*//g;

   $lab = $a;
   $lab =~ s/^(....).*/$1/ge;

   if (!length($a)) {
      return;
   }

   $hash{$a} = 1;

   print  "   n$a [ label=\"x$lab\", color=$fgcolor, fontcolor=$fgcolor ];\n";
}

sub closure() {
   foreach $a (keys(%hash)) {
      $lab = $a;
      $lab =~ s/^(....).*/$1/ge;
      if (!$hash{$a}) {
         print  "   n$a [ label=\"x$lab\", color=$fgcolor, fontcolor=red ];\n";
      }
   }
}

open FILE, "ls gates|";
@list = <FILE>;
close FILE;

print  "digraph foo {\n";

foreach $file (@list) {
   chomp $file;

   open FILE, "gates/$file";
   @cont = <FILE>;
   close FILE;

   foreach $line (@cont) {
      chomp $line;
      if ($line =~ /^POSTDATA/) {
         $line =~ s/POSTDATA: //g;
#         print "# $line\n";
         @conns = split /\|/, $line;
#print STDERR "$#conns\n";
         foreach $conn (@conns) {
            $conn = substr($conn, 0, 35);
            $conn =~ s/-//g;
         }
         $me = shift @conns;
         n($me);
         $pre = shift @conns;
         c($me, $pre, 0);

#print "$me\n";
#print join(",", @conns) . "\n";

         while (@conns[0] ne $me) {
            $tmp = shift @conns;
            push @conns, $tmp;
         }
         shift @conns;

         $i = 1;
         foreach $conn (@conns) {
            c($me, $conn, $i++);
         }
      }
   }
}

closure();

print "graph [ color=$fgcolor, bgcolor=$bgcolor ]\n";

@keys = sort(keys(%hash));
$n = $#keys+1;
$i = 0;

$r = ($#keys + 1) * 15;

foreach $key (@keys) {
   $x = ($r/2) + int($r*cos(2*3.141592653587*$i/$n));
   $y = ($r/2) + int($r*sin(2*3.141592653587*$i/$n));
   print "n$key [ pos=\"$x,$y\" ];\n";
   $i++;
}

foreach $key (keys(%links)) {
   ($a, $b) = split /:/, $key;
   $c = $links{$key};

   @all = sort(keys(%hash));
   while ($all[0] ne $a) {
      $tmp = shift @all;
      push @all, $tmp;
   }
#   shift @all;
#print "###\n";
#print "a:$a\n";
#print "all:\n" . join("\n", @all) . "\n";
#print "b:$b\n";
#print "c:$c\n";
#print "###\n";
   if ($all[1 << ($c-1)] ne $b) {
      $color = $colors[$c];
   }
   else {
      $color = "#333333";
   }

   print  "   n$a -> n$b [ color=\"$color\", len=$len ];\n";
}
print @pass2;
print  "}\n";

# # # # # # # # # # # # ./graph.pl > foo.dot; circo -Tpng -o foo.png foo.dot


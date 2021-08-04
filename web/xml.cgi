#!/usr/bin/perl

############# config

$timeout = 4*60*60;

############# symbols

@symbols = ();

for ($i = 0x2648; $i <= 0x2653; $i++) {
   push @symbols, "&#x" . sprintf("%x;", $i);
}
for ($i = 0x263C; $i <= 0x2647; $i++) {
   push @symbols, "&#x" . sprintf("%x;", $i);
}

sub sevensymbols($) {
   my $arg = shift @_;
   my @isymbols = @symbols;
   
   $arg =~ s/^(......).*/$1/g;
   $arg = hex($arg);

   my $i;
   my $rem;
   my $ret = "";
   my $foo;
   my $bar;

   for ($i = 0; $i < 7; $i++) {
      $rem = $arg % 11;
      $arg = int($arg/11);
      $foo = $isymbols[$rem];
      $ret = $ret . $foo;
      $bar = join ":", @isymbols;
      $bar =~ s/$foo//g;
      $bar =~ s/::/:/g;
      $bar =~ s/^://g;
      @isymbols = split /:/, $bar;
   }
   return $ret;
}

sub sevenalpha($) {
   my $arg = shift @_;
   my @isymbols = @symbols;
   my @isymbols = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
   
   $arg =~ s/^(......).*/$1/g;
   $arg = hex($arg);

   my $i;
   my $rem;
   my $ret = "";
   my $foo;
   my $bar;

   for ($i = 0; $i < 7; $i++) {
      $rem = $arg % 11;
      $arg = int($arg/11);
      $foo = $isymbols[$rem];
      $ret = $ret . $foo;
      $bar = join ":", @isymbols;
      $bar =~ s/$foo//g;
      $bar =~ s/::/:/g;
      $bar =~ s/^://g;
      @isymbols = split /:/, $bar;
   }
   return $ret;
}

############# begin main program

use CGI qw/:standard/;

$query = new CGI();

print "Content-type: text/xml\n\n";

$count = 0;

### begin old stuff
@keys = readpipe "ls gates";
foreach $key (@keys) {
   chomp $key;
   @bar = readpipe "cat gates/$key";
   foreach $bar (@bar) {
      chomp $bar;
   }
   $ref = { };
   for ($i = 0; $i < @bar; $i += 2) {
      $$ref{$bar[$i]} = $bar[$i+1];
   }
   $$ref{"address"} = sevensymbols($key);
   $gates{$key} = $ref;
   $count++;
}
### end old stuff

### BEGIN new stuff
$dirname = "/home/opengate/public_html/chord9/gates";
if (defined(param('dirname'))) {
   $dirname = param('dirname');
   $dirname =~ s/[^-a-zA-Z0-9]//g;
}

@keys = readpipe "ls $dirname";
foreach $key (@keys) {
   chomp $key;
   @bar = readpipe "cat $dirname/$key";
   foreach $bar (@bar) {
      chomp $bar;
   }
   $ref = { };
   for ($i = 0; $i < @bar; $i ++) {
      ($l,$r) = split /: /, $bar[$i];
      $l =~ s/HTTP_X_SECONDLIFE_//g;
      if ($l eq "POSTDATA") {
         $r =~ s/\|/<BR>/g;
      }
      $$ref{$l} = $r;
   }
   $$ref{"rev"} = "v400";
   $$ref{"grid"} = "open9";
#$$ref{"OBJECT_DESC"} = $$ref{"QUERY_STRING"};
#$$ref{"OBJECT_DESC"} =~ s/desc=//g;
   if (defined($$ref{"BORN"}) && defined($$ref{"TIMESTAMP"})) {
      $$ref{"AGE"} = ((0+$$ref{"TIMESTAMP"}) - (0+$$ref{"BORN"})) / (60*60*24);
   }
   foreach $kv (split /\&/, $$ref{"QUERY_STRING"}) {
      ($k, $v) = split /=/, $kv;
      $v =~ s/%(..)/chr(hex($1))/ge;
      $$ref{$k} = $v;
   }
   $gates{$key} = $ref;
   $count++;
}
### END new stuff

$sort = $query->param('sort');
if (!defined($sort)) {
   $sort = "REGION";
}

$select = $query->param('select');

sub bywhatever {
   my $refa = $gates{$a};
   my $refb = $gates{$b};

   my @whatever = split /,/, $sort;

   foreach my $whatever (@whatever) {
      my $invert = 0;
      my $numeric = 0;

      if ($whatever =~ /^-/) {
         $invert = 0;
         $numeric = 1;
         $whatever =~ s/^.//g;
      }
      elsif ($whatever =~ /^\+/) {
         $invert = 1;
         $numeric = 1;
         $whatever =~ s/^.//g;
      }
      elsif ($whatever =~ /^!/) {
         $invert = 1;
         $whatever =~ s/^.//g;
      }

      my $ret;
      
      if ($numeric) {
         $ret = $$refa{$whatever} <=> $$refb{$whatever};
      }
      else {
         $ret = $$refa{$whatever} cmp $$refb{$whatever};
      }

      if ($invert) {
         $ret = - $ret;
      }
      if ($ret != 0) {
         return $ret;
      }
   }

   return $a cmp $b;
}

@sortedkeys = sort bywhatever keys(%gates);

print "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n";
print "<gates network=\"open2\">\n";

foreach $key(@sortedkeys) {
   $ref = $gates{$key};

   if (defined($select) && $select == 1) {
      if (!($$ref{"HTTP_USER_AGENT"} =~ /1\.27/)) {
         next;
      }
   }

   print "   <gate id=\"$key\">\n";

   foreach my $subkey (sort(keys(%$ref))) {
      if ($subkey ne "===") {
         my $subval = $$ref{$subkey};
         $subval =~ s/\&/\&amp;/g;
         $subval =~ s/\</\&lt;/g;
         $subval =~ s/\>/\&gt;/g;
         print "      <$subkey>$subval</$subkey>\n";
      }
   }

   print "      <address>\n";
   print "         <symbols>";
   $alias = sevensymbols($key);
   $alias =~ s/\&/\&amp;/g;
   $alias =~ s/\</\&lt;/g;
   $alias =~ s/\>/\&gt;/g;
   print "$alias</symbols>\n";
   print "         <alpha>".sevenalpha($key)."</alpha>\n";
   print "      </address>\n";

   @aliases = ();

   push @aliases, sevensymbols($key);
   push @aliases, sevenalpha($key);

   $region = $$ref{"REGION"};
   $region =~ s/ \([0-9, ]*\)$//g;
   $region = lc($region);
   push @aliases, $region;

   $owner = $$ref{"OWNER_NAME"};
   $owner = lc($owner);
   push @aliases, $region." ".$owner;

   $name = $$ref{"OBJECT_NAME"};
   $name =~ s/\[([^\]]*)\]/push @aliases, lc($1)/ge;

   print "      <aliases>\n";
   foreach $alias (@aliases) {
      $alias =~ s/\&/\&amp;/g;
      $alias =~ s/\</\&lt;/g;
      $alias =~ s/\>/\&gt;/g;
      print "         <alias>$alias</alias>\n";
   }
   print "      </aliases>\n";

   @flags = ();
   $name = $$ref{"OBJECT_DESC"};
   $name =~ s/\{([^\}]*)\}/push @flags, lc($1)/ge;

   print "      <flags>\n";
   foreach $flag (@flags) {
      print "         <flag>$flag</flag>\n";
   }
   print "      </flags>\n";

   print "   </gate>\n";
}

print "</gates>\n";

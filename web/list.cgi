#!/usr/bin/perl

############# seeds

if (-e "seeds") {
   open SEEDS, "seeds";
   while (<SEEDS>) {
      chomp $_;
      $seeds{$_} = 1;
   }
   close SEEDS;
}

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

############# texture key hashes

%texturehash = (
      "bfe92f57" => "milkyway",
      "24b8ae60" => "battlezone",
      "daaebcc7" => "ebony",
      "d23e2b2c" => "ice",
      "0cc93587" => "pegasus",
      "85090267" => "simple",

      "65748bc5" => "milkyway x", # v189
      "4c08bb7c" => "pegasus x", # v189
      "df0fda07" => "ebony x", # v189
      "b898f481" => "battlezone x", # v189
      "c9111d02" => "ice x", # v189
      "55d3176c" => "simple x", # v189

      "e2de32ef" => "borg", # by crysti thor
      "842deb89" => "nikl", # by nikl kanto

      "ffffffff" => "dummy"
      );

%oldtexturehash = (
      "080c9e13" => "milkyway", # older
      "3c26c7e7" => "negative",
      "3c26c7e7" => "negative",
      "47478038" => "ebony (flat)",
      "4c08bb7c" => "pegasus",
      "55d3176c" => "simple",
      "5ea3f725" => "milkyway (flat)",
      "65748bc5" => "milkyway",
      "6a1e546a" => "milkyway (flat)", # oldest
      "78838128" => "battlezone (flat)", # old
      "831a11e6" => "pegasus (flat)", #oldestish
      "842deb89" => "custom", # nikl kanto, flat, custom chevrons
      "87325a04" => "milkyway (flat)", # ancient
      "87a54ea7" => "milkyway", # another older
      "87e75700" => "milkyway (flat)", #older
      "93d1eb14" => "pegasus (flat)", #oldestish
      "b01183b0" => "ice",
      "b898f481" => "battlezone",
      "c9111d02" => "ice",
      "cd87e647" => "milkyway", # older
      "df0fda07" => "ebony",
      "e2de32ef" => "borg",
      "e95bd798" => "milkyway (flat)", # old
      "ffffffff" => "dummy"
      );

############# script key hashes

%scripthash = (
      "6ad0952f" => "", # v183
      "449d3828" => "", # v184
      "105a21f0" => "", # v185

      "c4fc6be4" => "", # v186 on 1.24 server
      "fa73a514" => "", # v186 on 1.25 server
      "4126f26c" => "", # v186 on 1.25 server ???

      "e03ff3be" => "", # v187 on 1.24 server
      "564f3159" => "", # v187 on 1.25 server

      "1518bfd2" => "", # v188
      
      "a9c52022" => "", # v189 on 1.24 server
      "dae1d443" => "", # v189 on 1.25 server

      "5969c80b" => "", # v190 on 1.24 server
      "86d6252f" => "", # v190 on 1.25 server

      "626c2208" => "", # v191

      "95d72c1d" => "", # v194 on 1.24 server
      "afe63a9a" => "", # v194 on 1.25 server

      "fa0b066f" => "", # v195 new method

      "92511a4e" => "", # v196 newer method

      "a6374ae5" => "", # v197 newer method

      "0fbea5e7" => "", # v198 newer method

      "dffe093e" => "", # v199
      "cddc7dd2" => "", # v200
      "a4094e12" => "", # v201
      "ea2461e4" => "", # v202
      "4599d901" => "", # v203
      "635ec425" => "", # v204
      "12989681" => "", # v205
      "3a5ab214" => "", # v206
      "4ec4339f" => "", # v207
      "919d14e4" => "", # v208
      "49b46bbb" => "", # v209
#wtf?
      "79ce28cc" => "", # v211

      "397d37e7" => "", # v212
      "0cd9161a" => "", # v213
      "b450b6e0" => "", # v214
      "d42ff943" => "", # v215
      "1a06c52c" => "", # v216
      "94e87b80" => "", # v217
      "c8b4f1c9" => "", # v218,v219

      "4856e75f" => "", # v220
      "48d548a0" => "", # v221
      "a7e3439b" => "", # v222
      "63c7f2bc" => "", # v223
      "8b729eb3" => "", # v224
      "93ae243f" => "", # v225
      "78715933" => "", # v226
      "d04411dc" => "", # v227
      "909dac21" => "", # v228
      "7566c81a" => "", # v229
      "8b592701" => "", # v230
      "14710f23" => "", # v231

      "50c36c9c" => "", # v300
      "f1e29e53" => "", # v301
      "198a52d1" => "", # v302
      "fc0e05f5" => "", # v303
      "c922792f" => "", # v304
      "3b004ebe" => "", # v305
      "79d2e792" => "", # v306
      "28b8ea5a" => "", # v307
      "2a71ad71" => "", # v308
      "b17545a8" => "", # v309
      "0b4a36fb" => "", # v310
      "c6edcded" => "", # v311
      "d52d45e9" => "", # v312
      "f386e8f3" => "", # v313
      "82760674" => "", # v314
      "b7e9afd4" => "", # v315
      "8c9e1c73" => "", # v316
      "3e09f95e" => "", # v317
      "bf262b79" => "", # v318
      "915a94f7" => "", # v319
      "c762f620" => "", # v320
      "535ed032" => "", # v321
      "5f2845e7" => "", # v322
      "9bee8f6e" => "", # v323
      "410d7893" => "", # v324
      "d648ef92" => "", # v325
      "4364bca0" => "", # v326
      "95c064ff" => "", # v327
      "7a3cd329" => "", # v328
      "687d2a7d" => "", # v329
      "e6cfaba8" => "", # v330
      "2120d94b" => "", # v331
      "717a08df" => "", # v332
      "5b8adc85" => "", # v333
      "2d5ecbd0" => "", # v334
      "168b50fb" => "", # v335
# no v336!
      "a31d3520" => "", # v337
      "8f1fb734" => "", # v338
      "e94bc500" => "", # v339
      "b17f32d2" => "", # v340
      "ccfb1aaf" => "", # v341
      "463530e5" => "", # v342
      "78a5c31d" => "", # v343
      "9a456f6b" => "", # v344
      "3d66e02e" => "", # v345
      "64f74a0e" => "", # v346
      "d2e87aee" => "", # v347
      "57e5e436" => "", # v348
      "446b7d69" => "", # v349

      "f2a42d4c" => "", # eleven",    # v350
      "3ea8f0f4" => "", # oneprim",   # v350
      "32ca5294" => "", # supergate", # v350
      "bfc83a6b" => "", # warp",      # v350
      "2c95ceaa" => "", # cleary",    # v350
      "1239482b" => "", # alt_peg",   # v350
      "066b0552" => "", # reboot",    # v350
      "726c639c" => "", # destiny2",  # v350
      "37bee34d" => "", # anglia",    # v350

      "b2c31ee7" => "", # v353
      "5882b63a" => "", # v354
      "6149a107" => "", # v355
      "230a5504" => "", # v356
      "0dbdab7b" => "", # v357
      "f9b2b4c1" => "", # v358
      "21ed4382" => "", # v360
      "2a8d3865" => "", # v361

      "ffffffff" => "dummy" # must be last
      );

############# begin main program

use CGI qw/:standard/;

$query = new CGI();

print "Content-type: text/html; charset=utf-8\n\n";

$count = 0;

### begin combined new and old stuff
$dirnames = "gates,/home/opengate/public_html/chord9/gates";
if (defined(param('dirnames'))) {
   $dirnames = param('dirnames');
}
@dirnames = split /,/, $dirnames;
### end combined

foreach $dirname (@dirnames) {
   # reject anything that looks sneaky
   if ($dirname =~ /\.\./ || (($dirname =~ /^\//) && !($dirname =~ /^\/home\/opengate\//))) {
      print "rejecting $dirname\n";
      next;
   }
   @keys = readpipe("ls $dirname");
   foreach $key (@keys) {
      chomp $key;
      @bar = readpipe "cat $dirname/$key";
      foreach $bar (@bar) {
         chomp $bar;
      }
      $ref = { };
      if ($bar[0] =~ /:/) {
   # it is new, do new stuff
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
         if ($$ref{"SHARD"} eq "Testing") {
            $$ref{"grid"} = "aditi";
         }
         $gates{$key} = $ref;
         $count++;
      }
      else {
   # it is old, do old stuff
         for ($i = 0; $i < @bar; $i += 2) {
            $$ref{$bar[$i]} = $bar[$i+1];
            if ($bar[$i] eq "url") {
               $url2id{$bar[$i + 1]} = $key;
            }
         }
         if (defined($$ref{"BORN"}) && defined($$ref{"TIMESTAMP"})) {
            $$ref{"AGE"} = ((0+$$ref{"TIMESTAMP"}) - (0+$$ref{"BORN"})) / (60*60*24);
         }
         $gates{$key} = $ref;
         $count++;
      }
   }
}

foreach $key (@keys) {
   $ref = $gates{$key};
   if (defined($$ref{"prev"}) &&
         defined($url2id{$$ref{"prev"}})) {
      $$ref{"prev"} = $url2id{$$ref{"prev"}};
   }
   if (defined($$ref{"next"}) &&
         defined($url2id{$$ref{"next"}})) {
      $$ref{"next"} = $url2id{$$ref{"next"}};
   }
}

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
         $ret = lc($$refa{$whatever}) cmp lc($$refb{$whatever});
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

sub selectem {
   my @ret = ();
   my $select = shift @_;
   my $key;
   my $ref;

   foreach $key (@_) {
      $ref = $gates{$key};

      if ($select == 1) {
         if ($$ref{"desc"} =~ "0,0") {
            push @ret, $key;
         }
         elsif ($$ref{"n"} == "0" && $$ref{"m"} == "0") {
            push @ret, $key;
         }
      }
      elsif ($select == 23) {
         if ($$ref{"f"} == "0" && $$ref{"r"} == "0") {
            push @ret, $key;
         }
      }
      elsif ($select == 2) {
         if (! ($$ref{"OBJECT_DESCRIPTION"} =~ /theme:/)) {
            push @ret, $key;
         }
      }
      elsif ($select == 3) {
         if (! (defined($scripthash{substr($$ref{"codehash"},0,8)}))) {
            push @ret, $key;
         }
      }
   }
   return @ret;
}

@sortedkeys = sort bywhatever keys(%gates);

if (defined($select)) {
   @sortedkeys = selectem($select, @sortedkeys);
}

print "<html>\n";
print "   <head>\n";
print "      <title>Second Life Astria Porta Open Stargate Network - " . localtime(time()) . "</title>\n";
print "<META name=\"keywords\" content=\"stargate,star gate,secondlife,second life,open source,opengate,open gate,doran,zemlja,doran zemlja,dhd,sci-fi,scifi,sci fi,science fiction,action\">\n";
print "   <style>\n";
print "\@font-face { font-family: pegasus; src: url('fonts/pegasus.ttf'); } \n";
print "\@font-face { font-family: milkyway; src: url('fonts/milkyway.ttf'); } \n";
print "\@font-face { font-family: opengate; src: url('fonts/opengate.ttf'); } \n";
print "   </style>\n";
print "   </head>\n";
print "   <body text=white bgcolor=black link=cyan vlink=blue alink=red>\n";

system "cat /home/opengate/open2/doc/header.txt";

print "<style>\n";
foreach $key(@sortedkeys) {
   $keysd = $key; $keysd =~ s/-//g;
   print "div#X$keysd\n";
   print "{\n";
   print "   display: none;\n";
   print "}\n";
}
print "</style>\n";

print "<script language=\"javascript\">\n";
print "<!--\n";
print "  function toggle(layer) {\n";
print "     var elem, vis;\n";
print "     if( document.getElementById ) // this is the way the standards work\n";
print "        elem = document.getElementById( layer );\n";
print "     else if( document.all ) // this is the way old msie versions work\n";
print "        elem = document.all[layer];\n";
print "     else if( document.layers ) // this is the way nn4 works\n";
print "        elem = document.layers[layer];\n";
print "     vis = elem.style;\n";
print "     if (vis.display == 'block')\n";
print "        vis.display = 'none';\n";
print "     else\n";
print "        vis.display = 'block';\n";
print " ";
print "  }\n";
print "// -->\n";
print "</script>\n";

print "<center>\n";
print "<font face=\"sans-serif\">\n";
print "<b>Astria Porta Open Stargate Network - ".localtime(time())."</b><br>\n";
print "<b>" . $count . " Stargates</b><br>\n";
print "<table cellpadding=5>\n";
print "<tr>";
print "<td>&nbsp;</td>";
print "<td>&nbsp;</td>";
print "<td><i>Region<br/><font size=-2>aliases</font></i></td>";
print "<td><i>Owner</i></td>";
print "<td><i>Address</i></td>";
print "<td><i>Rev</i></td>";
print "<td><i>Last Contact</i></td>";
print "<td><i>Flags</i></td>";
print "</tr>\n";

print "<tr><td colspan=8><hr/></td></tr>\n";

sub descape($) {
   my $x = shift @_;
   $x =~ s/u\+(....)/&#x$1;/g;
   return $x;
}

$total = $count;
$count = 0;
foreach $key(@sortedkeys) {

   $count++;

   $ref = $gates{$key};

   $keysd = $key; $keysd =~ s/-//g;

   $age = time() - $$ref{"TIMESTAMP"};

   @colors = ( "black", "gray", "yellow", "orange", "red",);

   $numcolors = @colors;
   $color = $colors[int($age / ($timeout/($numcolors)))];
   if (!defined($color)) { $color = "purple"; }

   $textcolor="white";
   if ($color ne "black") {
      $textcolor = "black";
   }

   $region = $$ref{"REGION"};
   $region =~ s/ \([^)]*\)$//g;

   $pos = $$ref{"LOCAL_POSITION"};
   $pos =~ s/[\(\)]//g;
   $pos =~ s/ //g;
   $pos =~ s/,/\//g;

   ($pos_x, $pos_y, $pos_z) = split /\//, $pos;
   $pos_x = int($pos_x * 10) / 10.0;
   $pos_y = int($pos_y * 10) / 10.0;
   $pos_z = int($pos_z * 10) / 10.0;
   $roundpos = "$pos_x/$pos_y/$pos_z";

   ($pos_x, $pos_y, $pos_z) = split /\//, $pos;
   $pos_x = int($pos_x);
   $pos_y = int($pos_y);
   $pos_z = int($pos_z);
   $intpos = "$pos_x/$pos_y/$pos_z";

   $tmp = $$ref{"OBJECT_NAME"};
   @aliases = ();
   $tmp =~ s/\[([^\]]*)\]/push @aliases, $1/ge;
   $tmp =~ s/\<([^\>]*)\>/push @aliases, $1/ge;

   $totalaliases += (0 + @aliases);

   @flags = ();

   $tmp = $$ref{"OBJECT_NAME"};
   $tmp =~ s/\{([^}\]]*)\}/push @flags, $1/ge;

   $tmp = $$ref{"OBJECT_DESCRIPTION"};
   $tmp =~ s/\{([^}\]]*)\}/push @flags, $1/ge;

   $tmp = $$ref{"OBJECT_DESC"};
   $tmp =~ s/\{([^}\]]*)\}/push @flags, $1/ge;

   @flags = sort(@flags);

   print "<tr id=\"$keysd\">\n";

   $alt = "$count/$total";
   $gridcolor = "white";
   if (defined($seeds{$$ref{"OBJECT_KEY"}})) {
      $gridcolor = "green";
   }
   if (!defined($$ref{"image"})) {
      print "<td>&nbsp;</td>";
   }
   else {
      print "<td><image src=\"http://secondlife.com/app/image/" . $$ref{"image"} . "/3\"></td>";
   }
   print "<td align=center><input type=image alt=\"$alt\" src=\"images/".$$ref{"grid"}.".png\" onclick=\"toggle('X$keysd')\"><br><font size=-2 color=$gridcolor>".$$ref{"grid"}."</font></td>\n";
   print "</td>\n";
   print "<td><a href=\"secondlife://$region/$roundpos\">$region</a><font size=-3>/$intpos</font>";

   if (@aliases) {
      foreach $alias (@aliases) {
         if ($dups{$alias} > 1) {
            $alias = "<font color=red>".$alias."</font>";
         }
      }
      print "<br/><font size=-1>".fixup(join(";", @aliases))."</font>";
   }
   else {
      print "";
   }
   print "</td>\n";

   if ($$ref{"OWNER_NAME"} ne $$ref{"OWNER_DISPLAY_NAME"}) {
      print "<td>".$$ref{"OWNER_NAME"}."<BR><font size=-1>".$$ref{"OWNER_DISPLAY_NAME"}."</font></td>";
   }
   else {
      print "<td>".$$ref{"OWNER_NAME"}."</td>";
   }
   print "<td align=center>";
   print sevensymbols($key);
   print "<br/>";
   print "<font style=\"font-family: milkyway\">";
   print sevenalpha($key);
   print "</font>";
   print "<br/>";
   print "<font size=-2 style=\"font-family: pegasus\">";
   print lc(sevenalpha($key));
   print "</font>";
   print "<br/>";
   print "<font size=-1>";
   print sevenalpha($key);
   print "</font>";
   print "</td>\n";

   if (!defined($$ref{"rev"})) {
      $$ref{"rev"} = "&nbsp;";
   }
   $rev = $$ref{"rev"};
   $rev =~ s/^(....).*/$1/g;

   print "<td align=center>".$rev;
   if (defined($$ref{"desc"})) {
      @desctmp = split / /, $$ref{"desc"};
      if (@desctmp > 9) {
         $scriptrev = $desctmp[9];
         $texrev = $desctmp[10];

         print "<br/><font size=-2>";
         if (defined($texturehash{$texrev})) {
            $texrev = $texturehash{$texrev};
         }
         print $texrev;
         print "<br/>";
         if (defined($scripthash{$scriptrev})) {
            $scriptrev = $scripthash{$scriptrev};
         }
         print $scriptrev;
         print "</font>";
      }
   }
   elsif (defined($$ref{"codehash"})) {
      print "<br/><font size=-2>";
      $texrev = $$ref{"OBJECT_DESCRIPTION"};
      $theme = "";
      $texrev =~ s/theme:([^}]*)/$theme=$1/ge;
      print $theme;
      print "<br/>";
      $scriptrev = $$ref{"codehash"};
      $scriptrev =~ s/^(........).*/$1/g;
      if (defined($scripthash{$scriptrev})) {
         $scriptrev = $scripthash{$scriptrev};
      }
      print $scriptrev;
      print "</font>";
   }
   print "</td>";

   print "<td style=\"color: $textcolor; background-color: $color;\">".iso8601ago($$ref{"TIMESTAMP"})."</td>\n";

   if (@flags) {
      print "<td><font size=-2>".join("<br>", @flags)."</font></td>";
   }
   else {
      print "<td>&nbsp;</td>";
   }

   print "</tr>\n";
   print "<tr><td colspan=8>";
   print "<div id='X$keysd'>\n";

   print "<font size=-2>$alt</font>\n";
   print "<table border=1 width=100%>\n";
   print "<tr><td><i>key</i></td><td><i>value</i></td></tr>\n";
   foreach my $subkey (sort(keys(%$ref))) {
      my $subval = $$ref{$subkey};
      if ($subkey eq "TIMESTAMP" ||
          $subkey eq "BORN" ||
          $subkey =~ /:[0-9]{4}/ ) {
         $subval = iso8601ago($subval);
      }
      $subval =~ s/\%(..)/chr(hex($1))/ge;
      if ($subval =~ /^[-a-f0-9,]+$/) {
         $subval =~ s/,/,<br>/g;
      }
      print "<tr><td>$subkey</td><td>$subval</td></tr>\n";
   }
   print "</table>\n";

   print "</div>\n";
   print "</td></tr>\n";
}

print "   </body>\n";
print "</html>\n";


######
# ISO8601 time plus "ago" format
######

sub iso8601ago($) {
   my $t = shift @_;
   my $now = time();
   my $age = $now - $t;
   my @gmtime = gmtime($t);

   my $ret = sprintf("%04d-%02d-%02d %02d:%02d:%02d",
         $gmtime[5] + 1900,
         $gmtime[4] + 1,
         $gmtime[3],
         $gmtime[2],
         $gmtime[1],
         $gmtime[0]);

   $ret .= "<br><center><font size=-1>";
   if ($age >= (2*24*60*60)) {
      $ret .= sprintf("%0.1f days ago", $age/(24*60*60));
   }
   elsif ($age >= (2*60*60)) {
      $ret .= sprintf("%0.1f hours ago", $age/(60*60));
   }
   elsif ($age >= (2*60)) {
      $ret .= sprintf("%0.1f minutes ago", $age/60);
   }
   else {
      $ret .= sprintf("%0.1f seconds ago", $age);
   }
   $ret .= "</font></center>";

   return $ret;
}

######
# fixup
######

sub fixup($) {
   my $arg = shift @_;
   $arg =~ s/\&/\&amp;/g;
   $arg =~ s/u\+(....)/&#x$1;/g;
   return $arg;
}


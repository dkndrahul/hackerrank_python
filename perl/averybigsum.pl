#!/usr/bin/perl

use strict;
use warnings;

# Complete the aVeryBigSum function below.
sub aVeryBigSum {
    my $arr = shift;
    my $count = 0;
    foreach (0..(scalar(@$arr) -1)) {
        $count += @$arr[$_];        
    }
    return $count;
}

open(my $fptr, '>', $ENV{'OUTPUT_PATH'});

my $ar_count = <>;
$ar_count =~ s/\s+$//;

my $ar = <>;
$ar =~ s/\s+$//;
my @ar = split /\s+/, $ar;

my $result = aVeryBigSum \@ar;

print $fptr "$result\n";

close $fptr;
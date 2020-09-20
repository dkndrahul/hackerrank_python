#!/usr/bin/perl

use strict;
use warnings;

#
# Complete the simpleArraySum function below.
#
sub simpleArraySum {
    my $params = shift;
    my $result;
    foreach (@$params) {
        $result += $_;
    }

    return $result;

}

open(my $fptr, '>', $ENV{'OUTPUT_PATH'});

my $ar_count = <>;
$ar_count =~ s/\s+$//;

my $ar = <>;
$ar =~ s/\s+$//;
my @ar = split /\s+/, $ar;

my $result = simpleArraySum \@ar;

print $fptr "$result\n";

close $fptr;
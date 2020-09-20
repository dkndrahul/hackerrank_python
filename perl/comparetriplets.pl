#!/usr/bin/perl

use strict;
use warnings;

# Complete the compareTriplets function below.
sub compareTriplets {
    my $alice = shift;
    my $bob = shift;
    my $acount=0;
    my $bcount = 0;
    foreach (0..2) {
        if (@$alice[$_] > @$bob[$_]) {
            $acount++;
        } elsif(@$alice[$_] == @$bob[$_]) {
            next;
        } elsif (@$alice[$_] < @$bob[$_]) {
            $bcount++;
        }
    }
    my $result = [
        $acount,
        $bcount
    ];
    # if ($acount > $bcount) {
    #     $result = [
    #         $acount,
    #         $bcount
    #     ];
    # } else {
    #     $result = [
    #         $bcount,
    #         $acount
    #     ];
    # }
    return @$result;

}

open(my $fptr, '>', $ENV{'OUTPUT_PATH'});

my $a = rtrim(my $a_temp = <STDIN>);

my @a = split /\s+/, $a;

my $b = rtrim(my $b_temp = <STDIN>);

my @b = split /\s+/, $b;

my @result = compareTriplets \@a, \@b;

print $fptr join " ", @result;
print $fptr "\n";

close $fptr;

sub ltrim {
    my $str = shift;

    $str =~ s/^\s+//;

    return $str;
}

sub rtrim {
    my $str = shift;

    $str =~ s/\s+$//;

    return $str;
}
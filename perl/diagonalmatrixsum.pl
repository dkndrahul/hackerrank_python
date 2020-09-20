#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

sub diagonalDifference {
    my $array = shift;

    my $length = scalar(@$array);

    my ($pdiagonal, $sdiagonal, $result);

    for my $i (0..$length-1) {
        for my $j (0..$length -1) {
            if ($i == $j) {
                $pdiagonal += @$array[$i]->[$j];
            }
            if (($i + $j) == ($length - 1)) {
                $sdiagonal += @$array[$i]->[$j];
            }
        }
    }
    $result = $pdiagonal - $sdiagonal;
    
    return abs($result);

}

my $n = ltrim(rtrim(my $n_temp = <STDIN>));

my @arr = ();

for (1..$n) {
    my $arr_item = rtrim(my $arr_item_temp = <STDIN>);

    my @arr_item = split /\s+/, $arr_item;

    push @arr, \@arr_item;
}

my $result = diagonalDifference \@arr;

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

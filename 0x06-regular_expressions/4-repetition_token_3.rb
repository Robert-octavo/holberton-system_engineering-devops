#!/usr/bin/env ruby
# Find the regular expression that will match the above cases
#hbtn

puts ARGV[0].scan(/hbt?{1,}n/).join

#!/usr/bin/env ruby
# regular expression that takes the first argument and scans it for the substring "School"

puts ARGV[0].scan(/School/).join

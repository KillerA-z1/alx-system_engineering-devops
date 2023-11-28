#!/usr/bin/env ruby
#  script should output: SENDER,RECEIVER and FLAGS

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).map { |match| match.join(",") }.join(",")

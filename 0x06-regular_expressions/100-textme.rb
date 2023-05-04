#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/from:\+*\w*/).join[5..-1]
RECEIVER = ARGV[0].scan(/to:\+*\w*/).join[3..-1]
FLAGS = ARGV[0].scan(/flags:(.*?)\]/).join

msg = SENDER + "," + RECEIVER + "," + FLAGS
puts msg

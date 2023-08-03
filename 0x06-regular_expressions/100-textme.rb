#!/usr/bin/env ruby
# text = "[from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1]"
puts ARGV[0].scan(/\[from:(\w+|\+\d+)\]\s\[to:(\w+|\+\d+)\]\s\[flags:(.*?)\]/).join(',')

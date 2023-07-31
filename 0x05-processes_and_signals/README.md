# 0x05-processes and signals
---
## Scripts

* `0-what-is-my-pid`: Displays its own PID.
* `1-list_your_processes`: Displays a list of currently running processes.
* `2-show_your_bash_pid`: Displays lines containing the word "bash," thus allowing you to easily get the PID of your Bash process.
* `3-show_your_bash_pid_made_easy`: Displays the PID, along with the process name, of processes whose name contains the word "bash."
* `4-to_infinity_and_beyond`: Displays "To infinity and beyond" indefinitely with a sleep of 2 seconds in between each iteration.
* `5-dont_stop_me_now`: Stops the `4-to_infinity_and_beyond` process.
* `6-stop_me_if_you_can`: Stops the `4-to_infinity_and_beyond` process without using `kill` or `killall`.
* `7-highlander`: Displays "To infinity and beyond" indefinitely with a sleep of 2 seconds in between each iteration. It should also print "I am invincible!!!" when receiving a `SIGTERM` signal.
* `67-stop_me_if_you_can`: Stops the `7-highlander` process.
* `8-beheaded_process`: Kills the `7-highlander` process.

## Instructions

Make sure to make these scripts executable using `chmod u+x or 744  <script_name>` before running them. The scripts can be run by executing `./<script_name>` in the terminal.
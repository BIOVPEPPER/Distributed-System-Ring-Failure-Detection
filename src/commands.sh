#!/bin/bash

if [ $1 = "join" ]; then
	python3 server_client_new.py &
elif [ $1 = "leave" ]; then
	pkill python3
elif [ $1 = "list_mem" ]; then
	python3 tools.py "list_mem"
elif [ $1 = "list_self" ]; then
	python3 tools.py "list_self"
elif [ $1 = "list_pred" ]; then
	python3 tools.py "list_pred"
elif [ $1 = "list_succ1" ]; then
	python3 tools.py "list_succ1"
elif [ $1 = "list_succ2" ]; then
	python3 tools.py "list_succ2"
elif [ $1 = "set_loss_3" ]; then
	python3 tools.py "set_loss_3"
elif [ $1 = "set_loss_30" ]; then
	python3 tools.py "set_loss_30"
elif [ $1 = "set_loss_0" ]; then
	python3 tools.py "set_loss_0"
elif [ $1 = "get_loss" ]; then
	python3 tools.py "get_loss"
fi;

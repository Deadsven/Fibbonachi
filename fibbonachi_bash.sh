#!/bin/bash
echo -n "What should be the fibonacci limit ? "
read fib_length
fib_num1=0
fib_num2=1
for (( i = 0; i < fib_length; i++ )); do
	fib_res=$(($fib_num1+$fib_num2))
	fib_num2=$fib_num1
	fib_num1=$fib_res
done

echo -n "$fib_res "
echo ""

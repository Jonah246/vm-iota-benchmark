for i in {1..1000}
do
	echo "iota POW benchmark $i"
	time node send2.js 10 >> 1000_times_10.log
done

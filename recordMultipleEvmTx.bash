for i in {1..100}
do
    echo "evm Tx NO: $i"
    { time python3 main.py 1000 ; } 2>> evm_benchmark_log.txt
done

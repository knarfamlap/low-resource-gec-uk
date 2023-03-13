set -xe 

data=$1
path_to_model=$2
output_dir=$3

max_chunks=10
mkdir -p ${output_dir}

for i in $(seq 1 ${max_chunks});
do 
	split --number=l/${i}/${max_chunks} ${data} | python3 generate.py --path_to_model ${path_to_model} > ${output_dir}/${i}.out &
done 
wait

#for i in $(seq 1 ${max_chunks}); do cat ${output_dir}/${i}.out | python3 ~/unlp-2023-shared-task/scripts/tokenizer.py >> ${output_dir}/all.out; done
for i in $(seq 1 ${max_chunks}); do cat ${output_dir}/${i}.out >> ${output_dir}/all.out; done

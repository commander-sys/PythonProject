check_process_res() {
    # 进程资源检查
    echo '######states[2]: 进程资源检查######'
    local proc_list="ospfd|AdamPlugins|vpc_monitor|bfd_notice|bfdd-beacon|zebra|kni_single|dcos-agent|dcos_agent|infrastore"
    # 一次性获取所有资源数据
    local ps_data=$(ps -eww aux | grep -E "vpc_agent|dcgw_pal|${proc_list}" | grep -vE 'grep|awk|sed')
    # 资源检查逻辑
    local proc_cpu=$(echo "$ps_data" | grep -E "vpc_agent|${proc_list}" | awk '{if($3>20){print $11}}')
    local proc_cpu_pal=$(echo "$ps_data" | grep dcgw_pal | awk '{if($3>2500){print $11}}')
    local proc_mem=$(echo "$ps_data" | grep -E "dcgw_pal|${proc_list}" | awk '{if($4>2){print $11}}')
    local proc_mem_vpc_agent=$(echo "$ps_data" | grep vpc_agent | awk '{if($4>3){print $11}}')
    local proc_state=$(echo "$ps_data" | awk '{if($8=="Z"){print $11}}')
    # 输出检查结果
    if [ ! -n "${proc_cpu}" -a ! -n "${proc_cpu_pal}" -a ! -n "${proc_mem}" -a ! -n "${proc_mem_vpc_agent}" -a ! -n "${proc_state}" ]; then
        echo 'all process resource normal'states[2]=0
    else
        echo "ERROR: process resource error, please check"
    fi
    # 输出详细结果
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="vpc_agent|${proc_list}" '$11 ~ re {print $11, $3}' | \
        awk '{
            if ($2 > 20) print $1" cpu usage is "$2",WARNING!";
            else if ($2 > 10) print $1" cpu usage is "$2",Notice!";
            else print $1" cpu usage is "$2", < 10,Normal!";
        }'
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="dcgw_pal" '$11 ~ re {print $11, $3}' | \
        awk '{
            if ($2>2500) print $1" cpu usage is "$2",WARNING!";
            else print $1" cpu usage is "$2", < 2500,Normal!";
        }'
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="dcgw_pal|vpc_agent|${proc_list}" '$11 ~ re {print $11, $4}' | \
        awk '{
            if ($2>2) print $1" mem usage is "$2",WARNING!";else print $1" mem usage is "$2", < 2,Normal!";
        }'
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="dcgw_pal|vpc_agent|${proc_list}" '$11 ~ re {print $11, $8}' | \
        awk '{
            if($2=="Z") print $1" process_state is "$2",WARNING!";
        }'
    echo -e '\n\n'
}
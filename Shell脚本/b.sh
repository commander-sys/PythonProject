check_process_res() {
    # 进程资源检查函数开始

    # 打印检查标题
    echo '######states[2]: 进程资源检查######'

    # 定义需要监控的进程列表，使用|分隔多个进程名
    local proc_list="ospfd|AdamPlugins|vpc_monitor|bfd_notice|bfdd-beacon|zebra|kni_single|dcos-agent|dcos_agent|infrastore"

    # 获取所有目标进程的资源使用数据，排除grep/awk/sed等工具进程
    local ps_data=$(ps -eww aux | grep -E "vpc_agent|dcgw_pal|${proc_list}" | grep -vE 'grep|awk|sed')

    # 检查CPU使用率超过20%的进程(vpc_agent和proc_list中的进程)
    local proc_cpu=$(echo "$ps_data" | grep -E "vpc_agent|${proc_list}" | awk '{if($3>20){print $11}}')
    # 检查dcgw_pal进程CPU使用率超过2500%
    local proc_cpu_pal=$(echo "$ps_data" | grep dcgw_pal | awk '{if($3>2500){print $11}}')
    # 检查内存使用率超过2%的进程(dcgw_pal和proc_list中的进程)
    local proc_mem=$(echo "$ps_data" | grep -E "dcgw_pal|${proc_list}" | awk '{if($4>2){print $11}}')
    # 检查vpc_agent进程内存使用率超过3%
    local proc_mem_vpc_agent=$(echo "$ps_data" | grep vpc_agent | awk '{if($4>3){print $11}}')
    # 检查僵尸进程(状态为Z)
    local proc_state=$(echo "$ps_data" | awk '{if($8=="Z"){print $11}}')

    # 输出总体检查结果
    if [ ! -n "${proc_cpu}" -a ! -n "${proc_cpu_pal}" -a ! -n "${proc_mem}" -a ! -n "${proc_mem_vpc_agent}" -a ! -n "${proc_state}" ]; then
        echo 'all process resource normal'states[2]=0
    else
        echo "ERROR: process resource error, please check"
    fi

    # 输出详细的CPU使用率报告(vpc_agent和proc_list中的进程)
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="vpc_agent|${proc_list}" '$11 ~ re {print $11, $3}' | \
        awk '{
            if ($2 > 20) print $1" cpu usage is "$2",WARNING!";
            else if ($2 > 10) print $1" cpu usage is "$2",Notice!";
            else print $1" cpu usage is "$2", < 10,Normal!";
        }'

    # 输出dcgw_pal进程的CPU使用率报告
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="dcgw_pal" '$11 ~ re {print $11, $3}' | \
        awk '{
            if ($2>2500) print $1" cpu usage is "$2",WARNING!";
            else print $1" cpu usage is "$2", < 2500,Normal!";
        }'

    # 输出内存使用率报告
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="dcgw_pal|vpc_agent|${proc_list}" '$11 ~ re {print $11, $4}' | \
        awk '{
            if ($2>2) print $1" mem usage is "$2",WARNING!";else print $1" mem usage is "$2", < 2,Normal!";
        }'

    # 输出进程状态报告(检查僵尸进程)
    echo "-----------------------------------------------"
    echo "$ps_data" | awk -v re="dcgw_pal|vpc_agent|${proc_list}" '$11 ~ re {print $11, $8}' | \
        awk '{
            if($2=="Z") print $1" process_state is "$2",WARNING!";
        }'

    # 输出两个空行分隔
    echo -e '\n\n'
}
import queue
from jupyter_client.manager import run_kernel




def knit_chunk(chunk_lines, param_eggs):
    output = []
    for line in chunk_lines:
        code = line
        with run_kernel() as kc:
            msg_id = kc.execute(code)
            reply = kc.get_shell_msg(msg_id)
            print(reply['content'])
            print()

            n = 0
            while True:
                n += 1
                try:
                    io_msg = kc.get_iopub_msg(timeout=1)
                    if 'content' not in io_msg:
                        continue
                    content = io_msg['content']
                    print("{:d}:\t{}".format(n, content))
                    if 'text' in content:
                        output.append(content['text'])
                    if 'data' in content:
                        data = content['data']
                    if 'execution_state' in content:
                        state = content['execution_state']
                except queue.Empty:
                    print('timeout kc.get_iopub_msg')
                    break
    return output
    # from jupyter_client import KernelManager
    # import time
    # from queue import Empty
    #
    # km = KernelManager(kernel_name='ir')
    # km.start_kernel()
    # print(km.is_alive())
    #
    # for line in chunk_lines:
    #     try:
    #         c = km.client()
    #         msg_id = c.execute(line)
    #         state = 'busy'
    #         data = {}
    #         while state != 'idle' and c.is_alive():
    #             try:
    #                 msg = c.get_iopub_msg(timeout=1)
    #                 if 'content' not in msg:
    #                     continue
    #                 content = msg['content']
    #                 if 'data' in content:
    #                     data = content['data']
    #                 if 'execution_state' in content:
    #                     state = content['execution_state']
    #             except Empty:
    #                 pass
    #         print(data)
    #     finally:
    #         km.shutdown_kernel()
    #         print(km.is_alive())

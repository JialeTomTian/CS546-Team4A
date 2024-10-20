def construct_message_list(message, system_message=None):
    msglist = [{"role": "user", "content": message}]
    if system_message:
        msglist.insert(0, {"role": "system", "content": system_message})
    return msglist

# [ Avishkar Patil ] 

import time

def time_data(start_time):
    end = time.time()
    now = end - start_time
    now_time = now
    day = now_time // (24 * 3600)
    now_time = now_time % (24 * 3600)
    hour = now_time // 3600
    now_time %= 3600
    minutes = now_time // 60
    now_time %= 60
    seconds = now_time
    if(day!=0):
        return "%dd %dh %dm %ds" % (day, hour, minutes, seconds)
    if(hour!=0):
        return "%dh %dm %ds" % (hour, minutes, seconds)
    else:
        return "%dm %ds" % (minutes, seconds)


async def progress(current, total,up_msg, message, start_time):

    try:
        await message.edit(
            text = f"{up_msg} {current * 100 / total:.1f}% in {time_data(start_time)}"
                )
    except:
        pass

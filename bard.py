from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="XQg_zA4L1UClQssWKH5vAXpRtEaKCBrs0A85lLGxkouyyEiapUgoieE9UzfWQCk-JSGynQ."

x = Bard().get_answer("can you help me i feel stress")['content']
print(x)


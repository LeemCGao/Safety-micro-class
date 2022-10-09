from typing import Dict, Any

import Utils
import time

# tenantCode UserId x-token userProjectId
tenantCode = 0
userId = ""
x_token = ""
userProjectId = ""
#main = Utils.main(tenantCode,serId,x_token,userProjectId)
#需要更换对应网页的值(tenantCode，userId，x_token，userProjectId)
main = Utils.main('65000003', '204f0b94-4911-43f3-8936-9478cc94b2a1', '3', '0e8fd249-409d-4567-961c-e9f00a7e81ea')
main.init()
finishIdList: Dict[Any, Any] = main.getFinishIdList()
for i in main.getCourse():
    main.start(i)
    time.sleep(20)
    main.finish(finishIdList[i])



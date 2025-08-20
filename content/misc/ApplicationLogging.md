+++
title = "Application Logging"

weight = 15
+++

### Application Logging

Application operations are  written to log file by default stored in `home_folder/.resinsight/logs` If an error situation or crash happens, information related to the crash situation is writen to this log file. If you experience crash, please include the log file to help the developers to fix the crash.

## Example of log messages

```
[2025-07-24 07:39:52.648] [rotating_logger] [info] Completed C:/gitroot/ResInsight-regression-test/ModelData/2021.10.3dev_drogonsmry/realization-96/iter-3/eclipse/model/DROGON-96.SMSPEC
[2025-07-24 07:39:52.648] [rotating_logger] [info] Completed C:/gitroot/ResInsight-regression-test/ModelData/2021.10.3dev_drogonsmry/realization-97/iter-3/eclipse/model/DROGON-97.SMSPEC
[2025-07-24 07:39:52.648] [rotating_logger] [info] Completed C:/gitroot/ResInsight-regression-test/ModelData/2021.10.3dev_drogonsmry/realization-98/iter-3/eclipse/model/DROGON-98.SMSPEC
[2025-07-24 07:39:52.648] [rotating_logger] [info] Completed C:/gitroot/ResInsight-regression-test/ModelData/2021.10.3dev_drogonsmry/realization-99/iter-3/eclipse/model/DROGON-99.SMSPEC
[2025-07-24 07:39:53.552] [rotating_logger] [info] Completed C:/gitroot/ResInsight-regression-test/ModelData/2021.10.3dev_drogonsmry/realization-93/iter-3/eclipse/model/DROGON-93.SMSPEC
[2025-07-24 07:39:53.553] [rotating_logger] [info] ERROR : Optimized Summary Reader error : neigther unified or non-unified result files found
```
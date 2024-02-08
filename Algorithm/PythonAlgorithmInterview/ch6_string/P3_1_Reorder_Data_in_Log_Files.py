class P3_1_Reorder_Data_in_Log_Files:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:

        # 1. separate logs
        letterLogs = []
        digitLogs = []
        for log in logs:
            if (log.split()[1].isalpha()):
                letterLogs.append(log)
            else:
                digitLogs.append(log)


        # 2. sort letter Logs
        letterLogs = letterLogs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # 3. combine letter logs and digit logs and return
        return letterLogs + digitLogs






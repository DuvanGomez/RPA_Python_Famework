
import States.Functions.InitAllSettings as stateInit


def init_State(strPathData):
    config = stateInit.initAllSettings(strPathData)
    dataset = stateInit.readSetupFiles(config)
    return config, dataset

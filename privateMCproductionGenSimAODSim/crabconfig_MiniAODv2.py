from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "DigiReco_STEP2"
config.General.workArea = 'crab_TTbarPowloops_DigiRecoStep2'
config.General.transferLogs = False

config.section_("JobType")
#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TTbb_Fall17-Powloops-Pythia_MiniAODv2_cfg.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.maxMemoryMB = 2500
config.JobType.maxJobRuntimeMin = 1440

config.section_("Data")
#config.Data.outputPrimaryDataset = 'RelValJetFlavourMiniAOD'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
#config.Data.unitsPerJob = 2
#config.Data.totalUnits = 9000
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1'
config.Data.inputDBS = 'phys03'
## T3 Beijing
config.Data.ignoreLocality = True
#config.Data.outLFNDirBase = '/store/group/phys_higgs'
## T3 Beijing
#config.Data.userInputFiles =[
config.Data.inputDataset = ('PLEASE ADD THE NAME OF THE DIGI RECO STEP2 DATASET')
# ]

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist = ['T2_*','T1_*']

config.section_("User")

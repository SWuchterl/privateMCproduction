from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "DigiRecoStep1"
config.General.workArea = 'crab_TTbarSemilep_Powloops'
config.General.transferLogs = False

config.section_("JobType")
#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TTbar_Powloops_2017_DigiReco_1_cfg.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.maxMemoryMB = 2500

config.section_("Data")
#config.Data.outputPrimaryDataset = 'RelValJetFlavourMiniAOD'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.unitsPerJob = 2
#config.Data.totalUnits = 9000
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2-STEP1'
config.Data.inputDBS = 'phys03'
## T3 Beijing
config.Data.ignoreLocality = True
#config.Data.outLFNDirBase = '/store/group/phys_higgs'
## T3 Beijing
#config.Data.userInputFiles =[
config.Data.inputDataset = ('PLEASE ADD HERE THE GENSIM DATASET AS INPUT ')
# ]

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist = ['T2_*','T1_*']

config.section_("User")

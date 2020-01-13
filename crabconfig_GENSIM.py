from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
# config.General.requestName = "ttbb_Powloops_GENSIM_1kEvents"
config.General.requestName = "ttPlus1J_Powheg_GENSIM_1kEvents"
# config.General.workArea = 'crab_ttbb_Powloops_GENSIM_1kEvents'
config.General.workArea = 'crab_ttPlus1J_Powheg_GENSIM_1kEvents'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
#name of the python cmsRun config to run
config.JobType.psetName = 'TTbb_PowhegOpenloops_Pythia8Config.py'
#config.JobType.inputFiles = ['GeneratorInterface/GenFilters/src/TopDecayFilter.cc', 'GeneratorInterface/GenFilters/python/TopDecayFilter_cfi.py','GeneratorInterface/GenFilters/python/interface/TopDecayFilter.h']
config.JobType.disableAutomaticOutputCollection = False
#settings below should be enough for 1000 events per job. would advice 800-1000 events per job (jobs will fail if you use too many)
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2500
config.JobType.maxJobRuntimeMin = 2750

config.section_("Data")
#Name of the private campaign. It is going to be published with /outputPrimaryDataset/username-outputDatasetTag/
# config.Data.outputPrimaryDataset = 'TTbb_Powheg_Openloops'
config.Data.outputPrimaryDataset = 'TTPlus1J_Powheg'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 750
# config.Data.totalUnits = 15000000
config.Data.totalUnits = 526933
#publication on das under prod/phys03.
config.Data.publication = True
#second part of the sample name
# config.Data.outputDatasetTag = 'TTbbtoSemileptonic_TuneCP5_PSweights_13TeV-powheg-openloops-pythia8-Fall17GS'
config.Data.outputDatasetTag = 'TTPlus1J_PowhegToDilepton_TuneCP5_PSweights_13TeV-powheg-pythia8-GENSIM-v0'


config.section_("Site")
#site where you have your t2 account and grid storage
config.Site.storageSite = 'T2_DE_DESY'
#configure which sites to run on
config.Site.whitelist = ["T1_DE_KIT","T2_DE_DESY","T1_US_FNAL","T1_UK_RAL","T2_CH_CERN"]

config.section_("User")
## only german users
config.User.voGroup = "dcms"

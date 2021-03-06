from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProduction"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'pythonLHEGEN_cfg.py'
config.JobType.inputFiles = ['GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh', 'gridpack.tgz']
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.outputPrimaryDataset = 'privateMCProductionLHEGEN'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1100
config.Data.totalUnits = #NUMBEREVENTS#
config.Data.publication = False
config.Data.outputDatasetTag = 'eventLHEGEN'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
config.Site.blacklist = ['T3_US_UMiss']

config.section_("User")
config.User.voGroup = "dcms"

